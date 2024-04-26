def primos(valor):
    a = True
    for i in range(int(valor/2)):
        if (i > 1 and a):
            a = valor % i != 0 
    return a

print(primos(int(input("ingrese el numero: "))))