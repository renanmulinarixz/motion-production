#!/usr/bin/env node
// For trusted, self-contained Canvas templates only. DOM/SVG/CSS are not rendered.
const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const {spawn,execFileSync}=require('node:child_process');
const {once}=require('node:events');
let canvasAPI;
try {canvasAPI=require('@napi-rs/canvas');}
catch(e){canvasAPI=require(path.join(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES||'', '@napi-rs/canvas'));}
async function main(){
 const [input,output,fpsArg='30']=process.argv.slice(2),fps=Number(fpsArg);
 if(!input||!output||!Number.isFinite(fps)||fps<1||fps>120)throw Error('Usage: node render_canvas.cjs trusted.html output.mp4 [fps]');
 if(fs.existsSync(output))throw Error('Output exists.');
 const html=fs.readFileSync(input,'utf8');
 if(/<script[^>]+src\s*=/i.test(html))throw Error('External scripts unsupported.');
 const tag=html.match(/<canvas\b[^>]*id=["']stage["'][^>]*>/i)?.[0];
 const w=Number(tag?.match(/width=["'](\d+)/)?.[1]),h=Number(tag?.match(/height=["'](\d+)/)?.[1]);
 if(!w||!h||w%2||h%2)throw Error('Need #stage with even numeric width and height attributes.');
 const fontFiles=[];
 for(const style of ['Regular','Bold','Italic','Bold Italic']){
  try{const file=execFileSync('fc-match',['-f','%{file}','Arial:style='+style],{encoding:'utf8'}).trim();if(file&&fs.existsSync(file)){canvasAPI.GlobalFonts.registerFromPath(file,'Arial');fontFiles.push(file);}}catch(e){}
 }
 if(!fontFiles.length)throw Error('Arial-compatible fonts unavailable. Install local fonts and fontconfig before using this adapter.');
 const c=canvasAPI.createCanvas(w,h), elements={stage:c};
 // Skia parser does not reliably handle non-hundred numeric CSS font weights.
 const ctx=c.getContext('2d');let proto=ctx,desc;
 while(proto&&!desc){desc=Object.getOwnPropertyDescriptor(proto,'font');proto=Object.getPrototypeOf(proto);}
 const normalizedWeights=new Set();
 Object.defineProperty(ctx,'font',{get(){return desc.get.call(ctx)},set(value){const normalized=String(value).replace(/^(\d+)\s+(?=[\d.]+px\b)/,(_,weight)=>{const rounded=Math.min(900,Math.max(100,Math.round(Number(weight)/100)*100));if(rounded!==Number(weight))normalizedWeights.add(Number(weight));return rounded+' ';});desc.set.call(ctx,normalized);}});
 const context={document:{getElementById:id=>elements[id]||(elements[id]={}),body:{classList:{add(){}}}},location:{search:'?render'},performance:{now:()=>0}};
 context.window=context;
 vm.createContext(context);
 for(const match of html.matchAll(/<script\b[^>]*>([\s\S]*?)<\/script>/gi)) vm.runInContext(match[1],context,{timeout:5000});
 if(!context.motion?.renderAt||!context.motion?.stateAt)throw Error('Motion contract absent.');
 const duration=context.motion.duration,count=Math.round(duration*fps);
 if(!(duration>0&&duration<=600)||Math.abs(count/fps-duration)>0.00001)throw Error('Invalid duration.');
 fs.mkdirSync(path.dirname(path.resolve(output)),{recursive:true});
 const partial=output+'.partial.mp4';
 const encoder=spawn('ffmpeg',['-v','error','-y','-f','image2pipe','-vcodec','png','-framerate',String(fps),'-i','pipe:0','-an','-c:v','libx264','-threads','2','-preset','medium','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart',partial],{stdio:['pipe','ignore','pipe']});
 let err='';encoder.stderr.on('data',d=>err+=d);encoder.stdin.on('error',()=>{});
 const encoded=new Promise((resolve,reject)=>{encoder.on('error',reject);encoder.on('close',code=>code===0?resolve():reject(Error(err)));});
 encoded.catch(()=>{});
 let complete=false;
 try{
  for(let i=0;i<count;i++){
   context.__time=i/fps;
   vm.runInContext('motion.renderAt(__time)',context,{timeout:5000});
   if(encoder.exitCode!==null)throw Error('Encoder stopped: '+err);
   if(!encoder.stdin.write(c.toBuffer('image/png')))await Promise.race([once(encoder.stdin,'drain'),encoded.then(()=>{throw Error('Encoder closed early');})]);
   if(i%150===0)process.stderr.write('Frame '+i+'/'+count+'\n');
  }
  encoder.stdin.end();await encoded;
  fs.renameSync(partial,output);complete=true;
  const result={output,width:w,height:h,duration,fps,frames:count,audio:false,engine:'Skia via @napi-rs/canvas',fontFiles,normalizedWeights:[...normalizedWeights],networkRequests:0,limitation:'Canvas only; numeric weights rounded to hundreds; validate font metrics and pixels against browser reference.'};
  fs.writeFileSync(output+'.json',JSON.stringify(result,null,2));console.log(JSON.stringify(result));
 }finally{if(encoder.exitCode===null)encoder.kill('SIGTERM');if(!complete&&fs.existsSync(partial))fs.unlinkSync(partial);}
}
main().catch(e=>{console.error(e.message);process.exitCode=1});
