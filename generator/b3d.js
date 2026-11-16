(function(){
window.B3D={make:function(canvas,S,cfg){cfg=cfg||{};const W=canvas.width,H=canvas.height,NAVY=0x0b1f4b,BLUE=0x2f6bff;
const r=new THREE.WebGLRenderer({canvas,antialias:true,alpha:true,preserveDrawingBuffer:true});
r.setSize(W,H,false);r.setPixelRatio(1);r.setClearColor(0,0);r.shadowMap.enabled=true;r.shadowMap.type=THREE.PCFSoftShadowMap;
const sc=new THREE.Scene();const cam=new THREE.PerspectiveCamera(30,W/H,.1,100);
sc.add(new THREE.HemisphereLight(0xffffff,0x9fb4dc,1.05));
const dl=new THREE.DirectionalLight(0xffffff,1.35);dl.position.set((S=='B'||S=='bars')?2:4,(S=='B'||S=='bars')?12:8,(S=='B'||S=='bars')?5:7);dl.castShadow=true;dl.shadow.mapSize.set(1024,1024);
Object.assign(dl.shadow.camera,{left:-8,right:8,top:8,bottom:-8,near:1,far:30});dl.shadow.bias=-.0004;sc.add(dl);
const fl=new THREE.DirectionalLight(0x9db8ff,.5);fl.position.set(-6,2,4);sc.add(fl);
const ez=x=>1-Math.pow(1-Math.min(1,Math.max(0,x)),3);
const eb=x=>{x=Math.min(1,Math.max(0,x));const c=1.70158,c3=c+1;return 1+c3*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
function rr(w,h,rad){const s=new THREE.Shape(),x=-w/2,y=-h/2;s.moveTo(x+rad,y);s.lineTo(x+w-rad,y);s.absarc(x+w-rad,y+rad,rad,-Math.PI/2,0);s.lineTo(x+w,y+h-rad);s.absarc(x+w-rad,y+h-rad,rad,0,Math.PI/2);s.lineTo(x+rad,y+h);s.absarc(x+rad,y+h-rad,rad,Math.PI/2,Math.PI);s.lineTo(x,y+rad);s.absarc(x+rad,y+rad,rad,Math.PI,1.5*Math.PI);return s}
function slab(w,h,d,rad,col,rough=.35,metal=.25){const g=new THREE.ExtrudeGeometry(rr(w,h,rad),{depth:d,bevelEnabled:true,bevelSize:.03,bevelThickness:.03,bevelSegments:4,curveSegments:14});g.translate(0,0,-d/2);
 const m=new THREE.Mesh(g,new THREE.MeshStandardMaterial({color:col,roughness:rough,metalness:metal}));m.castShadow=true;m.receiveShadow=true;return m}
function rrect(g,x,y,w,h,rad){g.beginPath();g.moveTo(x+rad,y);g.arcTo(x+w,y,x+w,y+h,rad);g.arcTo(x+w,y+h,x,y+h,rad);g.arcTo(x,y+h,x,y,rad);g.arcTo(x,y,x+w,y,rad);g.closePath()}
function cvTex(w,h){const c=document.createElement('canvas');c.width=w;c.height=h;const t=new THREE.CanvasTexture(c);t.colorSpace=THREE.SRGBColorSpace;t.anisotropy=8;return {c,g:c.getContext('2d'),t}}
function facePlane(w,h,tex,z){const m=new THREE.Mesh(new THREE.PlaneGeometry(w,h),new THREE.MeshBasicMaterial({map:tex,transparent:true,toneMapped:false}));m.position.z=z;return m}
let update=()=>{},READY=false;
function sceneA(){
 const grp=new THREE.Group();sc.add(grp);
 const ph=slab(1.5,3.1,.2,.28,NAVY,.3,.4);grp.add(ph);
 const scr=cvTex(780,1620);grp.add(facePlane(1.36,2.82,scr.t,.135));
 function drawScr(t){const g=scr.g;g.clearRect(0,0,780,1620);g.fillStyle='#f6f9ff';rrect(g,0,0,780,1620,70);g.fill();
  g.fillStyle='#0b1f4b';g.font='800 54px Helvetica';g.fillText(cfg.title||'Growth',60,140);g.fillStyle='#7d8fb5';g.font='600 32px Helvetica';g.fillText(cfg.sub||'Last 7 days',60,190);
  const v=Math.round((cfg.num===undefined?48200:cfg.num)*ez(t/2.4));g.fillStyle='#0b1f4b';g.font='900 110px Helvetica';g.fillText(v.toLocaleString(),60,340);
  g.fillStyle='#2f6bff';g.font='800 40px Helvetica';g.fillText('+'+Math.round((cfg.pct===undefined?312:cfg.pct)*ez(t/2.4))+'%',60,405);
  const hs=[.35,.5,.42,.7,.58,.88,1];for(let i=0;i<7;i++){const k=ez((t-.3-i*.12)/.7),bh=520*hs[i]*k,x=60+i*95;g.fillStyle=i==6?'#2f6bff':'#c9d6f2';rrect(g,x,1000-bh,62,Math.max(bh,2),18);g.fill()}
  g.strokeStyle='#0b1f4b';g.lineWidth=7;g.beginPath();const n=Math.floor(cl((t-.8)/1.6)*7);for(let i=0;i<=n;i++){const x=91+i*95,y=1000-520*hs[i]*.95-40;i?g.lineTo(x,y):g.moveTo(x,y)}g.stroke();
  for(let i=0;i<3;i++){g.fillStyle='#e8effc';rrect(g,60,1100+i*140,660,110,30);g.fill();g.fillStyle=i==0?'#2f6bff':'#0b1f4b';g.beginPath();g.arc(120,1155+i*140,28,0,7);g.fill();g.fillStyle='#0b1f4b';g.font='700 34px Helvetica';g.fillText((cfg.items||['New reel published','Audience up','Followers goal'])[i],180,1167+i*140)}
  scr.t.needsUpdate=true}
 const cards=[];const defs=(cfg.cards||[['Views','1.2M'],['Saved','48K'],['Watch time','92%'],['Shares','9.6K'],['Reach','310K']]).map((d,i)=>[d[0],d[1],i%2?'#0b1f4b':'#2f6bff']);
 defs.forEach((d,i)=>{const cv=cvTex(512,320);const g=cv.g;g.fillStyle='rgba(255,255,255,.96)';rrect(g,0,0,512,320,50);g.fill();g.fillStyle='#7d8fb5';g.font='600 40px Helvetica';g.fillText(d[0],44,100);g.fillStyle=d[2];g.font='900 110px Helvetica';g.fillText(d[1],44,230);cv.t.needsUpdate=true;
  const m=slab(1.5,.94,.08,.2,0xffffff,.4,.05);m.material.emissive=new THREE.Color(0xdfe6f5);m.material.emissiveIntensity=.7;const f=facePlane(1.44,.9,cv.t,.092);const gg=new THREE.Group();gg.add(m,f);grp.add(gg);cards.push({gg,a0:i/defs.length*Math.PI*2,y:[.9,-.6,1.5,-1.3,.2][i],R:[1.8,1.95,1.7,1.9,2.0][i]})});
 const pts=new THREE.Points((()=>{const g=new THREE.BufferGeometry(),a=[];for(let i=0;i<120;i++)a.push((Math.random()-.5)*10,(Math.random()-.5)*12,(Math.random()-.5)*5-1);g.setAttribute('position',new THREE.Float32BufferAttribute(a,3));return g})(),new THREE.PointsMaterial({color:0x2f6bff,size:.06,transparent:true,opacity:.55}));sc.add(pts);
 update=t=>{drawScr(t);const o=Math.sin(t*.9)*.45;grp.rotation.y=o*.6;grp.rotation.x=Math.sin(t*.7)*.05;grp.position.y=Math.sin(t*1.3)*.08;
  cards.forEach(c=>{const a=c.a0+t*.8,x=Math.cos(a)*c.R,z=Math.sin(a)*1.7;c.gg.position.set(x,c.y+Math.sin(t*1.6+c.a0)*.12,z);c.gg.rotation.y=-Math.cos(a)*.5;c.gg.scale.setScalar(.62+.16*(z+1.7)/3.4)});
  pts.position.y=-t*.12%1;pts.rotation.y=t*.05;
  cam.position.set(Math.sin(t*.5)*1.2,.4,14-ez(t/3.5)*2.2);cam.lookAt(0,0,0)};
 READY=true}
// ---------- Scene B: 3D bar growth ----------
function sceneB(){
 const floor=new THREE.Mesh(new THREE.PlaneGeometry(40,40),new THREE.ShadowMaterial({opacity:.22}));floor.rotation.x=-Math.PI/2;floor.position.y=-1.6;floor.receiveShadow=true;sc.add(floor);
 const hs=cfg.heights||[1.3,2.1,1.7,2.9,4.1],bars=[];const grp=new THREE.Group();sc.add(grp);
 hs.forEach((h,i)=>{const col=new THREE.Color().lerpColors(new THREE.Color(0x9db8f2),new THREE.Color(i==4?0x2f6bff:0x0b1f4b),i/4);
  const m=new THREE.Mesh(new THREE.BoxGeometry(.78,1,.78),new THREE.MeshStandardMaterial({color:i==4?0x2f6bff:col,roughness:.3,metalness:.2}));m.castShadow=true;m.receiveShadow=true;m.position.x=(i-2)*1.15;grp.add(m);bars.push({m,h,i})});
 const lab=cvTex(512,256);const sp=new THREE.Sprite(new THREE.SpriteMaterial({map:lab.t,transparent:true,toneMapped:false}));sp.scale.set(2.4,1.2,1);grp.add(sp);
 const ln=[];const lineMat=new THREE.LineBasicMaterial({color:0x0b1f4b});
 update=t=>{bars.forEach(b=>{const k=Math.max(.001,eb((t-.25-b.i*.22)/.9));const h=b.h*k;b.m.scale.y=h;b.m.position.y=-1.6+h/2});
  const top=bars[4],ht=top.h*Math.max(.001,eb((t-.25-4*.22)/.9));sp.position.set(top.m.position.x-.9,-1.6+ht+.85,0);
  const g=lab.g;g.clearRect(0,0,512,256);g.fillStyle='#fff';rrect(g,16,40,480,170,45);g.fill();g.fillStyle='#2f6bff';g.font='900 100px Helvetica';g.textAlign='center';g.fillText((cfg.prefix===undefined?'+':cfg.prefix)+Math.round((cfg.pct||312)*ez((t-1.1)/1.8))+(cfg.suffix===undefined?'%':cfg.suffix),256,155);g.textAlign='left';lab.t.needsUpdate=true;sp.material.opacity=ez((t-1)/.4);
  const a=-.5+t*.32;cam.position.set(Math.sin(a)*20,2.6+Math.sin(t*.8)*.3,Math.cos(a)*20);cam.lookAt(0,.3,0);grp.position.y=0}
 READY=true}
// ---------- Scene C: tiles build the logo ----------
function sceneC(){
 const N=6,s=.72,img=new Image();img.onload=()=>{
  const cv=cvTex(1024,1024),g=cv.g;g.fillStyle='#ffffff';rrect(g,0,0,1024,1024,0);g.fill();const k=620/Math.max(img.width,img.height);g.drawImage(img,512-img.width*k/2,512-img.height*k/2,img.width*k,img.height*k);cv.t.needsUpdate=true;
  const side=new THREE.MeshStandardMaterial({color:NAVY,roughness:.35,metalness:.3}),front=new THREE.MeshBasicMaterial({map:cv.t,toneMapped:false});
  const grp=new THREE.Group();sc.add(grp);const tiles=[];
  for(let iy=0;iy<N;iy++)for(let ix=0;ix<N;ix++){const geo=new THREE.BoxGeometry(s*.97,s*.97,.34);const uv=geo.attributes.uv;for(let v=16;v<20;v++){uv.setXY(v,(ix+uv.getX(v))/N,(N-1-iy+uv.getY(v))/N)}uv.needsUpdate=true;
   const m=new THREE.Mesh(geo,[side,side,side,side,front,side]);m.castShadow=true;m.receiveShadow=true;
   const tx=(ix-(N-1)/2)*s,ty=((N-1)/2-iy)*s;const d=Math.random;const from=new THREE.Vector3((d()-.5)*14,(d()-.5)*18,d()*3),rot=new THREE.Vector3((d()-.5)*9,(d()-.5)*9,(d()-.5)*9);
   tiles.push({m,to:new THREE.Vector3(tx,ty,0),from,rot,delay:(ix+iy)*.05+d()*.35});grp.add(m)}
  const brand=document.getElementById('brand');
  update=t=>{tiles.forEach(o=>{const k=ez((t-.1-o.delay)/1.5);o.m.position.lerpVectors(o.from,o.to,k);o.m.rotation.set(o.rot.x*(1-k),o.rot.y*(1-k),o.rot.z*(1-k))});
   const pull=ez((t-2.4)/1.4);grp.rotation.y=Math.sin(t*1.1)*.18*(1-pull*.5);grp.rotation.x=-.06+Math.sin(t*.9)*.05;
   cam.position.set(0,.2,15.5+pull*3);cam.lookAt(0,-.2,0);0};
  READY=true};img.src=(cfg.logo||'logo-mark-navy.png')}

({orbit:sceneA,A:sceneA,bars:sceneB,B:sceneB,tiles:sceneC,C:sceneC})[S]();
return {ready:()=>READY,setT:t=>{update(t);r.render(sc,cam)}};}};})();
