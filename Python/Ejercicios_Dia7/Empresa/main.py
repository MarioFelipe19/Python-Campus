from datos import *
from menu import *
from funciones import *



while True:
    menu()
    op = opcion()
    if op == 1:
        print("--"*10)
        masempleados()
        print("--"*10)
    elif op == 2:
        print("--"*10)
        promedioempleados()
        print("--"*10)
    elif op == 3:
        print("--"*10)
        dobleempleados()
        print("--"*10)
    elif op == 4:
        print("--"*10)
        reorganizar()
        print("--"*10)
    elif op == 5:
        print("--"*10)
        print("Adios!")
        print("--"*10)
        break
    else:
        print("--"*10)
        print("Opcion invalida!")
        print("--"*10)