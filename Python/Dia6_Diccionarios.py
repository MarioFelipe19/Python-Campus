#Diccionario
persona = {
    "nombre":"Adrian",
    "edad": 20,
    "es estudiante": True,
    "hobbies" : ["caminar","Leer","Estudiar"],
    "mejor amigo" : {"nombre": "Luis Nicolaas" ,"edad": 18, "es estudiante": False}

}

print(persona)
print(persona["mejor amigo"])
print(persona["mejor amigo"]["nombre"])

#--------------------------------------------
#recorrer lista con diccionario
paises = [{"nombre": "colombia", "poblacion":50000000},{"nombre":"venezuela","poblacion":49000000}]

for i in paises:
    print(i["nombre"])
print(paises[0]["nombre"])

for i in paises:
    print(i)
    print(paises[i])
#-------------------------------------------
#Fucion Get
#puedo octener valor, si el valor no existe va regresar -1
paises = [{"nombre": "colombia", "poblacion":50000000},{"nombre":"venezuela","poblacion":49000000}]

for i in paises:
    print(i["nombre"])
print(paises[0]["nombre"])
print(paises[0].get("idioma"))




