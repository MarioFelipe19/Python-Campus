canti = int(input("Ingrse la cantidad a invertir: "))
inte = int(input("Ingrse el interes anual: "))
años = int(input("Ingrse el numero de años: "))

for i in range(años):
    r = (canti * inte) / 100
    canti += r
    print(f"en el año {años} se gano un papital de {canti}")
