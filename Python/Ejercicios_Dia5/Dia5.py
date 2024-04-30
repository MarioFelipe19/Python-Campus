def primo (num): 
    contador = 2 
    resultado =  True

    while (contador <= num/2 and resultado):
        resultado = num % contador != 0
        contador+= 1
    return resultado
def par(num):
    if num % 2 == 0:
        return "El numero es par"
    else:
        return "El numero es impar"
    
def media(lista):
    suma = 0
    for numero in list:
        suma+= numero
    return suma/len(lista)

def generar_lista():
    cantidad = (int(input("Ingrese cuantos valores desea ingresar")))
    lista = []
    for i in range(cantidad):
        lista.append(int(input("Ingrsese el valor")))
    return lista

def palabra ():
    palabra = (input("ingrese una palabra"))
    return palabra.count ("x") != 0 or palabra.count ("z") != 0



lista = [1,2,3,4,5,6,7]
print(media(lista))
option = int(input("Ingrese un (1) si desea verificar un numero primo,(2) si es  par o impar  (3) para obtener si una letra tiene x o z: "))

print(primo())
print(par())
print(generar_lista())