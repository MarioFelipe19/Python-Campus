edad = int(input("Ingrese la edad: "))

if edad < 4:
    print("Entra gratis")
if edad > 4 and edad < 18:
    print("Debe pagar 5 euros")
if edad > 18:
    print("Debe pagar 10")