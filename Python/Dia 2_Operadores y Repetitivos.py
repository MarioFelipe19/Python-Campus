# Ejemplos de conversión con bool()

valor1 = 1
valor2 = 0
valor3 = "Hola"
valor4 = ""
valor5 = []
valor6 = {}

resultado1 = bool(valor1)  # True
resultado2 = bool(valor2)  # False
resultado3 = bool(valor3)  # True
resultado4 = bool(valor4)  # False
resultado5 = bool(valor5)  # False
resultado6 = bool(valor6)  # False

print(f"bool({valor1}) = {resultado1}")
print(f"bool({valor2}) = {resultado2}")
print(f"bool({valor3}) = {resultado3}")
print(f"bool({valor4}) = {resultado4}")
print(f"bool({valor5}) = {resultado5}")
print(f"bool({valor6}) = {resultado6}")

#condicion if

edad = 15
if  edad < 18:
    print("Es menor a 18")
    print("Esto tambien")
else:
    print("Es mayor de edad")
print("Esto esta por fuera del if")

#Operador ternario

puede_entrar = None

puede_entrar =  True if edad >= 18 else False
print(puede_entrar)

# While

numero = 0

while numero <= 10:
    print(numero)
    numero += 1

# do while

numero = 0

while True:
    print(numero)
    numero += 1
    if numero > 10:
        break

#For

for i in range(5):
    print(i)

for i in range(2,8):
    print(i)

for i in range(2,8,2):
    print(i)
