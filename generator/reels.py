PC=dict(x=540,y=1175,s=.78)
R={}
R['R1']=dict(title='Brief checklist',scenes=[
 dict(line='Stop!',head='STOP.',hs=300,extra='rings',bg='shapes.png',blur=0,sp=.95,pre=.12,post=.45),
 dict(line='Your animation will flop if your brief skips this.',head='Your animation will *flop* if your brief skips this.',hs=92,phone=dict(ui='flop',ry0=-.4,ry1=.0,**PC),bg='shapes.png',blur=0,pre=0,post=.15,cont=True),
 dict(line='One. A single message.',head='A single message.',k='1 of 3',hs=100,phone=dict(ui='brief',ry0=-.45,ry1=-.12,tk=[1.2,99,99],**PC),bg='office.png',blur=8),
 dict(line='Two. A specific audience.',head='A specific audience.',k='2 of 3',hs=100,phone=dict(ui='audience',ry0=.4,ry1=.1,**PC),bg='desklight.png',blur=7),
 dict(line='Three. A clear next step.',head='A clear next step.',k='3 of 3',hs=100,phone=dict(ui='brief',ry0=.45,ry1=.12,tk=[-1,-1,.9],btn=1.5,**PC),bg='office.png',blur=12),
 dict(line='Contact us to learn more.',layout='end',bg='bg1.png',blur=0,pre=.3,post=1.2),
])
R['R2']=dict(title='Pulso promo',scenes=[
 dict(line='Everyone is using AI to make animated reels.',head='Everyone is using *AI* to make animated reels.',hs=92,phone=dict(ui='analytics',ry0=-.45,ry1=-.1,**PC),bg='camera.png',blur=4,pre=.08,post=.15),
 dict(line='Then they lock the method behind a course.',head='Then they *lock* the method behind a course.',hs=92,extra='lock',bg='deskdark.png',blur=8),
 dict(line='What if you skipped the course?',head='What if you *skipped* the course?',hs=100,extra='unlock',bg='office.png',blur=9),
 dict(line='Meet Pulso.',head='Meet *Pulso.*',hs=150,extra='pulsobig',bg='bg2.png',blur=0,sfx=[('shimmer',.1)]),
 dict(line='We create your content and post it.',head='We create your content and post it.',hs=80,extra='pulsosmall',phone=dict(ui='calendar',x=720,y=1175,s=.78,ry0=-.5,ry1=-.25),bg='desklight.png',blur=7),
 dict(line='Contact us to learn more.',layout='end',bg='bg1.png',blur=0,pre=.3,post=1.2),
])
R['R3']=dict(title='Three mistakes',scenes=[
 dict(line='Three mistakes make your animation look cheap.',head='Three mistakes make your animation look *cheap.*',hs=88,extra='mistakes',bg='shapes.png',blur=0,pre=.08,post=.15),
 dict(line='One. Too many ideas.',head='Too many ideas.',k='Mistake 1',num='1',hs=100,phone=dict(ui='clutter',x=540,y=1175,s=.78,ry0=.45,ry1=.15),bg='office.png',blur=8),
 dict(line='Two. Text nobody can read.',head='Text nobody can read.',k='Mistake 2',hs=92,phone=dict(ui='tiny',x=540,y=1175,s=.78,ry0=-.55,ry1=-.3),bg='desklight.png',blur=7),
 dict(line='Three. No next step.',head='No next step.',k='Mistake 3',num='3',hs=100,phone=dict(ui='dead',x=540,y=1175,s=.78,ry0=.45,ry1=.15),bg='office.png',blur=12),
 dict(line='Contact us to learn more.',layout='end',bg='bg1.png',blur=0,pre=.3,post=1.2),
])
PL=dict(x=340,y=1175,s=.78)
R['R4']=dict(title='Pulso daily',scenes=[
 dict(line='Posting every day is the hard part.',head='Posting every day is the *hard* part.',hs=84,phone=dict(ui='streak',ry0=.45,ry1=.15,**PC),pre=.08,post=.15),
 dict(line='Ideas. Scripts. Animation. Editing.',head='Ideas. Scripts. Animation. Editing.',hs=78,xc=dict(n='pipeline',x=540,y=1160,sc=.95)),
 dict(line='Pulso handles all of it.',head='*Pulso* handles all of it.',hs=110,extra='pulsobig',sfx=[('shimmer',.1)]),
 dict(line='Then it posts for you.',head='Then it *posts* for you.',hs=96,extra='pulsosmall',phone=dict(ui='calendar',x=720,y=1175,s=.78,ry0=-.5,ry1=-.25)),
 dict(line='Contact us to learn more.',layout='end',pre=.3,post=1.2),
])
R['R5']=dict(title='Three seconds',scenes=[
 dict(line='You have three seconds.',head='You have *three* seconds.',hs=104,xc=dict(n='countdown',x=540,y=1120,sc=.9),pre=.08,post=.15),
 dict(line='One. A bold first line.',head='A bold first line.',k='1 of 3',hs=100,phone=dict(ui='hookline',ry0=-.45,ry1=-.12,**PC)),
 dict(line='Two. Movement from frame one.',head='Movement from frame one.',k='2 of 3',hs=92,phone=dict(ui='motion',ry0=.4,ry1=.1,**PC)),
 dict(line='Three. A reason to stay.',head='A reason to stay.',k='3 of 3',hs=100,phone=dict(ui='retention',ry0=-.4,ry1=-.1,**PC)),
 dict(line='Contact us to learn more.',layout='end',pre=.3,post=1.2),
])
R['R6']=dict(title='Explainer videos',scenes=[
 dict(line='Nobody reads long product pages.',head='Nobody reads long *product pages.*',hs=92,phone=dict(ui='wall',ry0=-.4,ry1=-.1,**PC),pre=.08,post=.15),
 dict(line='They watch a thirty second video.',head='They watch a *thirty second* video.',hs=88,phone=dict(ui='player',ry0=.4,ry1=.1,**PC)),
 dict(line='Problem. Solution. Result.',head='Problem. Solution. Result.',hs=88,xc=dict(n='flow3',x=540,y=1150,sc=.95)),
 dict(line='Contact us to learn more.',layout='end',pre=.3,post=1.2),
])
R['R7']=dict(title='Logo animation',scenes=[
 dict(line='Your logo is a still image.',head='Your *logo* is a still image.',hs=88,xc=dict(n='logostill',x=540,y=1150,sc=.95),pre=.08,post=.15),
 dict(line='Make it move.',head='Make it *move.*',hs=120,xc=dict(n='logoanim',x=540,y=1150,sc=.95)),
 dict(line='A five second intro. Every video.',head='A five second intro. Every video.',hs=80,phone=dict(ui='timeline',ry0=.45,ry1=.15,**PC)),
 dict(line='Contact us to learn more.',layout='end',pre=.3,post=1.2),
])
R['R8']=dict(title='Motion ads',scenes=[
 dict(line='Static ads get scrolled past.',head='Static ads get *scrolled past.*',hs=92,phone=dict(ui='feed',mode='fast',ry0=-.4,ry1=-.1,**PC),pre=.08,post=.15),
 dict(line='Motion stops the scroll.',head='Motion *stops* the scroll.',hs=100,phone=dict(ui='feed',mode='stop',ry0=.4,ry1=.1,**PC)),
 dict(line='We make your ads move.',head='We make your ads *move.*',hs=100,xc=dict(n='adcard',x=540,y=1140,sc=.95)),
 dict(line='Contact us to learn more.',layout='end',pre=.3,post=1.2),
])
R['R9']=dict(title='Pulso never skips',scenes=[
 dict(line='Your competitors posted today.',head='Your competitors *posted* today.',hs=88,xc=dict(n='rivals',x=540,y=1150,sc=.95),pre=.08,post=.15),
 dict(line='Did you?',head='Did *you?*',hs=230,xc=dict(n='qmark',x=540,y=1190,sc=.9)),
 dict(line='Pulso never skips a day.',head='*Pulso* never skips a day.',hs=100,extra='pulsobig',sfx=[('shimmer',.1)]),
 dict(line='Contact us to learn more.',layout='end',pre=.3,post=1.2),
])
