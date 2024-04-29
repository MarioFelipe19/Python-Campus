num = int(input("Ingrese el numero: "))
lista = [num]
i = 1
for i in range(num):
    if num != 0:
        num -=1
        lista.append(num)
print(f"el numero inverso es {lista}")