# Pixevon Productions reel factory

Generates short vertical reels (1080x1920, voice, sound effects, soft music) and hosts the finished videos for scheduling.

- `generator/` the reel generator (HTML scenes + 3D phone via three.js, Kokoro TTS, Playwright capture, ffmpeg)
- `videos/` finished reels, public at `https://raw.githubusercontent.com/reclaivo/pixevon/main/videos/<file>.mp4`
- `WEEKLY.md` the weekly routine (make reels, push, schedule in Publer via the ZapierP connection)
- `schedule.json` every reel with its caption, planned time and status

## Setup in a fresh machine
```
pip install kokoro-onnx soundfile scipy pillow playwright --break-system-packages
# Chromium + ffmpeg must exist (Playwright chromium is usually preinstalled)
mkdir -p ~/tts && cd ~/tts
curl -L -o kokoro.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
curl -L -o voices.bin  https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
```
(Models are about 330 MB, so they are not stored in this repo. Voice used: `af_heart`.)

## Make one reel (run from `generator/`)
```
python3 gen.py R12        # TTS + timeline + html + sfx wav for the reel named R12 in reels.py
python3 music.py R12      # adds the soft music bed
python3 render.py R12     # captures frames, muxes to out/R12.mp4 (about 5 min per reel on 2 CPUs)
```
Reel names must be `R<number>` (the number seeds the background shuffle). Total length must stay <= 15 s (gen.py asserts this).
