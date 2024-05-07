def menu():
    print("==" * 10)
    print("Ingrese la opcion: ")
    print("1. Registrar empleados")
    print("2. Modificar empleados")
    print("3. Despedir empleados (")
    print("4. Registrar entrada empleados")
    print("5. Registrar salida de empleados")
    print("==" * 10)

    def opcion():
        return int(input("Ingrese la opcion: "))