from datos import *
from funciones import *
from menu import *

while True:
    menu()
    op = opcion()
    if op == 1:
        print("--"*10)
        registrar()
        print("--"*10)
    elif op == 2:
        print("--"*10)
        listar()
        print("--"*10)
    elif op == 3:
        print("--"*10)
        modificar()
        print("--"*10)
    elif op == 4:
        print("--"*10)
        despedir()
        print("--"*10)
    elif op == 5:
        print("--"*10)
        entrada()
        print("--"*10)
    elif op == 6:
        print("--"*10)
        salida()
        print("--"*10)
    elif op == 7:
        print("--"*10)
        print("Adios!")
        print("--"*10)
        break
    else:
        print("--"*10)
        print("Opcion invalida!")
        print("--"*10)

