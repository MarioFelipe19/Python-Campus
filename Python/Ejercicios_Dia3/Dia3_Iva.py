def calcular(num, iva = 21):
    r = num * iva / 100
    r2 = num - r
    return print(f" El resultado del {iva} % de iva para la factura es: {r2}")

num = int(input("ingrese el numero: "))
iva = int(input("ingrese el numero: "))


calcular(num)
calcular(num, iva  )




