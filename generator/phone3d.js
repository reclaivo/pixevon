(function(){
const P={};
P.init=function(canvas,W,H){
 const r=new THREE.WebGLRenderer({canvas,antialias:true,alpha:true,preserveDrawingBuffer:true});
 r.setSize(W,H,false);r.setPixelRatio(1);r.toneMapping=THREE.ACESFilmicToneMapping;r.toneMappingExposure=1.0;r.shadowMap.enabled=true;r.shadowMap.type=THREE.PCFSoftShadowMap;r.outputColorSpace=THREE.SRGBColorSpace;
 const sc=new THREE.Scene();
 // studio environment for reflections
 const env=new THREE.Scene();
 env.add(new THREE.Mesh(new THREE.BoxGeometry(30,30,30),new THREE.MeshBasicMaterial({color:new THREE.Color(.10,.12,.18),side:THREE.BackSide})));
 function panel(w,h,x,y,z,rx,ry,col){const m=new THREE.Mesh(new THREE.PlaneGeometry(w,h),new THREE.MeshBasicMaterial({color:new THREE.Color(col[0],col[1],col[2]),side:THREE.DoubleSide}));m.position.set(x,y,z);m.rotation.set(rx,ry,0);env.add(m);}
 panel(16,6,0,12,2,Math.PI/2,0,[10,10,10]);panel(5,5,-6,4,9,0,0.5,[6,6.5,8]);
 panel(3,16,-11,1,3,0,Math.PI/2,[7,7.5,9]);
 panel(3,16,11,1,-2,0,Math.PI/2,[3.5,5,9]);
 panel(10,3,0,-6,8,-0.5,0,[2.5,2.8,3.5]);
 panel(6,6,2,3,13,0,0,[3,3,3.4]);
 const pm=new THREE.PMREMGenerator(r);sc.environment=pm.fromScene(env,0.02).texture;
 const cam=new THREE.PerspectiveCamera(28,W/H,.1,100);cam.position.set(0,0,10);
 const cv=document.createElement('canvas');cv.width=780;cv.height=1690;const g=cv.getContext('2d');
 const tex=new THREE.CanvasTexture(cv);tex.colorSpace=THREE.SRGBColorSpace;tex.anisotropy=8;
 const pw=1.42,ph=3.04,pr=.26,pd=.16;
 function rr(w,h,rad){const s=new THREE.Shape();const x0=-w/2,y0=-h/2;s.moveTo(x0+rad,y0);s.lineTo(x0+w-rad,y0);s.quadraticCurveTo(x0+w,y0,x0+w,y0+rad);s.lineTo(x0+w,y0+h-rad);s.quadraticCurveTo(x0+w,y0+h,x0+w-rad,y0+h);s.lineTo(x0+rad,y0+h);s.quadraticCurveTo(x0,y0+h,x0,y0+h-rad);s.lineTo(x0,y0+rad);s.quadraticCurveTo(x0,y0,x0+rad,y0);return s;}
 const frame=new THREE.MeshPhysicalMaterial({color:0xD5DCEC,metalness:1,roughness:.16,clearcoat:.5,clearcoatRoughness:.12,envMapIntensity:2.4});
 const phone=new THREE.Group();
 const body=new THREE.Mesh(new THREE.ExtrudeGeometry(rr(pw,ph,pr),{depth:pd,bevelEnabled:true,bevelThickness:.03,bevelSize:.03,bevelSegments:8,curveSegments:40}),frame);body.castShadow=true;body.position.z=-pd/2;phone.add(body);
 // black glass front plate
 const plate=new THREE.Mesh(new THREE.ShapeGeometry(rr(pw-.07,ph-.07,pr-.03),40),new THREE.MeshPhysicalMaterial({color:0x020308,metalness:0,roughness:.3,clearcoat:1,clearcoatRoughness:.04,envMapIntensity:.35}));plate.position.z=pd/2+.032;phone.add(plate);
 // rounded screen via alpha
 const sw=pw-.17,shh=ph-.17;
 const scrM=new THREE.MeshBasicMaterial({map:tex,toneMapped:false,transparent:true});
 const scr=new THREE.Mesh(new THREE.PlaneGeometry(sw,shh),scrM);scr.position.z=pd/2+.034;phone.add(scr);
 // glass reflection layer
 const glass=new THREE.Mesh(new THREE.PlaneGeometry(pw-.07,ph-.07),new THREE.MeshPhysicalMaterial({color:0xffffff,roughness:.02,transparent:true,opacity:.09,clearcoat:1,clearcoatRoughness:.01,envMapIntensity:2.6}));glass.position.z=pd/2+.036;phone.add(glass);
 const isl=new THREE.Mesh(new THREE.CapsuleGeometry(.065,.34,8,24),new THREE.MeshStandardMaterial({color:0x020307,roughness:.35}));isl.rotation.z=Math.PI/2;isl.position.set(0,ph/2-.16,pd/2+.04);phone.add(isl);
 [[.55,.2,1],[.2,.32,-1],[-.2,.32,-1]].forEach(b=>{const m=new THREE.Mesh(new THREE.BoxGeometry(.04,b[1],.07),frame);m.position.set(b[2]*(pw/2+.02),b[0],0);phone.add(m);});
 const pivot=new THREE.Group();pivot.add(phone);sc.add(pivot);
 const key=new THREE.DirectionalLight(0xffffff,1.4);key.position.set(-.8,9,3.5);key.castShadow=true;key.shadow.mapSize.set(2048,2048);key.shadow.radius=16;key.shadow.camera.left=-5;key.shadow.camera.right=5;key.shadow.camera.top=5;key.shadow.camera.bottom=-5;key.shadow.bias=-.0003;sc.add(key);
 const floor=new THREE.Mesh(new THREE.PlaneGeometry(40,40),new THREE.ShadowMaterial({opacity:.14}));floor.rotation.x=-Math.PI/2;floor.position.y=-2.05;floor.receiveShadow=true;sc.add(floor);
 const api={ui:null};
 api.render=function(o){
  o=o||{};
  g.clearRect(0,0,780,1690);
  g.save();g.beginPath();g.roundRect(0,0,780,1690,118);g.clip();
  if(api.ui)api.ui(g,780,1690,o.t||0,o);
  g.restore();tex.needsUpdate=true;
  pivot.rotation.set(o.rx||0,o.ry||0,o.rz||0);pivot.position.set(o.px||0,o.py||0,o.pz||0);pivot.scale.setScalar(o.s||1);
  floor.position.y=-2.05+(o.floorOff||0);
  cam.position.set(o.cx||0,o.cy||0,o.cz||10);cam.lookAt(o.lx||0,o.ly||0,0);
  r.render(sc,cam);
 };
 return api;
};
window.P3D=P;
})();
