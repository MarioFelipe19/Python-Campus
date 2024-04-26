
# el parametro b queda definido en 1 si no se le ingresa ningun valor 
def multiplicacion(a, b = 1):
    return  a * b

print(multiplicacion(5,2))
#-------------------------------------
#puedo sustituir un else con otro return
#el parametro definido va de ultimo en la funcion
def Puede_netrar(nombre, edad = 0) :
    if edad < 18:
        return  "No puede entrar" + nombre
    return"Puede entrar" + nombre


print(Puede_netrar("juan", 20))

#------------------------------------------
# Da error por que no los pasa en orden
def Puede_netrar(nombre, edad = 0) :
    if edad < 18:
        return  "No puede entrar" + nombre + str(nombre)
    return"Puede entrar" + nombre + str(nombre)


print(Puede_netrar( 20, "juan"))
#-------------------------------------------
# Funciona por que los parametros estan definidos
def Puede_netrar(nombre, edad = 0) :
    if edad < 18:
        return  "No puede entrar" + nombre + str(nombre)
    return"Puede entrar" + nombre + str(nombre)


print(Puede_netrar( edad = 20, nombre = "juan"))
#-------------------------------------
# subfuncion 

def outer(x):
    def inner(y):
        return x + y 
    return inner

add_num = outer(10)

print(add_num)

#----------------------------
#demustra las variables locales y globales 
def saludar():
    saludo = "hoal a todos"
    return saludar

saludo = " hola a la clase"
print(saludo)
saludar()
print(saludo)

#----------------------------------
#