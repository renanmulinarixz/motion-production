#!/usr/bin/env python3
"""Inspect local motion dependencies without launching apps or calling providers."""
import json
import os
from pathlib import Path
import shutil
import subprocess


def detect_capabilities():
    executables = {name: shutil.which(name) for name in ('node', 'ffmpeg', 'ffprobe', 'fc-match')}
    modules = {'playwright': False, 'canvas': False, 'playwright_browser': None}
    node = executables['node']
    if node:
        javascript = """
const fs=require('node:fs'),path=require('node:path');
const result={playwright:false,canvas:false,playwright_browser:null};
function load(name){
 try{return require(name)}catch(e){
  const root=process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES;
  if(root)return require(path.join(root,name));
  throw e;
 }
}
try{const p=load('playwright');result.playwright=true;const exe=p.chromium.executablePath();if(fs.existsSync(exe))result.playwright_browser=exe;}catch(e){}
try{load('@napi-rs/canvas');result.canvas=true;}catch(e){}
console.log(JSON.stringify(result));
"""
        try:
            probe = subprocess.run([node, '-e', javascript], capture_output=True, text=True, timeout=15)
            if probe.returncode == 0:
                modules.update(json.loads(probe.stdout))
        except (OSError, subprocess.TimeoutExpired, json.JSONDecodeError):
            modules['probe_incomplete'] = True
    candidates = []
    for value in (os.environ.get('PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH'), modules.get('playwright_browser')):
        if value:
            candidates.append(Path(value))
    for name in ('chromium', 'chromium-browser', 'google-chrome', 'google-chrome-stable', 'chrome', 'msedge'):
        value = shutil.which(name)
        if value:
            candidates.append(Path(value))
    for variable in ('PROGRAMFILES', 'PROGRAMFILES(X86)', 'LOCALAPPDATA'):
        base = os.environ.get(variable)
        if base:
            candidates += [Path(base) / 'Google/Chrome/Application/chrome.exe',
                           Path(base) / 'Microsoft/Edge/Application/msedge.exe']
    browsers = sorted({str(candidate) for candidate in candidates if candidate.is_file()})
    return {
        'python': True,
        'executables': executables,
        'modules': modules,
        'browser_executables_found': browsers,
        'browser_launch_tested': False,
        'render_routes': {
            'chromium': {'dependencies_found': bool(node and modules['playwright'] and browsers and executables['ffmpeg'])},
            'skia': {'dependencies_found': bool(node and modules['canvas'] and executables['ffmpeg'] and executables['fc-match']),
                     'note': 'Current adapter also needs compatible local fonts.'},
        },
        'connected_tools_and_native_editors': 'Discover separately from the current session tools and application access.',
        'network_calls': 0,
        'installations_performed': 0,
    }


if __name__ == '__main__':
    print(json.dumps(detect_capabilities(), ensure_ascii=True, indent=2))
