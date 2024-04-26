def factorial(num):
    for i in range(num):
        num -= 1
        print(num + 1)
    return(f"Factorial{num}")


num = int(input("ingrese el numero: "))

factorial(num)