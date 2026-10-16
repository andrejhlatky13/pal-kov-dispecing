from playwright.sync_api import sync_playwright
import os
U='file:///workspace/aha-dispecing/index.html';O='/workspace/aha-dispecing/shots/'
errs=[]
with sync_playwright() as p:
  b=p.chromium.launch()
  for name,vp in [('desktop',{'width':1280,'height':800}),('mobile',{'width':390,'height':844})]:
    c=b.new_context(viewport=vp,device_scale_factor=1);pg=c.new_page();pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U);pg.wait_for_timeout(500);pg.screenshot(path=O+f'{name}-1-login.png')
    pg.fill('#ln','Radko Krupička');pg.fill('#lp','dispecer');pg.click('button.pri');pg.wait_for_timeout(2500);pg.screenshot(path=O+f'{name}-2-dispecer.png',full_page=True)
    pg.click('text=Prehľad / export');pg.wait_for_timeout(300);pg.screenshot(path=O+f'{name}-4-prehlad.png',full_page=True)
    pg.click('text=Odhlásiť');pg.fill('#ln','Vlado Češko');pg.fill('#lp','vodic');pg.click('button.pri');pg.wait_for_timeout(300)
    pg.screenshot(path=O+f'{name}-3-vodic.png');pg.screenshot(path=O+f'{name}-3-vodic-full.png',full_page=True)
    c.close()
  b.close()
print(errs, os.listdir(O))
