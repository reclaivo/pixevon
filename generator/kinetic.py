# Build light-theme kinetic reel HTML. Usage: python3 kinetic.py K3 K6 ...  (needs NAME.json, NAME.wav, NAME_music.wav from gen.py/music.py, and kin2_base.html)
import json,sys,random,shutil,os
D=os.path.dirname(os.path.abspath(__file__))
T=open(f'{D}/kin2_base.html').read()
BGS=['office','desklight','camera','deskdark','shapes','bg1','bg2','bg3','bg4','bg5']
LIGHT=[
("#root{position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:hidden;background:radial-gradient(900px 700px at 50% 38%,#0E2150 0%,#071230 45%,#030816 100%)}","#root{position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:hidden;background:#EEF3FF}"),
("rgba(0,0,0,.65) 100%","rgba(20,40,100,.28) 100%"),("color:#DCE6FF","color:#0A1A44"),
(".w{font-size:88px;font-weight:900;line-height:1.08;color:#fff",".w{font-size:88px;font-weight:900;line-height:1.08;color:#0A1A44"),
("0 6px 24px rgba(0,0,0,.7)","0 4px 18px rgba(255,255,255,.95)"),
("text-shadow:0 0 18px var(--ac),0 0 44px var(--ac),","text-shadow:0 0 16px rgba(255,255,255,.95),0 0 4px rgba(255,255,255,.9),"),
("border:9px solid #22366F;background:#07102B;","border:9px solid #C9D6F5;background:#FFFFFF;"),
("box-shadow:0 0 60px rgba(70,120,255,.45),0 40px 80px rgba(0,0,0,.6)","box-shadow:0 30px 70px rgba(30,60,140,.35)"),
("0 40px 80px rgba(0,0,0,.6)","0 30px 70px rgba(30,60,140,.35)"),
("text-shadow:0 0 30px #5B8CFF,0 0 70px #3B6BFF","text-shadow:0 0 22px rgba(79,115,255,.3)"),
("text-shadow:0 0 30px #5B8CFF,0 0 80px #3B6BFF","text-shadow:0 0 22px rgba(79,115,255,.3)"),
("text-shadow:0 0 30px #FF2A44,0 0 70px #FF2A44","text-shadow:0 0 18px rgba(224,48,74,.3)"),
("#EAF1FF","#0A1A44"),("#6EA0FF","#2F5BFF"),("#FF4D5E","#E0304A"),("#FF2A44","#E0304A"),
("#34406B","#C7D2EE"),("#5A6798","#8FA0D0"),
('id="off" style="position:absolute;inset:0;background:#000','id="off" style="position:absolute;inset:0;background:#0A1330'),
("linear-gradient(160deg,#1A3FA8,#0B1D55 60%,#06102E)","linear-gradient(160deg,#F2F6FF,#D3E0FF 60%,#B7CBF8)"),
('fill="#7FA8FF" opacity=".9"','fill="#2F5BFF" opacity=".9"'),('stroke="#B9D0FF"','stroke="#2F5BFF"'),('fill="#9DBEFF"','fill="#3B64F0"'),
("background:rgba(40,80,200,.45);border:2px solid #7FA8FF;box-shadow:0 0 36px rgba(91,140,255,.8);","background:rgba(255,255,255,.9);border:2px solid #A9C0F5;box-shadow:0 14px 34px rgba(30,60,140,.3);"),
("font-size:56px;color:#fff","font-size:56px;color:#2F5BFF"),("#14235A","#D3DDF5"),
("rgba(${110+(1-q)*100},${160+(1-q)*60},255,${.4+.6*q})","rgba(${47+(1-q)*110},${91+(1-q)*80},255,${.4+.6*q})"),
("rgba(110,160,255,${.9*q})","rgba(47,91,255,${.5*q})"),
("background:#7FA8FF;box-shadow:0 0 20px #5B8CFF","background:#2F5BFF;box-shadow:0 0 16px rgba(47,91,255,.5)"),
("background:rgba(20,40,100,.85);border:2px solid #5B8CFF;box-shadow:0 0 40px rgba(91,140,255,.7);display:flex;align-items:center;gap:20px;padding-left:32px;color:#fff","background:rgba(255,255,255,.93);border:2px solid #A9C0F5;box-shadow:0 14px 36px rgba(30,60,140,.3);display:flex;align-items:center;gap:20px;padding-left:32px;color:#0A1A44"),
("#0A1A40","#C3D1F2"),("#0C2150","#B2C4EE"),("#081633","#D4DFF7"),("#0F2B66","#9DB3E8"),("#FFD27A","#FFB347"),
("logo-mark-white.png","logo-mark-navy.png"),("color:#A9BBE8","color:#3B4768"),("color:#8FA6E6","color:#4F67B8"),
('id="cta" style="margin-top:110px;color:#fff','id="cta" style="margin-top:110px;color:#0A1A44'),
("drop-shadow(0 0 30px rgba(91,140,255,.7))","drop-shadow(0 8px 22px rgba(47,91,255,.25))"),
]
h0=T
for a,b in LIGHT:
    assert a in h0,a
    h0=h0.replace(a,b)
for name in sys.argv[1:]:
    n=int(name[1:]); ORDER=['K3','K6','K5','K7','K8','K9','K10','K11','K12','K13','K14','K15']
    r=random.Random(n*7+3); seq=BGS[:]; r.shuffle(seq)
    if name in ORDER: seq=[BGS[ORDER.index(name)%10]]
    bg=f'kbg_{seq[0]}.png'
    shutil.copy(f'{D}/../video2/bg/{seq[0]}.png',f'{D}/{bg}') if os.path.exists(f'{D}/../video2/bg/{seq[0]}.png') else None
    d=json.load(open(f'{D}/{name}.json'))
    src=json.load(open(f'{D}/{name}.json'))
    from reels import R
    for sc,sp in zip(d['scenes'],R[name]['scenes']):
        for k in ('vis','cnt','notm','key'):
            if k in sp: sc[k]=sp[k]
    h=h0.replace('/*TL*/',json.dumps(d)).replace('/*CFG*/',json.dumps(dict(bg=bg,tint='rgba(240,245,255,.84)')))
    open(f'{D}/{name}.html','w').write(h); print(name,bg)
