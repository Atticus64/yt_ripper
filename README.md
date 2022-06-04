# __Terminal script__ to download videos and convert to *mp3*
## By Jona
---
 _This script will be one of my tools to learn python and terminal utilities_

<img src="./assets/python-logo.png" alt="python" width="190"/>
<img src="./assets/powershell-logo.png" alt="powershell" width="190"/>

The dependencies of this script is the package *python3*, *pytube*, *colorama* and ffmpeg in linux
Install the packages with:
```
pip install pytube
```
I recomend download pytube by the next command to prevent problems:
```
python -m pip install git+https://github.com/kinshuk-h/pytube
```
```
pip install colorama
```
```
pip install tqdm
```
if you don't have pip, install with the next command:
In Windows download the script get-pip.py and navigate to that script and execute:
```
python get-pip.py`
```
In Mac in the terminal:
```
python Downloads/get-pip.py
```
or in the path of your get-pip.
In Linux in the terminal:
```
python Downloads/get-pip.py
```
or in the path of your get-pip.
Verify you have pip with the command:
`pip`
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
Clone this repository and execute the script:
```
python main.py
```
#### Demo Video
[![asciicast](https://asciinema.org/a/aYDSGccQ9o3Xyk051VqILxlNV.svg)](https://asciinema.org/a/lQVS73Crocx6Al6XF11yVg4UI?autoplay=1)

