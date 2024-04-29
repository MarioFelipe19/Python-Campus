
lista = []

while True:
    op = int(input("Quiere ingrsar una materia 1 SI o 2 NO: "))
    if op == 1:
        m = input("ingrese la materia: ")
        lista.append(m)
        print(lista)
    elif op == 2:
        print("Hastaluego")
        break
    else:
        print("Opcion invalida")



