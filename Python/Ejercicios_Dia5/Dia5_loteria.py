con =  {"telefono","table","tv","labadora","carro","moto"}
while len(con) != 0:
    t = int(input("ingrese el 1 para ganar un premio: "))
    if t == 1:
        print("=="*10)
        print(f"Ganaste un: {con.pop()}")    
        print("=="*10)
    else:
        print("opcion invalida")
print("NO hay mas premios")
        