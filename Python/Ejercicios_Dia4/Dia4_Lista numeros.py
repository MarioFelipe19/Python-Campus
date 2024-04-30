lista = []
while True: 
    num = input("ingrse el numero o una letra parafinalizar la ejecucion: ")
    if num.isnumeric():
        lista.append(int(num))
    if num.isnumeric() == False:
        break
lista.sort(reverse=True)
print(f"la lista es {lista}")


