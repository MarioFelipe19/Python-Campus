#funcion predefinida
print("hola mundo")
#-------------------------------------
#fincion type = sierve para ver el tipo de dato
x1 = 6
print (type(x1))
x2 = 9.8
print (type(x2))
x3 = True
print (type(x3))
x4 = "Hola"
print (type(x4))
#------------------------------------
#toma la parte entera
print (int(x2))
#-----------------------------------
#cadenas, puedo usar comillas dobles o sencillas 
mi_cadena = "Bienvenido"
print (mi_cadena)
mi_cadena = 'Bienvenidos'
print (mi_cadena)

mi_cadena = 'Bienvenidos\' campus'
print (mi_cadena)
#--------------------------------------
# formato para una cadena
n = 5
n2 = 10
mi_cadena2 = f"los numeros son {n} y {n2}"
print(mi_cadena2)
#---------------------------------------
#concateancion
c1 = "hola"
c2 = "mundo"
resultado = c1 + "" + c2
print(resultado)
#------------------------------------
#octener la logitud
c3 = "hola"
cantidad = len(c3)
print(cantidad)
#-----------------------------------
#acceso a caracteres individuales 
cade = "Esto es una cadena"
p_cadena = cade[0]
print(p_cadena)
#-----------------------------------
#sud candena va desde el primer numero y el ultimo -1
c4 = "Bienvenido"
sud = c4[4:6]
print(sud)

# el ultimo numero funciona para dar pasos en el arreglo  
mi = "Bienvenido"
mi_sub = mi[0:8:2]

mi2 = "Bienvenido"
mi2_sub = mi2[::-1]
print(mi2_sub)
#--------------------------
#Busqueda y reemplazo
cadena = "Esto es una cadena"
indice = cadena.find("cadena")
nueva_cadena = cadena.replace("cadena","_____")
#-----------------------------------
#coversion de mayusculas y minusculas
cade1 = "hola mundo"
mayuscula = cade1.upper()
minuscula = cade1.lower()
primeraMayuscula= cade1.capitalize()
titulada = cade1.title()

print(mayuscula)
print(minuscula)
print(primeraMayuscula)
print(titulada)

#----------------------------------
#separecion y union de caracteres
cade2 = "hola, como, esta"
sub2 = cade2.split(",")
nueva2 = "-".join(sub2)

print(sub2)
print(nueva2)
