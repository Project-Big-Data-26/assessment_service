/* node tests/animated_flow_browser_smoke.cjs <playwright-module> <chrome-exe> <output-dir>
   Serve the repo on 127.0.0.1:8765 first. Uses a fresh headless browser, no account. */
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const {chromium} = require(process.argv[2] || 'playwright');
(async () => {
  const output = path.resolve(process.argv[4] || 'runs/flow_documentation_qa');
  fs.mkdirSync(output,{recursive:true});
  const browser = await chromium.launch({executablePath:process.argv[3],headless:true});
  try {
    const page = await browser.newPage({viewport:{width:1440,height:1000},reducedMotion:'reduce'});
    const errors=[];
    page.on('pageerror',e=>errors.push(e.message));
    await page.goto('http://127.0.0.1:8765/API_DOCUMENTATION/33_ANIMATED_DATA_FLOW.html');
    await page.waitForFunction(()=>document.querySelectorAll('.node').length===window.FLOW_GRAPH.nodes.length);
    const applicationAssets=await page.locator('script[src],link[rel="stylesheet"]').evaluateAll(nodes=>nodes.map(node=>node.getAttribute('src')||node.getAttribute('href')).filter(url=>url.startsWith('interactive/')&&!url.includes('/vendor/')));
    assert.ok(applicationAssets.every(url=>new URL(url,'http://localhost/').searchParams.get('v')==='20261005-branches-2'));
    await page.screenshot({path:path.join(output,'overview.png'),fullPage:true});
    assert.equal(await page.locator('[data-focus="n3"]').getAttribute('aria-pressed'),'true');
    const layout=await page.evaluate(()=>{
      const map=document.querySelector('.map-panel').getBoundingClientRect(),detail=document.getElementById('stage-detail').getBoundingClientRect();
      const runs=[...document.querySelectorAll('.node.run')].map(node=>({width:node.getBoundingClientRect().width,fontSize:getComputedStyle(node.querySelector('.node-title')).fontSize}));
      const edges=[...document.querySelectorAll('#connectors path[data-from="model-blind-label"]')];
      return {mapWidth:map.width,detailBelowMap:detail.top>=map.bottom,runs,forkEdges:edges.length,edgesVisible:edges.every(e=>Number(getComputedStyle(e).opacity)>.8),labels:[...document.querySelectorAll('.edge-label')].map(e=>e.textContent)};
    });
    assert.ok(layout.mapWidth>1300,JSON.stringify(layout));
    assert.ok(layout.detailBelowMap);
    assert.ok(layout.runs.every(r=>r.width>=300&&r.fontSize==='16px'));
    assert.equal(layout.forkEdges,3);
    assert.ok(layout.edgesVisible);
    assert.ok(layout.labels.some(t=>t.includes('3–0')));
    assert.ok(layout.labels.some(t=>t.includes('2–1')));
    assert.ok(layout.labels.some(t=>t.includes('Run gagal')));
    assert.ok(layout.labels.some(t=>t.includes('Provider / schema gagal')));
    await page.locator('.map-panel').screenshot({path:path.join(output,'n3-focused.png')});
    await page.locator('[data-phase="Label AI"]').click();
    await page.locator('.node[data-stage="model-run-2"]').click();
    const runs=await page.locator('.node.run').evaluateAll(nodes=>nodes.map(n=>({hidden:n.hidden,top:n.getBoundingClientRect().top,left:n.getBoundingClientRect().left})));
    assert.equal(runs.length,3);
    assert.ok(runs.every(r=>!r.hidden));
    assert.ok(runs.every(r=>Math.abs(r.top-runs[0].top)<1));
    assert.equal(new Set(runs.map(r=>r.left)).size,3);
    await page.screenshot({path:path.join(output,'n3-branches.png'),fullPage:true});
    await page.locator('.node[data-stage="model-votes-lock"]').click();
    await page.locator('#stage-detail [data-target="model-adjudication"]').click();
    assert.match(await page.locator('#stage-detail h2').innerText(),/Adjudikasi/);
    const routes=await page.locator('#scenario option').evaluateAll(options=>options.map(o=>o.value));
    const routeResults=[];
    for(const id of routes) {
      await page.locator('#scenario').selectOption(id);
      const expected=await page.evaluate(id=>window.FLOW_GRAPH.routes.find(r=>r.id===id).stages,id);
      for(let i=1;i<expected.length;i++) await page.locator('#next').click();
      assert.equal(await page.locator('.node.active').getAttribute('data-stage'),expected.at(-1));
      assert.ok(await page.locator('#next').isDisabled());
      routeResults.push({id,lastStage:expected.at(-1),steps:expected.length});
    }
    // Autoplay must follow a selected branch and stop at its terminal node.
    await page.locator('#scenario').selectOption('incomplete');
    const timerResult=await page.evaluate(()=>{
      const speed=document.getElementById('speed');const option=new Option('QA fast','5');speed.add(option);speed.value='5';
      document.getElementById('play').click();return true;
    });
    assert.equal(timerResult,true);
    await page.waitForFunction(()=>document.querySelector('.node.active')?.dataset.stage==='model-checkpoint'&&!document.body.classList.contains('is-playing'));
    await page.locator('[data-view="lab"]').click();
    await page.locator('#temperature').fill('2');
    assert.match(await page.locator('#probability-bars').innerText(),/50\.65/);
    await page.locator('#temperature').fill('0');
    assert.equal(await page.locator('#classification-result').getAttribute('role'),'alert');
    await page.locator('#temperature').fill('1');
    assert.equal(await page.locator('#classification-result').getAttribute('role'),null);
    await page.locator('[data-view="summary"]').click();
    assert.equal(await page.locator('.ppt-card').count(),12);
    await page.locator('[data-view="reference"]').click();
    await page.locator('#expand-reference').click();
    assert.equal(await page.locator('#all-stages>details:not([open])').count(),0);
    await page.locator('[data-view="flow"]').click();
    const shortcutResults=[];
    for(const [focus,target] of [['n3','model-blind-label'],['validation','model-votes-lock'],['heads','model-token-encoder'],['irt','assessment-clean-matrix'],['all','model-source-json']]) {
      await page.locator(`[data-focus="${focus}"]`).click();
      assert.equal(await page.locator('.node.active').getAttribute('data-stage'),target);
      assert.equal(await page.locator(`[data-focus="${focus}"]`).getAttribute('aria-pressed'),'true');
      assert.equal(await page.locator('#stage-detail .technical-detail').getAttribute('open'),'');
      assert.ok(await page.locator('#stage-detail .technical-detail pre').count()>=2);
      shortcutResults.push(focus);
      if(focus==='validation') {
        const labels=await page.locator('.edge-label[data-from="model-votes-lock"]').evaluateAll(nodes=>nodes.map(node=>{const r=node.getBoundingClientRect();return {text:node.querySelector('text').textContent,left:r.left,right:r.right,top:r.top,bottom:r.bottom};}));
        assert.equal(labels.length,3);
        for(let i=0;i<labels.length;i++) for(let j=i+1;j<labels.length;j++) {
          const a=labels[i],b=labels[j];
          assert.ok(a.right<=b.left||b.right<=a.left||a.bottom<=b.top||b.bottom<=a.top,JSON.stringify(labels));
        }
      }
      if(['validation','heads','irt'].includes(focus)) await page.locator('.map-panel').screenshot({path:path.join(output,`${focus}-focused.png`)});
    }
    await page.locator('#technical-mode').uncheck();
    assert.equal(await page.locator('#stage-detail .technical-detail').getAttribute('open'),null);
    await page.locator('#open-stage-detail').click();
    assert.equal(await page.locator('#stage-detail .technical-detail').getAttribute('open'),'');
    assert.equal(await page.evaluate(()=>document.activeElement.id),'stage-detail');
    await page.locator('#scenario').selectOption('training');
    await page.locator('[data-phase="IndoBERT"]').click();
    await page.locator('.node[data-stage="model-head-difficulty"]').click();
    await page.screenshot({path:path.join(output,'indobert-branches.png'),fullPage:true});
    await page.setViewportSize({width:390,height:844});
    await page.locator('#scenario').selectOption('adjudication');
    await page.locator('[data-phase="Label AI"]').click();
    await page.locator('.node[data-stage="model-run-3"]').click();
    const mobile=await page.evaluate(()=>({width:innerWidth,documentWidth:document.documentElement.scrollWidth,mapScrollWidth:document.getElementById('map-scroll').scrollWidth,mapWidth:document.getElementById('map-scroll').clientWidth,selected:document.querySelector('.node.active').dataset.stage}));
    assert.ok(mobile.documentWidth<=mobile.width+1,JSON.stringify(mobile));
    assert.ok(mobile.mapScrollWidth>mobile.mapWidth);
    await page.screenshot({path:path.join(output,'mobile.png'),fullPage:true});
    await page.locator('[data-focus="n3"]').click();
    await page.locator('.node[data-stage="model-run-3"]').click();
    await page.locator('.map-panel').screenshot({path:path.join(output,'mobile-map.png')});
    assert.deepEqual(errors,[]);
    const report={passed:true,routes:routeResults,n3SeparateCards:true,layout,branchShortcuts:shortcutResults,versionedApplicationAssets:true,technicalDetailsAccessible:true,autoplayFollowsBranch:true,calculatorsResponsive:true,referenceExpandable:true,mobile,errors};
    fs.writeFileSync(path.join(output,'browser_verification.json'),JSON.stringify(report,null,2));
    console.log(JSON.stringify(report));
  } finally { await browser.close(); }
})().catch(e=>{console.error(e);process.exitCode=1;});
