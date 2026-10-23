#!/usr/bin/env python3
"""Run authored JSON through a pinned exported runtime; never execute catalog code."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys
import time
from urllib.parse import urlsplit


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--catalog', type=Path, required=True)
    parser.add_argument('--runtime', type=Path, required=True)
    parser.add_argument('--collection', required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--check-logos', action='store_true')
    args = parser.parse_args()
    root, runtime, output = args.catalog.resolve(), args.runtime.resolve(), args.output.resolve()
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]*', args.collection):
        raise ValueError('Invalid collection ID')
    output.mkdir(parents=True, exist_ok=True)
    # Only the independently pinned runtime supplies executable scraper code.
    sys.path.insert(0, str(runtime))
    from server.scrapers.models import ScraperRecipe
    from server.scrapers.runtime import run_scraper
    from server.public_jobs.collector import PublicClient, HostLimiter
    manifest = json.loads((runtime / 'runtime-manifest.json').read_text())
    collection = json.loads((root / 'collections' / f'{args.collection}.json').read_text())
    if not 1 <= len(collection['companies']) <= 50:
        raise ValueError('Live validation is limited to 50 companies')
    entries = []
    for member in collection['companies']:
        company_id = member['company_id']
        for monitor_id in member.get('monitor_ids', []):
            if not all(re.fullmatch(r'[a-z0-9][a-z0-9-]*', v) for v in (company_id, monitor_id)):
                raise ValueError('Invalid source identity')
            company = json.loads((root / 'companies' / company_id / 'company.json').read_text())
            monitor = json.loads((root / 'companies' / company_id / 'monitors' / f'{monitor_id}.json').read_text())
            entries.append((company, monitor))
    limiter = HostLimiter()

    def validate(entry):
        company, monitor = entry
        recipe = ScraperRecipe.model_validate(monitor['recipe'])
        proof = {'id': monitor['id'], 'company_id': company['id'], 'revision': monitor['revision'],
                 'recipe_sha256': hashlib.sha256(json.dumps(monitor['recipe'], sort_keys=True, separators=(',', ':')).encode()).hexdigest(),
                 'runtime_revision': manifest['runtime_revision'], 'checked_at': datetime.now(timezone.utc).isoformat(),
                 'status': 'failed', 'job_count': 0, 'pages': 0, 'complete': False, 'descriptions': 0}
        try:
            if recipe.company != company['name'] or monitor['company_id'] != company['id']:
                raise ValueError('Company/monitor identity mismatch')
            with PublicClient(limiter, time.monotonic() + 180) as client:
                result = run_scraper(recipe, client=client, detail_cache={})
            proof.update(job_count=len(result.jobs), pages=result.pages_fetched, complete=result.complete,
                         descriptions=sum(bool(j.description) for j in result.jobs), warnings=result.warnings[:20],
                         samples=[{'title': j.title, 'location': j.location, 'source_url': j.source_url,
                                   'description_chars': len(j.description)} for j in result.jobs if j.description][:3])
            if not result.jobs or not proof['descriptions']:
                raise ValueError('Need live jobs and at least one live description')
            if any(urlsplit(j.source_url).scheme != 'https' or urlsplit(j.source_url).hostname not in recipe.allowed_hosts for j in result.jobs):
                raise ValueError('Unexpected public posting host')
            proof['status'] = 'pass'
        except Exception as exc:
            proof['error'] = f'{type(exc).__name__}: {exc}'[:500]
        print('BUBOOLE_VALIDATION ' + json.dumps(proof, ensure_ascii=False), flush=True)
        return proof

    with ThreadPoolExecutor(max_workers=4) as pool:
        proofs = list(pool.map(validate, entries))
    report = {'runtime_revision': manifest['runtime_revision'], 'sources': proofs}
    (output / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')

    if args.check_logos:
        from playwright.sync_api import sync_playwright
        import html
        urls = [company['logo_url'] for company, _ in entries]
        if any(urlsplit(url).scheme != 'https' or not urlsplit(url).hostname or urlsplit(url).username for url in urls):
            raise ValueError('Logos require public HTTPS URLs')
        hosts = {urlsplit(url).hostname for url in urls}
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(service_workers='block', accept_downloads=False, viewport={'width': 1200, 'height': 1000})
            context.route('**/*', lambda route: route.continue_() if urlsplit(route.request.url).scheme == 'https' and urlsplit(route.request.url).hostname in hosts else route.abort())
            page = context.new_page()
            cards = ''.join(f'<article><img src="{html.escape(company["logo_url"], quote=True)}"><p>{html.escape(company["name"])}</p></article>' for company, _ in entries)
            page.set_content('<style>body{font:14px sans-serif;display:grid;grid-template-columns:repeat(4,1fr);gap:12px;background:#ddd}article{padding:12px;background:white;text-align:center}img{width:230px;height:110px;object-fit:contain}</style>' + cards, wait_until='networkidle', timeout=60000)
            loaded = page.locator('img').evaluate_all('(images)=>images.map(i=>({url:i.src,loaded:i.complete&&i.naturalWidth>0}))')
            page.screenshot(path=str(output / 'logos.png'), full_page=True)
            report['logos'] = loaded
            (output / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
            print('BUBOOLE_LOGOS ' + json.dumps(loaded), flush=True)
            browser.close()
            if not all(item['loaded'] for item in loaded):
                raise RuntimeError('One or more logos did not load in Chromium')
    if any(proof['status'] != 'pass' for proof in proofs):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
