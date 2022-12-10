import os, time,subprocess, platform, tqdm, shutil
from tqdm import tqdm 
from pathlib import Path
from getpass import getuser
from colorama import init, Fore, Back, Style
init()
from pytube import YouTube

rango = 1

if( platform.system() == 'Windows' ):
    clear = 'cls'
    home = Path.home()
    path = f'{home}/Downloads/'

else:
    clear = 'clear'
    usuario = getuser()
    path = f'/home/{usuario}/Downloads'

# Funcion main 
def main():
    os.system(clear)
    print(Fore.BLUE + 'Terminal Application to dowload videos and mp3')
    print(Fore.CYAN + '1. Download a Video')
    print(Fore.GREEN + '2. Download a Video to Mp3')
    print(Fore.RED + '3. Exit')
    print('')
    opc = int(input('What you want to do? '))
    modes(opc)


# Funcion de los modos u opciones
def modes(opc):
    if(opc == 1):
        os.system(clear)
        print(Fore.CYAN + 'Download Video Section')
        print(Fore.LIGHTBLUE_EX + '1. Download 1 video')
        print(Fore.BLUE + '2. Download a group of videos')
        print('')
        vidOp = int(input(Fore.YELLOW + 'Option: ' + Fore.LIGHTMAGENTA_EX))
        if(vidOp == 1):
           url = input(Fore.LIGHTWHITE_EX + 'Url: ' + Fore.LIGHTYELLOW_EX + '')
           for i in tqdm(range(rango)):
                yt = YouTube(url)
                yt.streams.filter(progressive=True, file_extension='mp4').first().download(path)
           print(Fore.LIGHTBLUE_EX + 'Download Finish :D')
        elif(vidOp == 2):
            numV = int(input(Fore.LIGHTYELLOW_EX + 'Number of videos: ' + Fore.LIGHTGREEN_EX))
            for k in range(numV):
                video = input(Fore.LIGHTGREEN_EX + f'{k + 1}. Url: ' + Fore.LIGHTYELLOW_EX + '')
                for i in tqdm(range(rango)):
                    yt = YouTube(video)
                    yt.streams.filter(progressive=True, file_extension='mp4').first().download(path)
                print(Fore.LIGHTBLUE_EX + f'Video {k + 1} downloaded sucessfully')
            
        else:
            print(Fore.RED + 'Error option is not recognized')
            print(Fore.LIGHTGREEN_EX + 'Moving to main menu')
            time.sleep(2.0)
            os.system(clear)
            main()

    elif(opc == 2):
        os.system(clear)
        print(Fore.LIGHTCYAN_EX + 'Download Video to Mp3 Section')
        print(Fore.MAGENTA + '1. Download 1 mp3 audio')
        print(Fore.BLUE + '2. Download a group of mp3 audios')
        print('')
        vidOp = int(input(Fore.YELLOW + 'Option: ' + Fore.LIGHTCYAN_EX))
        if(vidOp == 1):
           url = input(Fore.BLUE + 'Url: ' + Fore.LIGHTYELLOW_EX)
           yt = YouTube(url)
           if( platform.system() == 'Windows' ):
                for i in tqdm(range(rango)):
                    video = yt.streams.filter(only_audio=True).first()
                    fileDownloaded = video.download(path)
                    base, ext = os.path.splitext(fileDownloaded)
                    newFile = base + '.mp3'
                    # os.rename(fileDownloaded, newFile)
                    shutil.copy(fileDownloaded, newFile)
                    vPath = os.path.join(path , fileDownloaded) 
                    os.remove(vPath)
           else:
                yt.streams.filter(progressive=True, file_extension='mp4').first().download(path, filename='video.mp4')
                titulo = 'video'
                parent_dir = path
                default_filename = f'{titulo}.mp4'
                new_filename = input("Ingresa el nuevo nombre (con extension .mp3): ")
                for i in tqdm(range(rango)):
                    subprocess.run([
                        'ffmpeg',
                        '-i', os.path.join(parent_dir, default_filename),
                        os.path.join(parent_dir, new_filename)
                    ], stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
                    vPath = os.path.join(parent_dir, default_filename) 
                    os.remove(vPath)
           print(Fore.GREEN + 'Download Finish :D')
        elif(vidOp == 2):
            numMp3 = int(input(Fore.LIGHTBLUE_EX + 'Number of audios or mp3: ' + Fore.YELLOW))
            for i in range(numMp3):
                url = input(Fore.BLUE + f'Url {i + 1}: ' + Fore.LIGHTYELLOW_EX)
                yt = YouTube(url)
                if( platform.system() == 'Windows' ):
                    for i in tqdm(range(rango)):
                        video = yt.streams.filter(only_audio=True).first()
                        fileDownloaded = video.download(path)
                        base, ext = os.path.splitext(fileDownloaded)
                        newFile = base + '.mp3'
                        # os.rename(fileDownloaded, newFile)
                        shutil.copy(fileDownloaded, newFile)
                        vPath = os.path.join(path , fileDownloaded) 
                        os.remove(vPath)
                else:
                    yt.streams.filter(progressive=True, file_extension='mp4').first().download(path, filename='video.mp4')
                    titulo = 'video'
                    parent_dir = path
                    default_filename = f'{titulo}.mp4'
                    new_filename = input("Ingresa el nuevo nombre (con extension .mp3): ")
                    for i in tqdm(range(rango)):
                        subprocess.run([
                            'ffmpeg',
                            '-i', os.path.join(parent_dir, default_filename),
                            os.path.join(parent_dir, new_filename)
                        ], stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
                        vPath = os.path.join(parent_dir, default_filename) 
                        os.remove(vPath)
                print(Fore.GREEN + f'Audio {i + 1} downloaded sucessfully')
        else:
            print(Fore.RED + 'Error option is not recognized')
            print(Fore.LIGHTGREEN_EX + 'Moving to main menu')
            time.sleep(2.0)
            os.system(clear)
            main()
    
    elif(opc == 3):
        os.system(clear)
        time.sleep(0.5)
        print(Fore.LIGHTBLUE_EX + 'End of the program :D')

    else:
        print(Fore.LIGHTBLUE_EX + 'End of the program :D')


main()
