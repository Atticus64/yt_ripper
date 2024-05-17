# __Terminal script__ to download videos and convert to *mp3*
## By Jona
---
 _This script will be one of my tools to learn python and terminal utilities_

<img src="https://i.postimg.cc/YCNfYM5Z/python-logo.png" alt="python" width="190"/><img src="https://i.postimg.cc/kg7wj2vq/powershell-logo.png" alt="powershell" width="190"/>

## Requirements
The dependencies of this script are the packages 
- *python3*
- *pytube*
- *colorama*
- ffmpeg in linux

### Install pip
if you dont have pip install with: 

```
apt install python3-pip
```

Or your package manager for your distro

### Install ffmpeg
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
pacman -S ffmpeg4.4
```
And verify you have ffmpeg with:
```
ffmpeg --version
```

## Installation 

### Using pip
```
pip install yt_ripper
```
### Using source files
```bash
git clone https://github.com/Atticus64/yt_ripper.git
cd yt_ripper
pip install -r requirements.txt
cd yt_ripper
python3 main.py
```

#### Demo Video
[![asciicast](https://asciinema.org/a/544630.svg)](https://asciinema.org/a/544630)
