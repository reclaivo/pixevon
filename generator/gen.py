import os,sys,json,numpy as np,soundfile as sf
from scipy.signal import resample_poly
from reels import R
import sfxlib as L
name=sys.argv[1]; sc=R[name]['scenes']
import random
ALL=['office','desklight','camera','deskdark','shapes','bg1','bg2','bg3','bg4','bg5']
rg=random.Random(int(name[1:])*13+int(__import__('os').environ.get('SEEDADD','0'))); seq=ALL[:]; rg.shuffle(seq)
PHOTO={'office','desklight','camera','deskdark'}; DARK={'camera','deskdark','bg3','bg4','bg5'}
for i,s in enumerate(sc):
    b=seq[i%len(seq)]; s['bg']=b+'.png'; s['blur']=8 if b in PHOTO else 2; s['wash']=.8 if b in DARK else .72

from kokoro_onnx import Kokoro
k=Kokoro(os.path.expanduser(os.environ.get('KOKORO_DIR','~/tts'))+'/kokoro.onnx',os.path.expanduser(os.environ.get('KOKORO_DIR','~/tts'))+'/voices.bin')
t=0; tl=[]
for i,s in enumerate(sc):
    a,sr=k.create(s['line'],voice='af_heart',speed=s.get('sp',1.12),lang='en-us'); a=np.asarray(a,dtype=np.float32)
    idx=np.where(np.abs(a)>.01)[0]; a=a[idx[0]:idx[-1]+1]; d=len(a)/sr
    pre=s.get('pre',.08); post=s.get('post',.2); vs=t+pre; e=vs+d+post
    tl.append(dict(s,t0=round(t,3),vs=round(vs,3),vd=round(d,3),t1=round(e,3),aud=a,sr=sr)); t=e
total=round(t,2); print(name,'total',total); assert total<=15.0,total
SR=44100; N=int((total+.3)*SR); voice=np.zeros(N,np.float32); sfx=np.zeros(N,np.float32)
def put(b,x,tt,g=1):
    i=int(tt*SR); j=min(N,i+len(x))
    if 0<=i<N: b[i:j]+=(x[:j-i]*g).astype(np.float32)
for i,s in enumerate(tl):
    put(voice,resample_poly(s['aud'],147,80).astype(np.float32),s['vs'])
    cont=s.get('cont'); t0=s['t0']
    if i==0: put(sfx,L.impact(),0,1); put(sfx,L.pop(500,.2),.12,.5)
    elif cont: put(sfx,L.impact(),t0-.02,.9); put(sfx,L.whoosh(),t0-.2,.5)
    else: put(sfx,L.whoosh(),t0-.14,.55); put(sfx,L.pop(),t0+.03,.5)
    p=s.get('phone')
    if p:
        put(sfx,L.whoosh(.35),t0+.1,.4)
        for tk in p.get('tk',[]):
            if tk>0: put(sfx,L.tick(),t0+tk,.8); put(sfx,L.pop(900),t0+tk,.35)
        if p.get('btn'): put(sfx,L.thud(),t0+p['btn'],.8); put(sfx,L.tick(),t0+p['btn']+.02,.7)
    if s.get('layout')=='end': put(sfx,L.shimmer(),t0+.05,.35); put(sfx,L.pop(1100),t0+.32,.5)
    if s.get('extra')=='lock': put(sfx,L.thud(),t0+.7,.9)
    for n,u in s.get('sfx',[]): put(sfx,getattr(L,n)(),t0+u,.5)
def comp(x,th=.25,r=3.0):
    a=np.abs(x); g=np.where(a>th,(th+(a-th)/r)/np.maximum(a,1e-9),1); return x*g
voice=comp(voice); voice=voice/np.max(np.abs(voice))*.85; sfx=sfx/np.max(np.abs(sfx))*.5
mix=np.tanh((voice+sfx*.55)*1.1)/np.tanh(1.1); mix=mix/np.max(np.abs(mix))*.93
sf.write(f'{name}.wav',mix[:int(total*SR)],SR)
for s in tl: s.pop('aud'); s.pop('sr')
json.dump(dict(scenes=tl,total=total),open(f'{name}.json','w'))
html=open('template.html').read().replace('/*TL*/',json.dumps(dict(scenes=tl,total=total)))
open(f'{name}.html','w').write(html)
