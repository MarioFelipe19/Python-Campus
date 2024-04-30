lista = []
lista2 = []
while True:
    op1 = int(input("ingresar matria 1  Materia a reoetir 2   salir 3: "))
    if op1 == 1:
        while True:
            op = int(input("Quiere ingrsar una materia 1 SI o 2 NO: "))
            if op == 1:
                m = input("ingrese la materia: ")
                n = float(input("ingrese la Nota: "))
                lista.append(m)
                lista2.append(n)
            elif op == 2:
                break
            else:
                print("Opcion invalida")
    elif op1 == 2:
        for i in range(len(lista2)):
            if lista2[i] >= 3 :
                lista.remove(i)
                lista2.remove(i) 
        for i in range(len(lista)):
            print("=="*10)
            print(f"En Asignatura {lista[i]} has sacado {lista2[i]} Tiene que repetir")
            print("=="*10)
    elif op1 == 3:
        print("Adios")
        break
    else:
        print("Opcion invalida")