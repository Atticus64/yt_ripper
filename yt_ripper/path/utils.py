import platform
from pathlib import Path
from getpass import getuser

def get_path():
    if platform.system() == "Windows":
        home = Path.home()
        path = f"{home}/Downloads/"

    else:
        usuario = getuser()
        path = f"/home/{usuario}/Downloads"

    return path


def get_command():
    if platform.system() == "Windows":
        command = "cls"

    else:
        command = "clear"

    return command
