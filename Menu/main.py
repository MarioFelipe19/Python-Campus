from menu import*   
import os

def clear_console():
    # Detecta el sistema operativo y usa el comando adecuado
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

while True:
    menu_principal()
    op = pedir_opcion()
    
    if op == 3:
        print("--"*20)
        print("Adios!!")
        print("--"*20)
        break
    if op == 1:
        
        print(1)
    if op == 2:
        clear_console()
        print(2)
    if op == 3:
        
        print(3)
