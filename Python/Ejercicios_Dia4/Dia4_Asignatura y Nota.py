lista = []
lista2 = []
while True:
    op1 = int(input("ingresar matria 1 buscar materia 2 salir 3: "))
    if op1 == 1:
        while True:
            op = int(input("Quiere ingrsar una materia 1 SI o 2 NO: "))
            if op == 1:
                m = input("ingrese la materia: ")
                n = float(input("ingrese la Nota: "))
                lista.append(m)
                lista2.append(n)
                
            elif op == 2:
                print("Hastaluego")
                break
            else:
                print("Opcion invalida")
    elif op1 == 2:
        print(lista)
        b = int(input("Ingrese la posicion de la materia que empieza desde 0: ")) 
        print("=="*10)
        print(f"En Asignatura {lista[b]} has sacado {lista2[b]}")
        print("=="*10)
    elif op1 == 3:
        print("Adios")
        break
    else:
        print("Opcion invalida")