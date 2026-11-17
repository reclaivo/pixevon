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
R['R9']=dict(title='Documentaries',scenes=[
 dict(line='Some stories need more than a caption.',head='Some stories need *more* than a caption.',hs=88,phone=dict(ui='feed',mode='stop',ry0=.4,ry1=.1,**PC),pre=.08,post=.15),
 dict(line='We make short documentaries.',head='We make short *documentaries.*',hs=100,phone=dict(ui='player2',ry0=-.45,ry1=-.12,**PC)),
 dict(line='Researched. Scripted. Voiced. Edited.',head='Researched. Scripted. *Voiced.* Edited.',hs=88,phone=dict(ui='timeline',ry0=.45,ry1=.15,**PC)),
 dict(line='Contact us to learn more.',layout='end',pre=.3,post=1.2),
])

R['R10']=dict(title='New style demo',scenes=[
 dict(line='Still no video for your brand?',head='No video for your *brand?*',hs=92,shock=True,chips=[dict(t='NO REACH',x=210,y=750),dict(t='NO LEADS',x=540,y=750),dict(t='NO STORY',x=870,y=750)],b3d=dict(k='orbit',cfg=dict(title='Your brand',sub='Today',num=0,pct=0,cards=[['Views','0'],['Leads','0'],['Reach','0'],['Shares','0'],['Saves','0']],items=['No video yet','No story told','No new leads'])),pre=.08,post=.15),
 dict(line='Animation makes people stop.',head='Animation makes people *stop.*',hs=96,b3d=dict(k='bars',cfg=dict(pct=312))),
 dict(line='We turn your story into motion.',head='We turn your story into *motion.*',hs=84,b3d=dict(k='tiles',cfg={})),
 dict(line='Contact us to learn more.',layout='end',pre=.3,post=1.2),
])

