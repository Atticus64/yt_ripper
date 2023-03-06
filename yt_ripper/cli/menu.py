import os
from colorama import Fore, Style

from yt_ripper.path.utils import get_command

clear = get_command()


def print_menu():
    os.system(clear)
    print(Fore.BLUE + "Terminal Application to dowload videos and mp3")
    print(Fore.CYAN + "1. Download a Video")
    print(Fore.GREEN + "2. Download a Video to Mp3")
    print(Fore.RED + "3. Exit")
    print(Fore.WHITE + "")
    opc = int(input(Fore.YELLOW + "What you want to do? " + Fore.WHITE))
    return opc


def video_menu():
    os.system(clear)
    print(Fore.CYAN + "Download Video Section")
    print(Fore.LIGHTBLUE_EX + "1. Download 1 video")
    print(Fore.BLUE + "2. Download a group of videos")
    print(Style.RESET_ALL + "")
    vid_opc = int(input(Fore.YELLOW + "Option: " + Fore.LIGHTMAGENTA_EX))
    return vid_opc


def audio_menu():
    os.system(clear)
    print(Fore.LIGHTCYAN_EX + "Download Video to Mp3 Section")
    print(Fore.MAGENTA + "1. Download 1 mp3 audio")
    print(Fore.BLUE + "2. Download a group of mp3 audios")
    print("")
    aud_opc = int(input(Fore.YELLOW + "Option: " + Fore.LIGHTCYAN_EX))
    return aud_opc
