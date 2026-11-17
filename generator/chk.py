import asyncio,sys,json
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg=await b.new_page(viewport={'width':1080,'height':1920}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        for n in sys.argv[1:]:
            d=json.load(open(f'/home/claude/pp/video3/{n}.json'))
            await pg.goto(f'file:///home/claude/pp/video3/{n}.html'); await pg.wait_for_timeout(700)
            ts=[0]+[s['t0']+(s['t1']-s['t0'])*f for s in d['scenes'][:-1] for f in (.55,.92)]
            for i,t in enumerate(ts):
                await pg.evaluate(f'setT({t})'); await pg.wait_for_timeout(60); await pg.screenshot(path=f'/tmp/c_{n}_{i}.jpg',type='jpeg',quality=70)
        print(errs[:5]); await b.close()
asyncio.run(main())
