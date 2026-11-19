#!/usr/bin/env node
// Deterministic offline Canvas export. Usage: node render.cjs input.html output.mp4 [fps]
const fs = require('node:fs');
const path = require('node:path');
const {pathToFileURL} = require('node:url');
const {spawn} = require('node:child_process');
const {once} = require('node:events');
let playwright;
try { playwright = require('playwright'); }
catch (e) {
  const root = process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES;
  if (!root) throw new Error('Install local Playwright and Chromium before offline rendering.');
  playwright = require(path.join(root, 'playwright'));
}
async function main() {
  const [input, output, fpsArg = '30'] = process.argv.slice(2);
  const fps = Number(fpsArg);
  if (!input || !output || !Number.isFinite(fps) || fps < 1 || fps > 120) throw Error('Usage: node render.cjs input.html output.mp4 [fps 1..120]');
  if (fs.existsSync(output)) throw Error('Output exists; choose another path.');
  fs.mkdirSync(path.dirname(path.resolve(output)), {recursive:true});
  let browser, encoder, completed = false;
  const partial = output + '.partial.mp4';
  try {
    const executable = process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH || [playwright.chromium.executablePath(),'/usr/bin/chromium','/usr/bin/google-chrome'].find(p => fs.existsSync(p));
    browser = await playwright.chromium.launch({headless:true, ...(executable ? {executablePath:executable} : {})});
    const page = await browser.newPage({viewport:{width:1440,height:900}, deviceScaleFactor:1});
    const blocked = [], errors = [];
    await page.route(/https?:\/\//, route => {blocked.push(route.request().url()); return route.abort();});
    page.on('pageerror', e => errors.push(e.message));
    await page.goto(pathToFileURL(path.resolve(input)).href + '?render');
    await page.evaluate(() => document.fonts.ready);
    const meta = await page.evaluate(() => {
      const c = document.querySelector('#stage');
      if (!c || !window.motion || typeof motion.renderAt !== 'function' || typeof motion.stateAt !== 'function') throw Error('Need #stage Canvas and motion.renderAt/stateAt/duration.');
      return {width:c.width,height:c.height,duration:motion.duration};
    });
    if (!(meta.duration > 0 && meta.duration <= 600) || !Number.isInteger(meta.width) || !Number.isInteger(meta.height) || meta.width % 2 || meta.height % 2) throw Error('Require positive duration <=600s and even pixel dimensions.');
    const count = Math.round(meta.duration * fps);
    if (Math.abs(count / fps - meta.duration) > 0.00001) throw Error('Duration must contain an integer number of frames.');
    encoder = spawn('ffmpeg', ['-v','error','-y','-f','image2pipe','-vcodec','png','-framerate',String(fps),'-i','pipe:0','-an','-c:v','libx264','-threads','2','-preset','medium','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart',partial], {stdio:['pipe','ignore','pipe']});
    let stderr = '';
    encoder.stderr.on('data', d => stderr += d.toString());
    const encoded = new Promise((resolve,reject) => {
      encoder.on('error',reject);
      encoder.on('close', code => code === 0 ? resolve() : reject(Error('FFmpeg failed: ' + stderr)));
    });
    // Handle early exit while rendering without an unhandled rejected promise.
    encoded.catch(() => {});
    encoder.stdin.on('error', () => {});
    for (let i=0; i<count; i++) {
      const png = await page.evaluate(t => {
        motion.renderAt(t);
        return document.querySelector('#stage').toDataURL('image/png').split(',')[1];
      }, i/fps);
      if (encoder.exitCode !== null) throw Error('Encoder stopped: ' + stderr);
      if (!encoder.stdin.write(Buffer.from(png,'base64'))) await Promise.race([once(encoder.stdin,'drain'), encoded.then(() => {throw Error('Encoder closed early');})]);
      if (i % 150 === 0) process.stderr.write('Frame ' + i + '/' + count + '\n');
    }
    encoder.stdin.end();
    await encoded;
    if (blocked.length || errors.length) throw Error(JSON.stringify({blocked,errors}));
    fs.renameSync(partial,output);
    fs.writeFileSync(output + '.json', JSON.stringify({...meta,fps,frames:count,audio:false,networkRequests:blocked,pageErrors:errors},null,2));
    completed = true;
    console.log(JSON.stringify({output,...meta,fps,frames:count}));
  } finally {
    if (encoder && encoder.exitCode === null) encoder.kill('SIGTERM');
    if (browser) await browser.close();
    if (!completed && fs.existsSync(partial)) fs.unlinkSync(partial);
  }
}
main().catch(e => {console.error(e.message);process.exitCode=1;});
