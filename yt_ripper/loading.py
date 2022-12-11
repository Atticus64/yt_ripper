from tqdm import tqdm
from time import sleep
from colorama import Style, Fore

def loading_bar(message):
    Style.RESET_ALL
    if message == None:
      for i in tqdm(range(1000), Fore.WHITE + "Finalizando descarga"):
          sleep(0.001)

    else:
      for i in tqdm(range(1000), Fore.WHITE + message):
          sleep(0.001)