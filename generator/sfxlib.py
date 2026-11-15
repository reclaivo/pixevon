import numpy as np
from scipy.signal import butter, sosfilt
SR=44100
rng=np.random.default_rng(7)
def env(n,a=.005,d=3.0):
    t=np.arange(n)/SR; return np.minimum(1,t/a)*np.exp(-t*d)
def bp(x,lo,hi):
    return sosfilt(butter(2,[lo,hi],btype='band',fs=SR,output='sos'),x)
def whoosh(dur=.45):
    n=int(dur*SR); t=np.arange(n)/SR; x=rng.standard_normal(n)
    out=np.zeros(n)
    for k in range(6):
        c=500*(1.55**k)*(1+2.2*t/dur); 
    # sweep via time-varying cutoff approximated by blocks
    blk=int(.02*SR); y=np.zeros(n)
    for i in range(0,n,blk):
        f=400+5200*(i/n)**1.6; seg=x[i:i+blk]
        y[i:i+blk]=sosfilt(butter(2,[f*.7,min(f*1.4,SR/2-100)],btype='band',fs=SR,output='sos'),np.pad(seg,(0,0)))[:len(seg)]
    w=np.sin(np.pi*np.arange(n)/n)**1.5
    return (y*w*0.9).astype(np.float32)
def impact():
    n=int(.7*SR); t=np.arange(n)/SR; f=140*np.exp(-t*5)+38
    ph=2*np.pi*np.cumsum(f)/SR; s=np.sin(ph)*env(n,.002,5.5)
    nz=bp(rng.standard_normal(n),80,2500)*env(n,.001,18)*.6
    return (s*1.2+nz).astype(np.float32)
def pop(f0=900,dur=.14):
    n=int(dur*SR); t=np.arange(n)/SR; f=f0*np.exp(-t*14)+250
    return (np.sin(2*np.pi*np.cumsum(f)/SR)*env(n,.001,26)).astype(np.float32)
def tick():
    n=int(.06*SR); t=np.arange(n)/SR
    return ((np.sin(2*np.pi*2400*t)+.5*np.sin(2*np.pi*3600*t))*env(n,.0005,70)*.7).astype(np.float32)
def thud():
    n=int(.35*SR); t=np.arange(n)/SR; f=95*np.exp(-t*10)+45
    return (np.sin(2*np.pi*np.cumsum(f)/SR)*env(n,.002,11)*1.1).astype(np.float32)
def bell():
    n=int(1.3*SR); t=np.arange(n)/SR
    s=sum(a*np.sin(2*np.pi*f*t) for f,a in [(880,1),(1318.5,.55),(1760,.3),(2637,.15)])*env(n,.002,3.2)
    return (s*.5).astype(np.float32)
def glitch():
    n=int(.16*SR); x=rng.standard_normal(n); x=np.round(x*3)/3
    x=bp(x,400,6000)*env(n,.001,14)
    gate=(np.sin(np.arange(n)/SR*2*np.pi*45)>0).astype(float)
    return (x*gate*.9).astype(np.float32)
def shimmer():
    n=int(1.0*SR); t=np.arange(n)/SR
    s=sum(np.sin(2*np.pi*f*t) for f in [1568,2093,2637,3136])*(0.25)*np.sin(np.pi*np.minimum(1,t/1.0))**2
    return (s*(1+.4*np.sin(2*np.pi*7*t))).astype(np.float32)
def downsweep():
    n=int(.45*SR); t=np.arange(n)/SR; f=1400*np.exp(-t*5.5)+90
    return (np.sin(2*np.pi*np.cumsum(f)/SR)*env(n,.005,5)*.8).astype(np.float32)
def riser(dur):
    n=int(dur*SR); t=np.arange(n)/SR; x=rng.standard_normal(n)
    blk=int(.02*SR); y=np.zeros(n)
    for i in range(0,n,blk):
        f=300+5500*(i/n)**2; sg=x[i:i+blk]
        y[i:i+blk]=sosfilt(butter(2,[f*.8,min(f*1.3,SR/2-100)],btype='band',fs=SR,output='sos'),sg)[:len(sg)]
    tone=np.sin(2*np.pi*np.cumsum(180+900*(t/dur)**2)/SR)*.4
    return ((y*.8+tone)*(t/dur)**1.5).astype(np.float32)