R['R11']=dict(title='Social content done for you',scenes=[
 dict(line='Posting daily is exhausting.',head='Posting daily is *exhausting.*',hs=92,shock=True,chips=[dict(t='NO TIME',x=210,y=750),dict(t='NO IDEAS',x=540,y=750),dict(t='NO PLAN',x=870,y=750)],b3d=dict(k='orbit',cfg=dict(title='Your content',sub='This week',num=0,pct=0,cards=[['Posts','0'],['Reach','0'],['Saves','0'],['Leads','0'],['Shares','0']],items=['No time','No ideas','No plan'])),pre=.08,post=.15),
 dict(line='We make your content for you.',head='We make your *content* for you.',hs=88,b3d=dict(k='bars',cfg=dict(pct=240))),
 dict(line='Planned. Animated. Automated.',head='Planned. Animated. *Automated.*',hs=96,phone=dict(ui='calendar',ry0=-.45,ry1=-.12,**PC)),
 dict(line='Contact us to learn more.',layout='end',pre=.3,post=1.2),
])
R['R12']=dict(title='Documentary structure',scenes=[
 dict(line='Every documentary needs three things.',head='Every documentary needs *three* things.',hs=88,shock=True,chips=[dict(t='HOOK',x=210,y=750),dict(t='STORY',x=540,y=750),dict(t='PROOF',x=870,y=750)],b3d=dict(k='orbit',cfg=dict(title='Documentary',sub='Structure',num=3,pct=100,cards=[['Hook','1'],['Story','2'],['Proof','3'],['Voice','4'],['Edit','5']],items=['A strong hook','A real story','Clear proof'])),pre=.08,post=.15),
 dict(line='A hook. A story. And proof.',head='A hook. A story. And *proof.*',hs=96,phone=dict(ui='timeline',ry0=.45,ry1=.15,**PC)),
 dict(line='We make short documentaries.',head='We make short *documentaries.*',hs=92,b3d=dict(k='tiles',cfg={})),
 dict(line='Contact us to learn more.',layout='end',pre=.3,post=1.2),
])
R['R13']=dict(title='Captions on mute',scenes=[
 dict(line='Most people watch on mute.',head='Most people watch on *mute.*',hs=96,shock=True,chips=[dict(t='NO SOUND',x=210,y=750),dict(t='NO CAPTIONS',x=540,y=750),dict(t='NO REACH',x=870,y=750)],phone=dict(ui='feed',mode='stop',ry0=.4,ry1=.1,**PC),pre=.08,post=.15),
 dict(line='So add captions and motion.',head='So add captions and *motion.*',hs=92,b3d=dict(k='bars',cfg=dict(pct=180))),
 dict(line='We design videos that work without sound.',head='We design videos that work without *sound.*',hs=80,phone=dict(ui='player',ry0=-.45,ry1=-.12,**PC)),
 dict(line='Contact us to learn more.',layout='end',pre=.3,post=1.2),
])
R['R14']=dict(title='Storyboard first',scenes=[
 dict(line='Skip the storyboard and pay twice.',head='Skip the storyboard, pay *twice.*',hs=92,shock=True,chips=[dict(t='REWORK',x=210,y=750),dict(t='DELAYS',x=540,y=750),dict(t='WASTE',x=870,y=750)],phone=dict(ui='clutter',ry0=.4,ry1=.1,**PC),pre=.08,post=.15),
 dict(line='Plan every scene first.',head='Plan every *scene* first.',hs=96,b3d=dict(k='orbit',cfg=dict(title='Storyboard',sub='Plan',num=5,pct=100,cards=[['Scene 1','Hook'],['Scene 2','Story'],['Scene 3','Proof'],['Scene 4','Offer'],['Scene 5','Next step']],items=['Write the script','Sketch each scene','Approve the plan']))),
 dict(line='Then animation goes fast.',head='Then animation goes *fast.*',hs=100,phone=dict(ui='timeline',ry0=-.45,ry1=-.12,**PC)),
 dict(line='Contact us to learn more.',layout='end',pre=.3,post=1.2),
])
R['R15']=dict(title='Founder story documentary',scenes=[
 dict(line='Your story is your best content.',head='Your story is your best *content.*',hs=88,shock=True,chips=[dict(t='FOUNDERS',x=210,y=750),dict(t='BRANDS',x=540,y=750),dict(t='STORIES',x=870,y=750)],b3d=dict(k='tiles',cfg={}),pre=.08,post=.15),
 dict(line='We turn it into a short documentary.',head='We turn it into a short *documentary.*',hs=84,phone=dict(ui='player2',ry0=-.45,ry1=-.12,**PC)),
 dict(line='We handle every step.',head='We handle every *step.*',hs=100,b3d=dict(k='orbit',cfg=dict(title='Your film',sub='Progress',num=100,pct=100,cards=[['Research','Done'],['Script','Done'],['Voice','Done'],['Edit','Done'],['Export','Done']],items=['Research done','Script done','Edit done']))),
 dict(line='Contact us to learn more.',layout='end',pre=.3,post=1.2),
])

R['K1']=dict(title='Kinetic test',scenes=[
 dict(line='A founder opens your site at 1 AM.',key=['1','AM.'],pre=.05,post=.12),
 dict(line='Wall of text. Three seconds. Gone.',key=['Gone.'],cont=True,pre=.05,post=.12),
 dict(line='Now picture twenty seconds of motion.',key=['motion.'],cont=True,pre=.05,post=.12),
 dict(line='One clear idea. Understood instantly.',key=['instantly.'],cont=True,pre=.05,post=.12),
 dict(line='Contact us to learn more.',layout='end',pre=.3,post=1.2,cont=True),
])

R['K2']=dict(title='Kinetic test 2',scenes=[
 dict(line='Buyers decide in three seconds.',key=['three'],pre=.05,post=.12),
 dict(line='So show it in motion instead.',key=['motion'],cont=True,pre=.05,post=.12),
 dict(line='One idea per scene. Twenty seconds.',key=['Twenty'],cont=True,pre=.05,post=.12),
 dict(line='Clear. Memorable. Easy to share.',key=['share.'],cont=True,pre=.05,post=.12),
 dict(line='Contact us to learn more.',layout='end',pre=.3,post=1.2,cont=True),
])

R['K3']=dict(title='K3',scenes=[{'line': 'Three mistakes make animation look cheap.', 'key': ['cheap.'], 'vis': 'wall', 'pre': 0.05, 'post': 0.12, 'cont': False, 'notm': True}, {'line': 'Fix them with one idea per video.', 'key': ['idea'], 'vis': 'motion', 'pre': 0.05, 'post': 0.12, 'cont': True}, {'line': 'Large text. One clear next step.', 'key': ['step.'], 'vis': 'grid', 'pre': 0.05, 'post': 0.12, 'cont': True, 'cnt': [1, ' action']}, {'line': 'Contact us to learn more.', 'layout': 'end', 'pre': 0.3, 'post': 1.2, 'cont': True, 'vis': 'end'}])

