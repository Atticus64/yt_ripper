# __Terminal script__ to download videos and convert to *mp3*
## By Jona
---
 _This script will be one of my tools to learn python and terminal utilities_

<img src="./assets/python-logo.png" alt="python" width="190"/><img src="./assets/powershell-logo.png" alt="powershell" width="190"/>

## Important
The dependencies of this script is the package *python3*, *pytube*, *colorama* and ffmpeg in linux

if you dont have pip install with: 

```
apt install python3-pip
```

Or your package manager for your distro

And install ffmpeg with the command:
**In Debian and Ubuntu Based:**

```
apt install ffmpeg
```
**In Fedora and CentOS:**
```
dnf install ffmpeg ffmpeg-devel
```
**In ArchLinux:** 
```
pacman -R ffmpeg4.0
```
And verify you have ffmpeg with:
```
ffmpeg --version
```

## Init virtual env

```bash
python3 -m venv .env
```

## install Dependencies 

```bash
pip install -r requirements.txt 
```

## Run cli

```bash
python main.py
```

#### Demo Video
[![asciicast](https://asciinema.org/a/aYDSGccQ9o3Xyk051VqILxlNV.svg)](https://asciinema.org/a/lQVS73Crocx6Al6XF11yVg4UI?autoplay=1)