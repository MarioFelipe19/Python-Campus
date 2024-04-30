lista = []
lista2 = []
while True:
    op1 = int(input("ingresar matria 1  salir 2: "))
    if op1 == 1:
        while True:
            op = int(input("Quiere ingrsar una materia 1 SI o 2 NO: "))
            if op == 1:
                m = input("ingrese la materia: ")
                n = float(input("ingrese la Nota: "))
                if n >= 3:
                    lista.remove(m)
                    lista2.remove(n)
                else:
                    lista.append(m)
                    lista.append(n)
            elif op == 2:
                print("Hastaluego")
                break
            else:
                print("Opcion invalida")
        for i in lista:
            print("=="*10)
            print(f"En Asignatura {lista[i]} has sacado ")
            print("=="*10)
    elif op1 == 2:
        print("Adios")
        break
    else:
        print("Opcion invalida")