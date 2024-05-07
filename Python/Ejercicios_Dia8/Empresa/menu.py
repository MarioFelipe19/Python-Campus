def menu():
    print("==" * 10)
    print("Ingrese la opcion: ")
    print("1. Registrar empleados")
    print("2. Listar empleados")
    print("3. Modificar empleados")
    print("4. Despedir empleados (")
    print("5. Registrar entrada empleados")
    print("6. Registrar salida de empleados")
    print("7. Para salir")
    print("==" * 10)

    def opcion():
        return int(input("Ingrese la opcion: "))