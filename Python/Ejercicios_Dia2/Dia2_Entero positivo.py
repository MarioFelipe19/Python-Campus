num = int(input("Ingrese el numero: "))

lista = []
i = 1
for i  in range(num + 1):
    if i % 2 == 1:
        lista.append(i)
print(f"Los numero impares son {lista}" )
        