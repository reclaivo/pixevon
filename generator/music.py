import sys,numpy as np,soundfile as sf
from scipy.signal import butter,sosfilt
name=sys.argv[1]; SR=44100
import os; HERE=os.path.dirname(os.path.abspath(__file__)); w,sr=sf.read(f'{HERE}/{name}.wav'); 
if w.ndim>1: w=w.mean(1)
N=len(w); T=N/SR
rng=np.random.default_rng(5)
def hz(n): return 440*2**((n-69)/12)
chords=[[48,55,64,71],[45,52,60,67],[41,48,57,64],[43,50,59,64]]  # Cmaj7, Am7, Fmaj7, G6 (low voicing)
ch=2.9; m=np.zeros(N)
t=np.arange(N)/SR
def env(t0,t1,a,r):
    e=np.zeros(N); i0=int(t0*SR); i1=min(N,int(t1*SR)); n=i1-i0
    if n<=0: return e
    x=np.arange(n)/SR; d=(t1-t0); e[i0:i1]=np.minimum(1,x/a)*np.minimum(1,(d-x)/r).clip(0)
    return e
k=0;t0=-.2
while t0<T:
    for nt in chords[k%4]:
        f=hz(nt); e=env(max(0,t0),t0+ch+.6,.9,1.2)
        tone=sum(np.sin(2*np.pi*f*(1+d)*t+p)/(j+1) for j,(d,p) in enumerate([(0,0),(.003,1),(-.003,2)]))+.3*np.sin(2*np.pi*2*f*t)
        m+=tone*e*.12
    # soft bell arpeggio
    arp=[chords[k%4][i%4]+12 for i in (1,2,3,2,1,3)]
    for j,nt in enumerate(arp):
        ts=t0+.15+j*.45
        if ts<0 or ts>=T: continue
        i=int(ts*SR); n=min(N-i,int(1.4*SR)); x=np.arange(n)/SR; f=hz(nt+12)
        b=(np.sin(2*np.pi*f*x)+.35*np.sin(2*np.pi*2.01*f*x))*np.exp(-x*3.2)*np.minimum(1,x/.004)
        m[i:i+n]+=b*.05
    t0+=ch; k+=1
sos=butter(2,2200,'low',fs=SR,output='sos'); m=sosfilt(sos,m)
# reverb-ish: few delays
for dly,g in [(.23,.35),(.41,.25),(.67,.18)]:
    s=int(dly*SR); m[s:]+=m[:-s]*g
m=m/np.max(np.abs(m))
# fades
m*=np.minimum(1,t/.6)*np.minimum(1,(T-t)/1.0).clip(0)
# duck under voice+sfx energy
a=np.abs(w); sos2=butter(2,6,'low',fs=SR,output='sos'); en=sosfilt(sos2,a); en=en/np.max(en)
duck=1-.55*np.clip(en*3,0,1)
mix=w+m*.16*duck
mix=mix/np.max(np.abs(mix))*.93
sf.write(f'{HERE}/{name}_music.wav',mix,SR)
