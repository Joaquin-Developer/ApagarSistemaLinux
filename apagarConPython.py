
# coding=utf-8

import subprocess
import datetime

hh = input("Ingresar hora (valido entre 0 y 23): ");
mm = input("Ingresar minuto (valido entre 0 y 59): ");

def Shutdown():  
    while True:
        if (datetime.datetime.now().hour == int(hh)) and (datetime.datetime.now().minute == int(mm)):
            break
        pass
    subprocess.call("poweroff", shell=True)

# validaciones:    > <
try:
    if (int(hh) >= 0 and int(hh) < 24) and (int(mm) >= 0 and int(mm) < 60):
        Shutdown()
except:
    print("Error: No se pudo realizar la conversión de datos ingresados")
    pass


#subprocess.call("ls -la ", shell=True)
