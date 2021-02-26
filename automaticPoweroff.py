# coding=utf-8
import subprocess, datetime
debug_mode = False

def main():
    user_input = input("Ingrese (1) para apagar, o (2) para reiniciar: ")
    try:
        option = int(user_input)
        if option not in (1, 2): raise Exception("Error: debe ingresar una opción válida!")
        actual_time = get_actual_time()
        action_time = ask_time_to_action()

    except ValueError as e:
        print("Error: Debe ingresar un número válido")
    except IndexError as e:
        print("Error: El dato que ingresó no es válido")
    except Exception as e:
        print(e)
    else:
        # Optimizar esto (cambiar el while True):
        action_name = "apagará" if option == 1 else "reiniciará"
        print("El sistema se {} a las {}".format(action_name, action_time))
        print("Presione Ctrl + Z para detener.")

        while True:
            if (actual_time == action_time) and option == 1: poweroff()
            elif (actual_time == action_time) and option == 2: reboot()


def poweroff():
    if debug_mode: print("Apagando...")
    else: subprocess.call("poweroff", shell=True)

def reboot():
    if debug_mode: print("Reiniciando...")
    else: subprocess.call("reboot", shell=True)

def get_actual_time():
    actual_time = datetime.datetime.now()
    return str(actual_time.hour) + ":" + str(actual_time.minute)

def ask_time_to_action():
    user_date = input("Ingresar hora válida para realizar la acción (ej: 14:30): ")
    try:
        hh = int(user_date.split(":")[0])
        mm = int(user_date.split(":")[1])
    except IndexError as e:
        raise e
    except ValueError as e:
        raise e
    else:
        if hh < 10: hh = ("0" + str(hh))
        else: hh = str(hh)

        if mm < 10: mm = ("0" + str(mm))
        else: mm = str(mm)

        return hh + ":" + mm

if __name__ == "__main__":
    main()
