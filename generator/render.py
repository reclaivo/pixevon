import asyncio,os,shutil,json,sys,subprocess
from playwright.async_api import async_playwright
HERE=os.path.dirname(os.path.abspath(__file__))
name=sys.argv[1]; D=json.load(open(f'{HERE}/{name}.json')); FPS=30; N=int(D['total']*FPS)
only=[int(x) for x in sys.argv[2].split(',')] if len(sys.argv)>2 else None
out=f'{HERE}/fr_{name}'
if not only: shutil.rmtree(out,ignore_errors=True)
os.makedirs(out,exist_ok=True)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist','--allow-file-access-from-files'])
        pg=await b.new_page(viewport={'width':1080,'height':1920}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m:errs.append(m.text) if m.type=='error' else None)
        await pg.goto(f'file://{HERE}/{name}.html'); await pg.wait_for_timeout(1000)
        for i in (only if only else range(N)):
            await pg.evaluate(f'setT({i/FPS})'); await pg.wait_for_timeout(30)
            await pg.screenshot(path=f'{out}/f{i:04d}.jpg',type='jpeg',quality=92)
        print('errors',errs[:5]); await b.close()
asyncio.run(main())
if not only:
    wav=f'{HERE}/{name}_music.wav' if os.path.exists(f'{HERE}/{name}_music.wav') else f'{HERE}/{name}.wav'
    os.makedirs(f'{HERE}/out',exist_ok=True)
    subprocess.run(f'ffmpeg -y -loglevel error -framerate 30 -i {out}/f%04d.jpg -i {wav} -c:v libx264 -pix_fmt yuv420p -crf 18 -c:a aac -b:a 192k -af loudnorm=I=-14:TP=-1.5 -shortest {HERE}/out/{name}.mp4',shell=True,check=True)
    shutil.rmtree(out,ignore_errors=True); print('done',name)
