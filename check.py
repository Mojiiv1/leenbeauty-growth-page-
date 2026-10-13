from playwright.sync_api import sync_playwright
from pathlib import Path
import json
base=Path('/mnt/data/leen-growth-page')
preview=(base/'qa'/'preview_inlined.html').read_text()
results=[]
with sync_playwright() as p:
  browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
  for width in [320,375,390,768,1024,1440]:
    page=browser.new_page(viewport={'width':width,'height':850},device_scale_factor=1)
    errors=[]
    page.on('pageerror',lambda exc:errors.append(str(exc)))
    page.set_content(preview,wait_until='domcontentloaded')
    page.locator('img[loading=lazy]').evaluate_all("ims=>ims.forEach(i=>i.loading='eager')")
    page.wait_for_function('Array.from(document.images).every(i=>i.complete)',timeout=20000)
    page.locator('img').first.wait_for(state='visible')
    photos=page.eval_on_selector_all('img','ims=>ims.map(i=>({src:i.getAttribute("src"),ok:i.complete&&i.naturalWidth>0}))')
    metrics=page.evaluate('({documentWidth:document.documentElement.scrollWidth, windowWidth:innerWidth, title:document.title})')
    anchors=page.locator('a[href]')
    button=page.locator('a.action-book')
    book=button.get_attribute('href')
    assert book=='https://book.daysmart.com/booking/service?DSID=DC-2162536'
    assert all(i['ok'] for i in photos),photos
    assert metrics['documentWidth']<=width,metrics
    assert not errors,errors
    page.get_by_role('button',name='FR').click()
    assert page.locator('html').get_attribute('lang')=='fr'
    assert page.get_by_text('Prendre rendez-vous').count()>0
    page.get_by_role('button',name='EN').click()
    assert page.locator('html').get_attribute('lang')=='en'
    if width in [390,1440]:
      page.locator('img').evaluate_all("imgs=>Promise.all(imgs.map(i=>i.decode().catch(()=>{})))")
      for idx in range(page.locator('img').count()):
        page.locator('img').nth(idx).scroll_into_view_if_needed()
        page.wait_for_timeout(100)
      page.evaluate('window.scrollTo(0,0)')
      page.wait_for_timeout(350)
      page.screenshot(path=str(base/'qa'/f'preview_{width}.png'),full_page=True,animations='disabled')
    results.append({'width':width,'no_overflow':True,'photos':len(photos),'all_photos_loaded':True,'links':anchors.count(),'en_fr_toggle':'passed','js_errors':[]})
    page.close()
  browser.close()
(base/'qa'/'report.json').write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2))
