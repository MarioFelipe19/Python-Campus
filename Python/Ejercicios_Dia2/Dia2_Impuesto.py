edad = int(input("Ingrese su edad:"))
ingre = int(input("Ingrese sus ingresos mensuales:"))
if edad >=16 and ingre >= 1000:
    print(f"El ciudadano con edad de {edad} años y con ingresos de {ingre} 'Tiene' que Tributar")
else:
    print(f"El ciudadano con edad de {edad} años y con ingresos de {ingre} 'NO' Tiene que Tributar")