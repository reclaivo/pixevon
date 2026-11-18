"""QA for glass reels: python3 qa_bounds.py NAME [NAME...]  (run after gw_build.py, before render).
Fails (exit 1) if any glass tile or label leaves x 40..1040 at any sampled time, or a tile is not dark."""
import asyncio,json,os,sys
from playwright.async_api import async_playwright
HERE=os.path.dirname(os.path.abspath(__file__))
async def main():
    bad=0
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist','--allow-file-access-from-files'])
        pg=await b.new_page(viewport={'width':1080,'height':1920})
        for n in sys.argv[1:]:
            d=json.load(open(f'{HERE}/{n}.json'))
            await pg.goto(f'file://{HERE}/{n}.html'); await pg.wait_for_timeout(600)
            l,r=1e9,-1e9
            for s in d['scenes']:
                if s.get('vis')!='glass': continue
                for f in [x/20 for x in range(21)]:
                    await pg.evaluate(f"setT({s['t0']+(s['t1']-s['t0'])*f})")
                    q=await pg.evaluate("""()=>{let l=1e9,r=-1e9;document.querySelectorAll('#gl .gt[data-k]:not(#big),#gl .chip').forEach(e=>{const c=getComputedStyle(e);if(e.classList.contains('chip')&&parseFloat(c.opacity)<.05)return;const q=e.getBoundingClientRect();if(q.width<5)return;l=Math.min(l,q.left);r=Math.max(r,q.right)});return [l,r]}""")
                    l,r=min(l,q[0]),max(r,q[1])
            dark=await pg.evaluate("""()=>{const e=document.querySelector('#gl .gt[data-k]');return e?getComputedStyle(e).backgroundImage:''}""")
            ok=(l>=40 and r<=1040) and ('rgb(22, 33, 92)' in dark or dark=='')
            print(f'{n}: glass extent {l:.0f}..{r:.0f} dark_tiles={"rgb(22, 33, 92)" in dark or dark==""} -> {"OK" if ok else "FAIL"}')
            bad+=0 if ok else 1
        await b.close()
    sys.exit(1 if bad else 0)
asyncio.run(main())
