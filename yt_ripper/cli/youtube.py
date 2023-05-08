import os, shutil, subprocess
from uuid import uuid4
from pytube import YouTube
from colorama import Fore

from yt_ripper.cli.loading import loading_bar

def get_url():
    url = input(Fore.LIGHTWHITE_EX + "Url: " + Fore.LIGHTYELLOW_EX + "")
    return url

def download_video(url, path):
    yt = YouTube(url, use_oauth=True , allow_oauth_cache=True)
    print(Fore.BLUE + "Fetching Video")
    yt.streams.get_highest_resolution().download(path)
    # filter(progressive=True, file_extension="mp4").first().download(
    #     path
    # )
    loading_bar('Downloading video')
    print(Fore.LIGHTBLUE_EX + "Download Finish :D")

def download_audio_win(yt, path):
    print(Fore.BLUE + "Downloading Audio")
    video = yt.streams.filter(only_audio=True).first()
    fileDownloaded = video.download(path)
    base, ext = os.path.splitext(fileDownloaded)
    newFile = base + ".mp3"
    shutil.copy(fileDownloaded, newFile)
    vPath = os.path.join(path, fileDownloaded)
    os.remove(vPath)
    loading_bar()

def download_audio(yt, path):
    id = uuid4() 
    print(Fore.BLUE + "Downloading...")
    yt.streams.filter(
        progressive=True, file_extension="mp4"
    ).first().download(path, filename=f"{id}.mp4")
    parent_dir = path
    default_filename = f"{id}.mp4"
    new_filename = input("Ingresa el nuevo nombre (con extension .mp3): ")
    print(Fore.BLUE + "Converting to audio")
    subprocess.run(
        [
            "ffmpeg",
            "-i",
            os.path.join(parent_dir, default_filename),
            os.path.join(parent_dir, new_filename),
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
    )
    vid_path = os.path.join(parent_dir, default_filename)
    os.remove(vid_path)
    loading_bar('Finalizando conversion')
