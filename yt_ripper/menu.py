import os
from colorama import Fore

from path_resources import get_command


def print_menu():
    os.system(get_command())
    print(Fore.BLUE + "Terminal Application to dowload videos and mp3")
    print(Fore.CYAN + "1. Download a Video")
    print(Fore.GREEN + "2. Download a Video to Mp3")
    print(Fore.RED + "3. Exit")
    print("")
    opc = int(input("What you want to do? "))
    return opc
