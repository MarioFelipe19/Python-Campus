nom = str.lower(input("Ingrse su Nombre:"))
sex = str(input("Ingrse su sexo:"))
lista = ["a","b","c","d","e","f","g","h","i","j","k","l"]

for i in range(len(lista)):
    if nom[0] == lista[i]:
        print("Es del grupo A")
        break
    else:
        print("Es del grupo N")
        break