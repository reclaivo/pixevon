# Dark theme (black base, navy highlights, white logo) for the reel templates. Default theme since 18 Nov 2026.
import os
D=os.path.dirname(os.path.abspath(__file__))
DARK_TINT='rgba(0,0,0,.95)'
ROOT_BG='radial-gradient(900px 700px at 50% 36%,#030408 0%,#010102 55%,#000 100%)'
def bgfile(name):
    for p in (f'{D}/bg/{name}.png',f'{D}/../video2/bg/{name}.png'):
        if os.path.exists(p): return p
    raise SystemExit('background not found: '+name)
KIN_DARK=[
("#030816;font-family","#010204;font-family"),
("radial-gradient(900px 700px at 50% 38%,#0E2150 0%,#071230 45%,#030816 100%)",ROOT_BG),
(".tag{position:absolute;left:0;width:1080px;top:230px",".tag{position:absolute;left:0;width:1080px;top:260px"),
("#FF4D5E","#5B8CFF"),("#FF2A44","#2F5BFF"),("rgba(255,60,90,","rgba(70,110,255,"),
("#4DFFA6","#9DB6FF"),("#FFD27A","#9DB6FF"),
]
GW_DARK=[
("background:#EAF0FF;font-family","background:#020306;font-family"),
("overflow:hidden;background:#EAF0FF}","overflow:hidden;background:"+ROOT_BG+"}"),
("rgba(20,40,100,.28) 100%","rgba(0,0,0,.62) 100%"),
(".flash{position:absolute;inset:0;background:#fff",".flash{position:absolute;inset:0;background:#5B8CFF"),
("color:#0A1A44;font-size:34px;font-weight:700;letter-spacing:.5px;opacity:.9","color:#fff;font-size:34px;font-weight:700;letter-spacing:.5px;opacity:.9"),
("logo-mark-navy.png","logo-mark-white.png"),
("line-height:1.08;color:#0A1A44;","line-height:1.08;color:#fff;"),
("text-shadow:0 4px 18px rgba(255,255,255,.95)","text-shadow:0 6px 24px rgba(0,0,0,.85)"),
("text-shadow:0 0 16px rgba(255,255,255,.95),0 0 4px rgba(255,255,255,.9)","text-shadow:0 0 18px var(--ac),0 0 44px var(--ac)"),
("border:2px solid rgba(255,255,255,.9);-webkit-backdrop-filter","border:2px solid rgba(120,150,255,.6);-webkit-backdrop-filter"),
("rgba(255,255,255,.75),rgba(255,255,255,0)","rgba(160,190,255,.40),rgba(160,190,255,0)"),
("drop-shadow(0 6px 8px rgba(10,26,68,.35))","drop-shadow(0 6px 10px rgba(0,0,0,.5))"),
("background:rgba(255,255,255,.92);border:2px solid #C9D6F5;font-size:30px;font-weight:800;color:#0A1A44;box-shadow:0 10px 22px -10px rgba(30,60,140,.45)","background:rgba(8,11,26,.94);border:2px solid #3A56B8;font-size:30px;font-weight:800;color:#fff;box-shadow:0 10px 22px -10px #000"),
("background:#fff;border:2px solid #C9D6F5;box-shadow:0 40px 80px -30px rgba(30,60,140,.5);overflow:hidden","background:#07090F;border:2px solid #2B3F8F;box-shadow:0 40px 80px -30px #000,0 0 70px rgba(47,91,255,.22);overflow:hidden"),
("background:#F2F6FF;border-bottom:2px solid #E1E9FA","background:#0B0E1C;border-bottom:2px solid #161F4A"),
("background:#C7D2EE","background:#34468C"),("font-size:26px;color:#4F67B8","font-size:26px;color:#9DB6FF"),
("linear-gradient(150deg,#EAF1FF,#C9D9FA)","linear-gradient(150deg,#10173A,#0B0E1C)"),
("color:#0A1A44","color:#EAF1FF"),("color:#4F67B8","color:#9DB6FF"),("#3B4768","#A9BBE8"),
("background:#fff","background:#0D1226"),("#C9D6F5","#2B3F8F"),("#F7FAFF","#0D1226"),("#EAF0FF","#0B0E1C"),
("#DCE6FA","#10173A"),("#C9D9FA","#131C45"),("#A9BDEB","#2A3F8C"),("#B7C8F0","#22357A"),("#9FB4E6","#34468C"),("#E1E9FA","#161F4A"),("#F2F6FF","#0B0E1C"),
]
DARKEN=[('#2F5BFF','#1C3A9E'),('#5B8CFF','#2748B8'),('#9DB6FF','#5F7BCB'),('#7FA8FF','#4666C4'),('#3B64F0','#1F3FA8'),('#2F54D6','#1B3590'),('#1738B8','#10276E'),('rgba(70,110,255,','rgba(40,75,200,'),('rgba(47,91,255,','rgba(28,58,158,'),('#EAF1FF','#E6ECFA'),('--ac:#1C3A9E','--ac:#4B6FE0')]
def apply(h,pairs):
    for a,b in pairs:
        if a not in h: print('  theme: not found:',a[:70])
        h=h.replace(a,b)
    for a,b in DARKEN: h=h.replace(a,b)
    return h.replace('</style>','.tag span{text-transform:uppercase;font-weight:800!important;letter-spacing:.16em}.tag{font-weight:800!important}</style>',1)
def safe(h,els_line,scale=.92):
    """wrap all scenes in a container scaled toward the centre: more empty space at top and bottom"""
    w="const safe=document.createElement('div');safe.style.cssText='position:absolute;inset:0;transform:scale(%s);transform-origin:540px 960px';root.appendChild(safe);"%scale
    assert els_line in h and "root.appendChild(d);return d}" in h
    return h.replace(els_line,w+els_line).replace("root.appendChild(d);return d}","safe.appendChild(d);return d}")
