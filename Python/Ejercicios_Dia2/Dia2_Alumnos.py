nom = str.lower(input("Ingrse su Nombre: "))
sex = str.lower(input("Ingrse su sexo M o F: "))
lista = ["a","b","c","d","e","f","g","h","i","j","k","l"]
lista2 = ["o","p","q","r","s","t","u","v","w","x","y","z"]

gru = "B"

for i in lista:
    if i == nom[0]  and sex == "f":
        gru = "A"
for i in lista2: 
    if i == nom[0] and sex == "m" :
        gru = "A"

print(f"El estudiante {nom} es del grupo: {gru}")






