"""Render one FlowFin post image (1080x1350).
Usage: python3 template/render.py '<json>' out.png
json keys: theme (white|green|black), big (number like "21x" or a short headline),
line1 (main line, dark/bold), line2 (muted second line, optional)
"""
import json, os, sys, html as H
from playwright.sync_api import sync_playwright
HERE = os.path.dirname(os.path.abspath(__file__))
THEMES = {
 'white': dict(bg='#FFFFFF', num='#039967', txt='#0F142B', mute='#8A8FA3', rule='#0F142B', logo='logo_dark.png'),
 'green': dict(bg='#039967', num='#FFFFFF', txt='#0F142B', mute='#D5F2E6', rule='#FFFFFF', logo='logo_white.png'),
 'black': dict(bg='#0B0D14', num='#039967', txt='#FFFFFF', mute='#7C8196', rule='#FFFFFF', logo='logo_light.png'),
}
def render(theme, big, line1, line2, out):
    t = THEMES[theme]; n = len(big); short = n <= 7
    size = 300 if n <= 3 else (230 if short else 104)
    page = f'''<!doctype html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:{t['bg']};font-family:Inter,sans-serif;color:{t['txt']};position:relative;overflow:hidden}}
.wrap{{position:absolute;left:130px;right:130px;top:{300 if short else 260}px}}
.num{{white-space:{'nowrap' if short else 'normal'};font-size:{size}px;font-weight:800;letter-spacing:{-14 if short else -3.5}px;line-height:{1 if short else 1.04};color:{t['num']}}}
.line{{width:72px;height:6px;background:{t['rule']};margin:48px 0 44px}}
.txt{{font-size:54px;font-weight:600;line-height:1.22;letter-spacing:-1.2px}}
.txt span{{color:{t['mute']};font-weight:500}}
.foot{{position:absolute;left:130px;right:130px;bottom:150px;display:flex;justify-content:flex-end}}
.foot img{{height:34px}}
</style></head><body><div class="wrap"><div class="num">{H.escape(big)}</div><div class="line"></div>
<div class="txt">{H.escape(line1)}{'<br><span>'+H.escape(line2)+'</span>' if line2 else ''}</div></div>
<div class="foot"><img src="file://{HERE}/{t['logo']}"></div></body></html>'''
    tmp = os.path.abspath(out) + '.html'
    open(tmp, 'w').write(page)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width':1080,'height':1350})
        pg.goto('file://' + tmp); pg.wait_for_timeout(400); pg.screenshot(path=out); b.close()
    os.remove(tmp)
if __name__ == '__main__':
    d = json.loads(sys.argv[1]); render(d['theme'], d['big'], d['line1'], d.get('line2',''), sys.argv[2])
