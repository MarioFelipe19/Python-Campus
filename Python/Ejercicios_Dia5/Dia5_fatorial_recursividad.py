# la funcion se llama a ella misma
def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    else:
        return num

print(factorial(5))
