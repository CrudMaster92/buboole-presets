const fs = require('node:fs'), vm = require('node:vm'), assert = require('node:assert/strict');
const source = fs.readFileSync(require('node:path').join(__dirname, '../site/app.js'), 'utf8');
const elements = new Map();
const context = { TextEncoder, btoa, state: {catalog: {source_commit:'test', collections:[{id:'fortune-50-2026'}]}},
  $: id => { if (!elements.has(id)) elements.set(id, {showModal(){}}); return elements.get(id); },
  renderDrawer(){}, keyOf: (a,b)=>`${a}:${b}`, selection: (c,m)=>({company_id:c.company_id,monitor_id:m.id,revision:1}) };
vm.createContext(context);
vm.runInContext(source.slice(source.indexOf('function selectable('), source.indexOf('function openBuboole(')), context);
vm.runInContext(source.slice(source.indexOf('function openBuboole('), source.indexOf('function matchingCompanyIds(')), context);
vm.runInContext(source.slice(source.indexOf('async function openCollection('), source.indexOf('function renderDrawer(')), context);
const members = Array.from({length:447}, (_,i)=>({company_id:`company-${i}`, monitors:[{id:`monitor-${i}`,verification:{status:'verified'}}]}));
context.collectionMembers = async()=>members;
(async()=>{
  await context.openCollection('fortune-50-2026');
  assert.equal(context.state.drawer.chosen.size, 0);
  const selections = members.map(c=>context.selection(c,c.monitors[0]));
  for (const batch of [selections.slice(0,200), selections.slice(200,400), selections.slice(400)]) {
    const payload = JSON.parse(Buffer.from(context.encodeHandoff('collection',batch,'fortune-50-2026'),'base64url').toString());
    assert.deepEqual(payload.selections,batch);
    assert.equal(payload.collection_id,'fortune-50-2026');
    assert.equal(payload.format,'jobhound-catalog-install');
    assert.equal(payload.version,1);
    assert.equal(payload.catalog_version,3);
  }
  let opened;
  context.window = {open: (...args)=>{opened=args;}};
  context.openBuboole('collection',selections.slice(0,200),'fortune-50-2026');
  const installUrl = new URL(opened[0]);
  assert.equal(installUrl.origin,'http://127.0.0.1:4175');
  assert.equal(installUrl.pathname,'/companies/presets');
  const installed = JSON.parse(Buffer.from(installUrl.hash.slice('#install='.length),'base64url').toString());
  assert.equal(installed.format,'jobhound-catalog-install');
  assert.deepEqual(installed.selections,selections.slice(0,200));
  assert.deepEqual(opened.slice(1),['_blank','noopener']);
  assert.match(elements.get('notice').textContent,/Buboole/);
  assert.throws(()=>context.encodeHandoff('collection',selections,'fortune-50-2026'), /1 and 200/);
  assert.throws(()=>context.encodeHandoff('collection',[],'fortune-50-2026'), /1 and 200/);
  context.collectionMembers = async()=>members.slice(0,200);
  await context.openCollection('fortune-50-2026');
  assert.equal(context.state.drawer.chosen.size,200);
  console.log('Large collection starts empty; exact 200/200/47 batches; empty and oversized handoffs rejected.');
})().catch(error=>{console.error(error);process.exitCode=1;});
