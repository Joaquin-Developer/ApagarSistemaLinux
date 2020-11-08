
import subprocess

hora = input("Ingresar hora (valido entre 00 y 23): ");
minuto = input("Ingresar minuto (valido entre 00 y 59): ");

def Validar(hora = None, minuto = None):
    # return True
    print(str(hora) + ':' + str(minuto))
    pass

Validar(hora, minuto);


subprocess.call("ls -la ", shell=True)
