def calcular(o,radio,altura):
    if o == 1:
        r = 3.14 * (radio**2)
        return print(f" El resultado deL area con radio {radio} del Circulo es: {r}")
    else:
        volumen = 3.14 * (radio**2) * altura
        return print(f" El resultado con radio {radio} y  altuara {altura} del volumen del cilidro  es: {volumen}")


o = int(input("ingrese 1 para Calcular Area o 2 para Calcular Volumen : "))
if o == 1:
    radio = float(input("ingrese el Valor radio: "))
    calcular(o,radio,altura = 0)
elif o == 2:
    radio = float(input("ingrese el Valor radio: "))
    altura = float(input("ingrese el volumen del cilindro Valor altura: "))
    calcular(o,radio,altura)
else:
    print("Opcion ivalida")
