import math
def calcular(num1,num2):
    while num2 != 0:
        num1 , num2 = num2 , num1 % num2 
    return print(f"El MCD es {num1}")

def calcular(num1,num2):
    r = math.lcm(num1,num2)
    return print(f"El MCD es {r}")

o = int(input("ingrese 1 para Calcular MCD o 2 para Calcular MCM: "))
if o == 1:
    num1 = float(input("ingrese numero 1: "))
    num2 = float(input("ingrese numero 2: "))
    calcular(num1,num2)
elif o == 2:
    num1 = int(input("ingrese numero 1: "))
    num2 = int(input("ingrese numero 2: "))
    calcular(num1,num2)
else:
    print("Opcion ivalida")