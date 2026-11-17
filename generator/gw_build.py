import json,sys,shutil,os
D=os.path.dirname(os.path.abspath(__file__))
from reels import R
T=open(f'{D}/gw_base.html').read()
for name,bgn in [(a.split(':')[0],a.split(':')[1]) for a in sys.argv[1:]]:
    d=json.load(open(f'{D}/{name}.json'))
    for sc,sp in zip(d['scenes'],R[name]['scenes']):
        for k,v in sp.items():
            if k not in sc: sc[k]=v
    bg=f'gbg_{bgn}.png'; shutil.copy(f'{D}/../video2/bg/{bgn}.png',f'{D}/{bg}')
    h=T.replace('/*TL*/',json.dumps(d)).replace('/*CFG*/',json.dumps(dict(bg=bg,tint='rgba(240,245,255,.8)')))
    open(f'{D}/{name}.html','w').write(h); print(name,bg)