R['K6']=dict(title='K6',scenes=[{'line': 'Long product pages lose buyers.', 'key': ['lose'], 'vis': 'wall', 'pre': 0.05, 'post': 0.12, 'cont': False, 'notm': True}, {'line': 'Show problem, solution, result.', 'key': ['result.'], 'vis': 'motion', 'pre': 0.05, 'post': 0.12, 'cont': True}, {'line': 'Explain it in thirty seconds.', 'key': ['thirty'], 'vis': 'grid', 'pre': 0.05, 'post': 0.12, 'cont': True, 'cnt': [30, 's']}, {'line': 'Contact us to learn more.', 'layout': 'end', 'pre': 0.3, 'post': 1.2, 'cont': True, 'vis': 'end'}])

R['K5']=dict(title='K5',scenes=[{'line': 'You have three seconds.', 'key': ['three'], 'vis': 'wall', 'pre': 0.05, 'post': 0.12, 'cont': False}, {'line': 'Bold first line. Movement from frame one.', 'key': ['movement'], 'vis': 'motion', 'pre': 0.05, 'post': 0.12, 'cont': True}, {'line': 'Three rules hold attention.', 'key': ['attention.'], 'vis': 'grid', 'pre': 0.05, 'post': 0.12, 'cont': True, 'cnt': [3, ' rules']}, {'line': 'Contact us to learn more.', 'layout': 'end', 'pre': 0.3, 'post': 1.2, 'cont': True, 'vis': 'end'}])

R['K7']=dict(title='K7',scenes=[{'line': 'Your logo is a still image.', 'key': ['still'], 'vis': 'motion', 'pre': 0.05, 'post': 0.12, 'cont': False}, {'line': 'Make it move for five seconds.', 'key': ['move'], 'vis': 'grid', 'pre': 0.05, 'post': 0.12, 'cont': True, 'cnt': [5, 's']}, {'line': 'Instant brand recognition.', 'key': ['recognition.'], 'vis': 'motion', 'pre': 0.05, 'post': 0.12, 'cont': True}, {'line': 'Contact us to learn more.', 'layout': 'end', 'pre': 0.3, 'post': 1.2, 'cont': True, 'vis': 'end'}])

R['K8']=dict(title='K8',scenes=[{'line': 'Static ads get scrolled past.', 'key': ['past.'], 'vis': 'wall', 'pre': 0.05, 'post': 0.12, 'cont': False, 'notm': True}, {'line': 'Motion stops the scroll.', 'key': ['scroll.'], 'vis': 'motion', 'pre': 0.05, 'post': 0.12, 'cont': True}, {'line': 'Lead with the benefit. One action.', 'key': ['action.'], 'vis': 'grid', 'pre': 0.05, 'post': 0.12, 'cont': True, 'cnt': [1, ' action']}, {'line': 'Contact us to learn more.', 'layout': 'end', 'pre': 0.3, 'post': 1.2, 'cont': True, 'vis': 'end'}])

R['K9']=dict(title='K9',scenes=[{'line': 'Some stories need more than a caption.', 'key': ['more'], 'vis': 'motion', 'pre': 0.05, 'post': 0.12, 'cont': False}, {'line': 'Hook. Story. Proof.', 'key': ['Proof.'], 'vis': 'grid', 'pre': 0.05, 'post': 0.12, 'cont': True, 'cnt': [3, ' parts']}, {'line': 'We make short documentaries.', 'key': ['documentaries.'], 'vis': 'motion', 'pre': 0.05, 'post': 0.12, 'cont': True}, {'line': 'Contact us to learn more.', 'layout': 'end', 'pre': 0.3, 'post': 1.2, 'cont': True, 'vis': 'end'}])

