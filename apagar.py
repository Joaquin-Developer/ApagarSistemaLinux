"""
Apagar sistema
"""

import subprocess
from typing import Tuple
from datetime import datetime
from time import sleep


def validate_params(hour: str, minite: str):
    """validate the inputs"""
    if (int(hour) < 0 or int(hour) >= 24) or (int(minite) < 0 or int(minite) >= 60):
        raise Exception("Formato ingresado de hora/minutos invalido.")


def input_params() -> Tuple[int, int, int]:
    """read the params"""
    option = input("Ingrese 1 para APAGAR, 2 para REINICIAR: ")
    hour = input("Ingresar hora (valido entre 0 y 23): ")
    minute = input("Ingresar minuto (valido entre 0 y 59): ")
    validate_params(hour, minute)
    return hour, minute, option


def run_subprocess(hour: str, minute: str, option: int = 1):
    """run poweroff or reboot command."""
    while True:
        if datetime.now().hour == int(hour) and datetime.now().minute == int(minute):
            break
        sleep(30)

    if option == 1:
        subprocess.call("poweroff", shell=True)
    else:
        subprocess.call("reboot", shell=True)


def main():
    """main method"""
    hour, minute, option = input_params()
    run_subprocess(hour, minute, option)


if __name__ == "__main__":
    main()
