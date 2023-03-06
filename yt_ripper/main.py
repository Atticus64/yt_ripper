from colorama import init, Fore
from pytube import YouTube

import os, time, platform
from yt_ripper.path.utils import get_command, get_path
from yt_ripper.cli.menu import print_menu, video_menu, audio_menu
from yt_ripper.cli.youtube import get_url, download_video, download_audio_win, download_audio

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
        vid_opc = video_menu()
        if vid_opc == 1:
            url = get_url()
            download_video(url, path)
        elif vid_opc == 2:
            num_vid = int(
                input(Fore.LIGHTYELLOW_EX + "Number of videos: " + Fore.LIGHTGREEN_EX)
            )
			# Por cada video se descarga 
            for k in range(num_vid):
                video = input(
                    Fore.LIGHTGREEN_EX + f"{k + 1}. Url: " + Fore.LIGHTYELLOW_EX + ""
                )
                download_video(video, path)

        else:
            print(Fore.RED + "Error option is not recognized")
            print(Fore.LIGHTGREEN_EX + "Moving to main menu")
            time.sleep(2.0)
            os.system(clear)
            main()

    elif opc == 2:
        vid_opc = audio_menu()
        if vid_opc == 1:
            url = get_url()
            yt = YouTube(url)
            if platform.system() == "Windows":
                download_audio_win(yt, path)
            else:
                download_audio(yt, path)

            print(Fore.GREEN + "Download Finish :D")
        elif vid_opc == 2:
            num_mp3 = int(
                input(Fore.LIGHTBLUE_EX + "Number of audios or mp3: " + Fore.YELLOW)
            )
            for i in range(num_mp3):
                url = get_url()
                yt = YouTube(url)
                if platform.system() == "Windows":
                    download_audio_win(yt, path)
                else:
                    download_audio(yt, path)
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


if __name__ == '__main__':
    main()