R['K10']=dict(title='K10',scenes=[{'line': 'No video for your brand?', 'key': ['video'], 'vis': 'wall', 'pre': 0.05, 'post': 0.12, 'cont': False, 'notm': True}, {'line': 'Animation makes people stop.', 'key': ['stop.'], 'vis': 'motion', 'pre': 0.05, 'post': 0.12, 'cont': True}, {'line': 'Your story in twenty seconds.', 'key': ['twenty'], 'vis': 'grid', 'pre': 0.05, 'post': 0.12, 'cont': True, 'cnt': [20, 's']}, {'line': 'Contact us to learn more.', 'layout': 'end', 'pre': 0.3, 'post': 1.2, 'cont': True, 'vis': 'end'}])

R['K11']=dict(title='K11',scenes=[{'line': 'Posting daily is exhausting.', 'key': ['exhausting.'], 'vis': 'wall', 'pre': 0.05, 'post': 0.12, 'cont': False, 'notm': True}, {'line': 'Plan the week once.', 'key': ['once.'], 'vis': 'grid', 'pre': 0.05, 'post': 0.12, 'cont': True, 'cnt': [7, ' days']}, {'line': 'We make it. Animated. Automated.', 'key': ['Automated.'], 'vis': 'motion', 'pre': 0.05, 'post': 0.12, 'cont': True}, {'line': 'Contact us to learn more.', 'layout': 'end', 'pre': 0.3, 'post': 1.2, 'cont': True, 'vis': 'end'}])

R['K12']=dict(title='K12',scenes=[{'line': 'Every documentary needs three things.', 'key': ['three'], 'vis': 'motion', 'pre': 0.05, 'post': 0.12, 'cont': False}, {'line': 'A hook. A story. And proof.', 'key': ['proof.'], 'vis': 'grid', 'pre': 0.05, 'post': 0.12, 'cont': True, 'cnt': [3, ' parts']}, {'line': 'We make short documentaries.', 'key': ['documentaries.'], 'vis': 'motion', 'pre': 0.05, 'post': 0.12, 'cont': True}, {'line': 'Contact us to learn more.', 'layout': 'end', 'pre': 0.3, 'post': 1.2, 'cont': True, 'vis': 'end'}])

R['K13']=dict(title='K13',scenes=[{'line': 'Most people watch on mute.', 'key': ['mute.'], 'vis': 'wall', 'pre': 0.05, 'post': 0.12, 'cont': False, 'notm': True}, {'line': 'Add captions. Add motion.', 'key': ['motion.'], 'vis': 'motion', 'pre': 0.05, 'post': 0.12, 'cont': True}, {'line': 'Videos that work without sound.', 'key': ['sound.'], 'vis': 'grid', 'pre': 0.05, 'post': 0.12, 'cont': True, 'cnt': [0, ' sound']}, {'line': 'Contact us to learn more.', 'layout': 'end', 'pre': 0.3, 'post': 1.2, 'cont': True, 'vis': 'end'}])

R['K14']=dict(title='K14',scenes=[{'line': 'Skip the storyboard, pay twice.', 'key': ['twice.'], 'vis': 'wall', 'pre': 0.05, 'post': 0.12, 'cont': False, 'notm': True}, {'line': 'Plan every scene first.', 'key': ['first.'], 'vis': 'grid', 'pre': 0.05, 'post': 0.12, 'cont': True, 'cnt': [5, ' scenes']}, {'line': 'Then animation goes fast.', 'key': ['fast.'], 'vis': 'motion', 'pre': 0.05, 'post': 0.12, 'cont': True}, {'line': 'Contact us to learn more.', 'layout': 'end', 'pre': 0.3, 'post': 1.2, 'cont': True, 'vis': 'end'}])

R['K15']=dict(title='K15',scenes=[{'line': 'Your story is your best content.', 'key': ['content.'], 'vis': 'motion', 'pre': 0.05, 'post': 0.12, 'cont': False}, {'line': 'Research. Script. Edit.', 'key': ['Edit.'], 'vis': 'grid', 'pre': 0.05, 'post': 0.12, 'cont': True, 'cnt': [3, ' steps']}, {'line': 'We handle every step.', 'key': ['step.'], 'vis': 'motion', 'pre': 0.05, 'post': 0.12, 'cont': True}, {'line': 'Contact us to learn more.', 'layout': 'end', 'pre': 0.3, 'post': 1.2, 'cont': True, 'vis': 'end'}])
