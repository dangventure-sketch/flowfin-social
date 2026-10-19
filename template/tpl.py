import sys
from playwright.sync_api import sync_playwright
THEMES={
 'white':dict(bg='#FFFFFF',num='#039967',txt='#0F142B',mute='#8A8FA3',rule='#0F142B',logo='logo_dark.png'),
 'green':dict(bg='#039967',num='#FFFFFF',txt='#0F142B',mute='#D5F2E6',rule='#FFFFFF',logo='logo_white.png'),
 'black':dict(bg='#0B0D14',num='#039967',txt='#FFFFFF',mute='#7C8196',rule='#FFFFFF',logo='logo_light.png'),
}
def render(theme,num,line1,line2,src,out):
  t=THEMES[theme]
  html=f'''<!doctype html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:{t['bg']};font-family:Inter,sans-serif;color:{t['txt']};position:relative;overflow:hidden}}
.wrap{{position:absolute;left:130px;right:130px;top:{300 if len(num)<=7 else 260}px}}
.num{{white-space:{'nowrap' if len(num)<=7 else 'normal'};font-size:{300 if len(num)<=3 else (230 if len(num)<=7 else 104)}px;font-weight:800;letter-spacing:{-14 if len(num)<=7 else -3.5}px;line-height:{1 if len(num)<=7 else 1.04};color:{t['num']}}}
.line{{width:72px;height:6px;background:{t['rule']};margin:48px 0 44px}}
.txt{{font-size:54px;font-weight:600;line-height:1.22;letter-spacing:-1.2px}}
.txt span{{color:{t['mute']};font-weight:500}}
.foot{{position:absolute;left:130px;right:130px;bottom:150px;display:flex;justify-content:flex-end;align-items:flex-end}}
.src{{font-size:22px;color:{t['mute']};line-height:1.4;font-weight:500}}
.foot img{{height:34px}}
</style></head><body><div class="wrap"><div class="num">{num}</div><div class="line"></div>
<div class="txt">{line1}<br><span>{line2}</span></div></div>
<div class="foot"><img src="{t['logo']}"></div></body></html>'''
  open(out+'.html','w').write(html)
  import os
  with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
    pg.goto('file://'+os.path.abspath(out+'.html')); pg.wait_for_timeout(300); pg.screenshot(path=out+'.png'); b.close()
