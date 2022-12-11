from tqdm import tqdm
from colorama import init, Fore
from pytube import YouTube

import os, time, subprocess, platform, shutil
from time import sleep
from path_resources import get_path, get_command
from menu import print_menu

init()

path = get_path()
clear = get_command()

# Funcion main
def main():
    opc = print_menu()
    modes(opc)


# Funcion de los modos u opciones
def modes(opc):
    if opc == 1:
        os.system(clear)
        print(Fore.CYAN + "Download Video Section")
        print(Fore.LIGHTBLUE_EX + "1. Download 1 video")
        print(Fore.BLUE + "2. Download a group of videos")
        print("")
        vid_opc = int(input(Fore.YELLOW + "Option: " + Fore.LIGHTMAGENTA_EX))
        if vid_opc == 1:
            url = input(Fore.LIGHTWHITE_EX + "Url: " + Fore.LIGHTYELLOW_EX + "")
            yt = YouTube(url)
            yt.streams.filter(
                progressive=True, file_extension="mp4"
            ).first().download(path)
            for i in tqdm(range(1000)): sleep(0.001)
            print(Fore.LIGHTBLUE_EX + "Download Finish :D")
        elif vid_opc == 2:
            numV = int(
                input(Fore.LIGHTYELLOW_EX + "Number of videos: " + Fore.LIGHTGREEN_EX)
            )
            for k in range(numV):
                video = input(
                    Fore.LIGHTGREEN_EX + f"{k + 1}. Url: " + Fore.LIGHTYELLOW_EX + ""
                )
                yt = YouTube(video)
                yt.streams.filter(
                    progressive=True, file_extension="mp4"
                ).first().download(path)
                for i in tqdm(range(1000)): sleep(0.001)
                print(Fore.LIGHTBLUE_EX + f"Video {k + 1} downloaded sucessfully")

        else:
            print(Fore.RED + "Error option is not recognized")
            print(Fore.LIGHTGREEN_EX + "Moving to main menu")
            time.sleep(2.0)
            os.system(clear)
            main()

    elif opc == 2:
        os.system(clear)
        print(Fore.LIGHTCYAN_EX + "Download Video to Mp3 Section")
        print(Fore.MAGENTA + "1. Download 1 mp3 audio")
        print(Fore.BLUE + "2. Download a group of mp3 audios")
        print("")
        vid_opc = int(input(Fore.YELLOW + "Option: " + Fore.LIGHTCYAN_EX))
        if vid_opc == 1:
            url = input(Fore.BLUE + "Url: " + Fore.LIGHTYELLOW_EX)
            yt = YouTube(url)
            if platform.system() == "Windows":
                video = yt.streams.filter(only_audio=True).first()
                fileDownloaded = video.download(path)
                base, ext = os.path.splitext(fileDownloaded)
                newFile = base + ".mp3"
                # os.rename(fileDownloaded, newFile)
                shutil.copy(fileDownloaded, newFile)
                vPath = os.path.join(path, fileDownloaded)
                os.remove(vPath)

                for i in tqdm(range(1000)): sleep(0.001)
            else:
                yt.streams.filter(
                    progressive=True, file_extension="mp4"
                ).first().download(path, filename="video.mp4")
                titulo = "video"
                parent_dir = path
                default_filename = f"{titulo}.mp4"
                new_filename = input("Ingresa el nuevo nombre (con extension .mp3): ")
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
                vPath = os.path.join(parent_dir, default_filename)
                os.remove(vPath)
                for i in tqdm(range(1000), "Finalizando"): sleep(0.001)

            print(Fore.GREEN + "Download Finish :D")
        elif vid_opc == 2:
            numMp3 = int(
                input(Fore.LIGHTBLUE_EX + "Number of audios or mp3: " + Fore.YELLOW)
            )
            for i in range(numMp3):
                url = input(Fore.BLUE + f"Url {i + 1}: " + Fore.LIGHTYELLOW_EX)
                yt = YouTube(url)
                if platform.system() == "Windows":
                    video = yt.streams.filter(only_audio=True).first()
                    fileDownloaded = video.download(path)
                    base, ext = os.path.splitext(fileDownloaded)
                    newFile = base + ".mp3"
                    # os.rename(fileDownloaded, newFile)
                    shutil.copy(fileDownloaded, newFile)
                    vPath = os.path.join(path, fileDownloaded)
                    os.remove(vPath)
                    for i in tqdm(range(1000, "Finalizando")): sleep(0.001)
                else:
                    yt.streams.filter(
                        progressive=True, file_extension="mp4"
                    ).first().download(path, filename="video.mp4")
                    titulo = "video"
                    parent_dir = path
                    default_filename = f"{titulo}.mp4"
                    new_filename = input(
                        "Ingresa el nuevo nombre (con extension .mp3): "
                    )
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
                    vPath = os.path.join(parent_dir, default_filename)
                    os.remove(vPath)
                    for i in tqdm(range(1000)): sleep(0.001)
                print(Fore.GREEN + f"Audio {i + 1} downloaded sucessfully")
        else:
            print(Fore.RED + "Error option is not recognized")
            print(Fore.LIGHTGREEN_EX + "Moving to main menu")
            time.sleep(2.0)
            os.system(clear)
            main()

    elif opc == 3:
        os.system(clear)
        time.sleep(0.5)
        print(Fore.LIGHTBLUE_EX + "End of the program :D")

    else:
        print(Fore.LIGHTBLUE_EX + "End of the program :D")


main()
