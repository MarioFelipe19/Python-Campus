from colorama import init, Fore, Back, Style
from termcolor import colored



init(autoreset=True)

def menu_principal():
    print("")
    # print(Fore.RED + Back.YELLOW + "=="* 20)
    # print(Style.BRIGHT + "          proyecto scrum")
    # print(colored('Texto parpadeante', 'cyan', attrs=['blink']))
    # print(colored('Texto con colores invertidos', 'blue', attrs=['reverse']))
    # print(colored('Texto subrayado', 'green', attrs=['underline']))
    # print(colored('Texto blanco con fondo cian', 'white', 'on_cyan'))
    # print(colored('Texto en negrita', 'magenta', attrs=['bold']))
    # print(colored('Este texto es rojo', 'red'))
    # print(colored('Este texto es verde', 'green'))
    # print(colored('Este texto es azul', 'blue'))
    # print(colored('Este texto es amarillo', 'yellow'))
    # print(colored('Este texto es magenta', 'magenta'))
    # print(colored('Este texto es cian', 'cyan'))
    # print(colored('Este texto es blanco', 'white'))

    # # Texto con fondo
    # print(colored('Texto negro con fondo blanco', 'grey', 'on_white'))
    # print(colored('Texto rojo con fondo verde', 'red', 'on_green'))
    # print(colored('Texto amarillo con fondo azul', 'yellow', 'on_blue'))
    # print(colored('Texto cian con fondo magenta', 'cyan', 'on_magenta'))
    # print(colored('Texto blanco con fondo cian', 'white', 'on_cyan'))

    # # Texto con atributos
    # print(colored('Texto subrayado', 'green', attrs=['underline']))
    # print(colored('Texto en negrita', 'yellow', attrs=['bold']))
    # print(colored('Texto parpadeante', 'magenta', attrs=['blink']))
    # print(colored('Texto con colores invertidos', 'blue', attrs=['reverse']))

    # print(Fore.RED + "=="* 20)
    print("")
    print("     1. Indicar sección")
    print("     2. Registrarse")
    print("     3. Salir")
    # print(Fore.RED + "=="* 20)
    print("")
    

def pedir_opcion():
    try:
        print("//"*20)
        op = int(input("  Ingrese su opcion: "))
        print("//"*20)
        
        return op
        
    except Exception:
        print("--"*20)
        print("valor invalido")