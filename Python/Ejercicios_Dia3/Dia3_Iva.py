def calcular(num, iva = 21):
    r = num * iva / 100
    r2 = num + r
    return print(f" El resultado del {iva} % de iva para la factura es: {r2}")

num = int(input("ingrese el Valor: "))
iva = input("ingrese el Iva: ")


if iva != "":
    calcular(num, int(iva))
else:
    calcular(num)




