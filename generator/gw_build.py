import json,sys,shutil,os
D=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,D)
from theme_dark import GW_DARK,DARK_TINT,apply,safe,bgfile
THEME=os.environ.get('REEL_THEME','dark')
from reels import R
T=open(f'{D}/gw_base.html').read()
if THEME=='dark': T=apply(T,GW_DARK)
T=safe(T,'const els=TL.scenes.map(mk);')
for name,bgn in [(a.split(':')[0],a.split(':')[1]) for a in sys.argv[1:]]:
    d=json.load(open(f'{D}/{name}.json'))
    for sc,sp in zip(d['scenes'],R[name]['scenes']):
        for k,v in sp.items():
            if k not in sc: sc[k]=v
    bg=f'gbg_{bgn}.png'; shutil.copy(bgfile(bgn),f'{D}/{bg}')
    h=T.replace('/*TL*/',json.dumps(d)).replace('/*CFG*/',json.dumps(dict(bg=bg,tint=(DARK_TINT if THEME=='dark' else 'rgba(240,245,255,.8)'))))
    open(f'{D}/{name}.html','w').write(h); print(name,bg)
