def ordenar(o,cadena):

    if o == 1:
        r = len(cadena)
        return print(f"El tamaño de la caden es: {r}")
    elif o == 2:
        return print(f"La caden en Mayuscula es: {[cadena2.upper() for cadena2 in cadena]}")
    elif o == 3:
        return print(f"La caden en Minuscula es: {[cadena2.lower() for cadena2 in cadena]}")
    elif o == 4:
        r = cadena[::-1]
        return print(f"La cadena invertida es: {r}")
    elif o == 5: 
        cadena2 = len(cadena) // 2
        return print(f"La segunda Mitad es: {cadena[cadena2:]}")

cadena = []

while True:
    c = input("ingrese la letra o un numero  para terminar la ejecucion: ")
    if c.isalpha():
        cadena.append(c) 
    print(cadena)
    if c.isalpha() == False:
        break
    
o = int(input("ingrese 1: Tamayo 2: Mayuscula 3: Minuscula 4: Invertida 5: Segunda Mitad "))
if o > 0 and o <= 5:
    ordenar(o,cadena)
else:
    print("Opcion ivalida")