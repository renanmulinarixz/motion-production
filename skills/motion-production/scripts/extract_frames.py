#!/usr/bin/env python3
"""Extract every decoded frame and original PTS; does not resample VFR inputs."""
import argparse, hashlib, json, pathlib, subprocess
p = argparse.ArgumentParser()
p.add_argument('video', type=pathlib.Path)
p.add_argument('directory', type=pathlib.Path)
p.add_argument('--format', choices=['jpg','png'], default='jpg')
a = p.parse_args()
if a.directory.exists() and any(a.directory.iterdir()):
    p.error('Output directory must be empty.')
a.directory.mkdir(parents=True,exist_ok=True)
r = subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_frames','-show_entries','frame=best_effort_timestamp_time','-of','json',str(a.video)],check=True,capture_output=True,text=True)
timestamps = [float(f['best_effort_timestamp_time']) for f in json.loads(r.stdout)['frames']]
cmd = ['ffmpeg','-v','error','-i',str(a.video),'-map','0:v:0','-fps_mode','passthrough','-start_number','0']
if a.format == 'jpg': cmd += ['-q:v','3']
subprocess.run(cmd + [str(a.directory / ('frame-%06d.' + a.format))],check=True)
images = sorted(a.directory.glob('frame-*.' + a.format))
assert len(images)==len(timestamps), (len(images),len(timestamps))
manifest = {'source':a.video.name,'source_sha256':hashlib.sha256(a.video.read_bytes()).hexdigest(),'resampled':False,'encoding':'JPEG FFmpeg q=3' if a.format=='jpg' else 'PNG lossless','frames':[{'index':i,'time':t,'file':f.name} for i,(t,f) in enumerate(zip(timestamps,images))]}
(a.directory/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'frames':len(images),'first_pts':timestamps[0],'last_pts':timestamps[-1],'directory':str(a.directory)}))
