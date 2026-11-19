#!/usr/bin/env python3
"""Check final video metadata and fully decode it. No network."""
import argparse, json, subprocess
from fractions import Fraction
p = argparse.ArgumentParser()
p.add_argument('video')
p.add_argument('--duration', type=float, required=True)
p.add_argument('--fps', type=float, required=True)
p.add_argument('--frames', type=int, required=True)
a = p.parse_args()
r = subprocess.run(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',a.video],check=True,capture_output=True,text=True)
data = json.loads(r.stdout)
v = next(s for s in data['streams'] if s['codec_type'] == 'video')
fps = float(Fraction(v['avg_frame_rate']))
duration = float(v.get('duration',data['format']['duration']))
frames = int(v['nb_read_frames'])
assert abs(fps-a.fps) < .001, (fps,a.fps)
assert abs(duration-a.duration) <= 1/a.fps, (duration,a.duration)
assert frames == a.frames, (frames,a.frames)
subprocess.run(['ffmpeg','-v','error','-xerror','-i',a.video,'-f','null','-'],check=True)
print(json.dumps({'ok':True,'duration':duration,'fps':fps,'frames':frames,'width':v['width'],'height':v['height'],'audio':any(s['codec_type']=='audio' for s in data['streams'])},indent=2))
