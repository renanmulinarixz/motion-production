#!/usr/bin/env python3
"""Materializar quadros de referência a partir dos arquivos incluídos na skill."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]

def prepare_pinterest():
    folder = ROOT / "assets" / "pinterest-logos"
    manifest = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
    total = 0
    for source in manifest["sources"]:
        destination = folder / source["key"]
        archive = folder / source["frame_archive"]
        expected = {Path(frame["file"]).name for frame in source["frames"]}
        with zipfile.ZipFile(archive) as package:
            members = package.namelist()
            if len(members) != len(expected):
                raise ValueError(f"Quantidade divergente em {archive.name}")
            for member in members:
                relative = Path(member)
                if relative.parts[0] != "frames" or len(relative.parts) != 2:
                    raise ValueError(f"Caminho inesperado em {archive.name}")
                if relative.name not in expected:
                    raise ValueError(f"Frame inesperado em {archive.name}")
                target = destination / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                data = package.read(member)
                if not target.exists() or target.read_bytes() != data:
                    target.write_bytes(data)
        total += len(expected)
    print(f"Pinterest pronto com {total} frames.")

def prepare_model():
    folder = ROOT / "assets" / "frames"
    manifest = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
    expected = sorted(folder.glob("frame-*.jpg"))
    if len(expected) == len(manifest["frames"]):
        print("Frames do modelo já disponíveis.")
        return
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise RuntimeError("FFmpeg necessário para materializar os frames do modelo.")
    with tempfile.TemporaryDirectory(prefix="besafe-model-") as staging:
        subprocess.run([
            ffmpeg, "-v", "error", "-i", str(ROOT / "assets" / "model.mp4"),
            "-fps_mode", "passthrough", "-start_number", "0", "-q:v", "3",
            str(Path(staging) / "frame-%06d.jpg")
        ], check=True)
        images = sorted(Path(staging).glob("frame-*.jpg"))
        if len(images) != len(manifest["frames"]):
            raise ValueError("Quantidade de quadros diferente do manifesto do modelo.")
        folder.mkdir(parents=True, exist_ok=True)
        for image in images:
            shutil.copyfile(image, folder / image.name)
    print(f"Modelo pronto com {len(images)} frames.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", choices=["pinterest", "model", "all"], default="pinterest")
    args = parser.parse_args()
    if args.source in {"pinterest", "all"}:
        prepare_pinterest()
    if args.source in {"model", "all"}:
        prepare_model()
