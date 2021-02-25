# coding=utf-8
import subprocess, datetime

text_answer = "Ingresar hora válida para realizar la acción (ej: 14:30): "

def main():
    user_input = input("Ingrese (1) para apagar, o (2) para reiniciar: ")
    try:
        option = int(user_input)
        if option not in (1, 2): raise Exception("Error: debe ingresar una opción válida!")
        action_time = ask_time_to_action()

    except ValueError as e:
        print("Error: Debe ingresar un número válido")
    except IndexError as e:
        print("Error: El dato que ingresó no es válido")
    except Exception as e:
        print(e)
    else:
        actual_time = get_actual_time()
        action_time = ask_time_to_action()
        # Optimizar esto (cambiar el while True):
        while True:
            if (actual_time == action_time) and option == 1: poweroff()
            elif (actual_time == action_time) and option == 2: reboot()


def poweroff():
    subprocess.call("poweroff", shell=True)

def reboot():
    subprocess.call("reboot", shell=True)

def get_actual_time():
    actual_time = datetime.datetime.now()
    return str(actual_time.hour) + ":" + str(actual_time.minute)

def ask_time_to_action():
    user_date = input(text_answer)
    try:
        hh = int(user_date.split(":")[0])
        mm = int(user_date.split(":")[1])
    except IndexError as e:
        raise e
    except ValueError as e:
        raise e
    else:
        if hh < 10: hh = ("0" + str(hh))
        if mm < 10: mm = ("0" + str(mm))
        return hh + ":" + mm

if __name__ == "__main__":
    main()
