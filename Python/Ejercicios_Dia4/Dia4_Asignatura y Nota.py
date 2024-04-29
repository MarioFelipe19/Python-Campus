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
        b = input("ingrese la materia: ")
        
        if  lista.find(b) ==  1:
            for i in lista and lista2:
                
                print("=="*10)
                print(f"En Asignatura{lista[i]} has sacado{lista2[i]}")
                print("=="*10)
        else:
            print("materia incorrecta")
    elif op1 == 3:
        break
    else:
        print("Opcion invalida")