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
#---------------------------------------
#Repetición (*)
#La repetición se utiliza para repetir una cadena un número específico de veces.
cadena = "Hola"
cadena_repetida = cadena * 3
print(cadena_repetida)  # Salida: HolaHolaHola
#------------------------------------------
#Pertenencia (in)
#El operador in comprueba si una subcadena está contenida dentro de una cadena. Devuelve True si la subcadena se encuentra en la cadena, y False en caso contrario.
cadena = "Hola, mundo"
subcadena = "mundo"

if subcadena in cadena:
    print("La subcadena", subcadena, "está contenida en la cadena", cadena)
else:
    print("La subcadena", subcadena, "no está contenida en la cadena", cadena)
#-------------------------------------------
# Igualdad (==)
#El operador == compara si dos cadenas son iguales. Devuelve True si las cadenas son exactamente iguales, y False en caso contrario. 
cadena1 = "Hola mundo"
cadena2 = "Hola mundo"

if cadena1 == cadena2:
    print("Las cadenas", cadena1, "y", cadena2, "son iguales")
else:
    print("Las cadenas", cadena1, "y", cadena2, "no son iguales")
#--------------------------------------------
#Diferencia (!=)
#El operador != compara si dos cadenas son diferentes. Devuelve True si las cadenas no son exactamente iguales, y False en caso contrario. Es lo opuesto al operador ==.
cadena1 = "Hola mundo"
cadena2 = "Adiós mundo"

if cadena1 != cadena2:
    print("Las cadenas", cadena1, "y", cadena2, "son diferentes")
else:
    print("Las cadenas", cadena1, "y", cadena2, "son iguales")
#------------------------------------
# Nota: Es importante recordar que la comparación de cadenas en Python es sensible a las mayúsculas. Si deseas comparar cadenas sin tener en cuenta las mayúsculas, puedes utilizar el método lower() para convertir ambas cadenas a minúsculas antes de la comparación:
cadena1 = "HOLA MUNDO"
cadena2 = "hola mundo"

if cadena1.lower() == cadena2.lower():
    print("Las cadenas", cadena1, "y", cadena2, "son iguales (ignorando mayúsculas)")
else:
    print("Las cadenas", cadena1, "y", cadena2, "no son iguales (ignorando mayúsculas)")
#-----------------------------------------------------------------
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
#cadena.find(subcadena): devuelve el índice de la primera aparición de subcadena.
#retorna -1 cuando el argumento no es encontrado
indice = cadena.find("cadena")
nueva_cadena = cadena.replace("cadena","_____")
#-----------------------------------
#----------------------------------
#cadena.strip():
# elimina los espacios en blanco al principio y al final de la cadena.
adena = "   ¡Hola, mundo!   "
cadena_limpia = cadena.strip()
print(cadena_limpia)  # Esto imprimirá "¡Hola, mundo!"
#----------------------------------------
#cadena.index(subcadena)
# similar a find(), pero lanza una excepción si no se encuentra la subcadena. lanza un error ValueError
cadena = "Hola mundo"
indice = cadena.index("mundo")
print(indice)  # Esto imprimirá 5, que es el índice donde comienza "mundo" en la cadena.
#--------------------------------------------
#cadena.startswith(prefijo)
# devuelve True si la cadena comienza con el prefijo dado.
cadena = "Hola mundo"

# Verificar si la cadena comienza con el prefijo "Hola":
print(cadena.startswith("Hola"))  # Esto imprimirá True

# Verificar si la cadena comienza con el prefijo "mundo":
print(cadena.startswith("mundo"))  # Esto imprimirá False
#----------------------------------------------
#cadena.endswith(sufijo)
#: devuelve True si la cadena termina con el sufijo dado.
cadena = "Hola mundo"

# Verificar si la cadena termina con el sufijo "mundo":
print(cadena.endswith("mundo"))  # Esto imprimirá True

# Verificar si la cadena termina con el sufijo "Hola":
print(cadena.endswith("Hola"))  # Esto imprimirá False
#-----------------------------------------------
#coversion de mayusculas y minusculas
cade1 = "hola mundo"
#cadena.upper(): convierte la cadena a mayúsculas.
mayuscula = cade1.upper()
#cadena.lower(): convierte la cadena a minúsculas.
minuscula = cade1.lower()
#cadena.capitalize(): convierte la primera letra de la cadena a mayúscula.
primeraMayuscula= cade1.capitalize()
#cadena.title(): convierte la primera letra de cada palabra a mayúscula.
titulada = cade1.title()

print(mayuscula)
print(minuscula)
print(primeraMayuscula)
print(titulada)

#----------------------------------
#separecion y union de caracteres
cade2 = "hola, como, esta"
#cadena.split(delimitador): divide la cadena en una lista de subcadenas utilizando delimitador.
sub2 = cade2.split(",")
#Utilizando el método str.join(): " ".join(["Hola", "mundo"])
nueva2 = "-".join(sub2)

print(sub2)
print(nueva2)
#------------------------------
# count(): Retorna el número de veces que se repite un conjunto de caracteres especificado. Por ejemplo:
s = "Hola mundo"
print(s.count("Hola"))  # Salida: 1
#-------------------------------
#cadena.isdigit()
#: devuelve True si la cadena contiene solo dígitos.
cadena1 = "12345"
print(cadena1.isdigit())  # Esto imprimirá True, ya que todos los caracteres son dígitos.

cadena2 = "abc123"
print(cadena2.isdigit())  # Esto imprimirá False, ya que la cadena contiene caracteres que no son dígitos.

cadena3 = ""
print(cadena3.isdigit())  # Esto imprimirá False, ya que la cadena está vacía.

#isnumeric():
#Devuelve True si todos los caracteres de la cadena son numéricos y la cadena no está vacía.
#Acepta subíndices y dígitos numéricos (incluyendo números romanos).
#Puede ser más amplio que isdigit() en términos de los caracteres que acepta como numéricos.

#isdecimal():
#Devuelve True si todos los caracteres de la cadena son dígitos y la cadena no está vacía.
#Acepta solo caracteres que están en la categoría de "dígitos decimales" (es decir, los dígitos del 0 al 9).
#Es más estricto que isdigit() y isnumeric() en cuanto a los caracteres aceptados.

cadena1 = "12345"
cadena2 = "²3455"
cadena3 = "½3455"
cadena4 = "१२३४५"
cadena5 = "12345"

print(cadena1.isdigit())    # True
print(cadena1.isnumeric())  # True
print(cadena1.isdecimal())  # True

print(cadena2.isdigit())    # True
print(cadena2.isnumeric())  # True
print(cadena2.isdecimal())  # False

print(cadena3.isdigit())    # False
print(cadena3.isnumeric())  # True
print(cadena3.isdecimal())  # False

print(cadena4.isdigit())    # True
print(cadena4.isnumeric())  # True
print(cadena4.isdecimal())  # False

print(cadena5.isdigit())    # True
print(cadena5.isnumeric())  # True
print(cadena5.isdecimal())  # True
#-------------------------------------
#isalnum()
#l método cadena.isalnum() en Python se utiliza para verificar si todos los caracteres de una cadena son alfanuméricos, es decir, si son letras (mayúsculas o minúsculas) o números. Devuelve True si todos los caracteres de la cadena son alfanuméricos y la cadena no está vacía; de lo contrario, devuelve False.
cadena1 = "Hola123"
cadena2 = "Hola mundo"
cadena3 = "12345"
cadena4 = "¡Hola123!"

print(cadena1.isalnum())  # Esto imprimirá True, ya que todos los caracteres son alfanuméricos.
print(cadena2.isalnum())  # Esto imprimirá False, ya que hay espacios en la cadena.
print(cadena3.isalnum())  # Esto imprimirá True, ya que todos los caracteres son dígitos.
print(cadena4.isalnum())  # Esto imprimirá False, ya que hay un signo de exclamación en la cadena.
#----------------------------------------
#isalpha()
#El método cadena.isalpha() en Python se utiliza para verificar si todos los caracteres de una cadena son letras del alfabeto (ya sea en mayúsculas o minúsculas). Devuelve True si todos los caracteres de la cadena son letras y la cadena no está vacía; de lo contrario, devuelve False.
cadena1 = "Hola"
cadena2 = "Hola123"
cadena3 = "12345"
cadena4 = ""

print(cadena1.isalpha())  # Esto imprimirá True, ya que todos los caracteres son letras.
print(cadena2.isalpha())  # Esto imprimirá False, ya que la cadena contiene números además de letras.
print(cadena3.isalpha())  # Esto imprimirá False, ya que la cadena contiene solo números.
print(cadena4.isalpha())  # Esto imprimirá False, ya que la cadena está vacía.
#------------------------------------------
#islower()
#El método cadena.isalpha() en Python se utiliza para verificar si todos los caracteres de una cadena son letras del alfabeto (ya sea en mayúsculas o minúsculas). Devuelve True si todos los caracteres de la cadena son letras y la cadena no está vacía; de lo contrario, devuelve False.
cadena1 = "Hola"
cadena2 = "Hola123"
cadena3 = "12345"
cadena4 = ""

print(cadena1.isalpha())  # Esto imprimirá True, ya que todos los caracteres son letras.
print(cadena2.isalpha())  # Esto imprimirá False, ya que la cadena contiene números además de letras.
print(cadena3.isalpha())  # Esto imprimirá False, ya que la cadena contiene solo números.
print(cadena4.isalpha())  # Esto imprimirá False, ya que la cadena está vacía.
#--------------------------------------------
#isupper()
#El método cadena.isupper() en Python se utiliza para verificar si todos los caracteres alfabéticos de una cadena están en mayúsculas. Devuelve True si todos los caracteres alfabéticos de la cadena están en mayúsculas y la cadena contiene al menos un carácter alfabético; de lo contrario, devuelve False.

cadena1 = "HOLA"
cadena2 = "Hola"
cadena3 = "12345"

print(cadena1.isupper())  # Esto imprimirá True, ya que todos los caracteres están en mayúsculas.
print(cadena2.isupper())  # Esto imprimirá False, ya que hay letras en minúscula.
print(cadena3.isupper())  # Esto imprimirá False, ya que la cadena no contiene caracteres alfabéticos.
#-------------------------------------------
#isprintable()
#El método cadena.isprintable() en Python se utiliza para verificar si todos los caracteres de una cadena son imprimibles. Devuelve True si todos los caracteres de la cadena son imprimibles, es decir, si no son caracteres de control como saltos de línea o tabulaciones; de lo contrario, devuelve False.

cadena1 = "Hola mundo!"
cadena2 = "Hola\nmundo!"

print(cadena1.isprintable())  # Esto imprimirá True, ya que todos los caracteres son imprimibles.
print(cadena2.isprintable())  # Esto imprimirá False, ya que la cadena contiene un salto de línea.
#-------------------------------------------
#isspace()
#El método cadena.isspace() en Python se utiliza para verificar si todos los caracteres de una cadena son espacios en blanco. Devuelve True si todos los caracteres de la cadena son espacios en blanco y la cadena no está vacía; de lo contrario, devuelve False.
cadena1 = "   "
cadena2 = "Hola mundo"
cadena3 = "    \t\t\n"

print(cadena1.isspace())  # Esto imprimirá True, ya que todos los caracteres son espacios en blanco.
print(cadena2.isspace())  # Esto imprimirá False, ya que la cadena contiene letras además de espacios en blanco.
print(cadena3.isspace())  # Esto imprimirá True, ya que todos los caracteres son espacios en blanco o caracteres de control como tabulaciones o saltos de línea.
#---------------------------------------
#El método cadena.encode(encoding) en Python se utiliza para codificar una cadena en una secuencia de bytes utilizando una codificación de caracteres específica. El parámetro encoding especifica la codificación que se utilizará para la conversión. Devuelve un objeto de tipo bytes que representa la cadena codificada.

cadena = "Hola mundo"
cadena_codificada = cadena.encode("utf-8")
print(cadena_codificada)  # Esto imprimirá b'Hola mundo', una representación en bytes de la cadena codificada en UTF-8.

#El método bytes.decode(encoding) en Python se utiliza para decodificar una secuencia de bytes en una cadena utilizando una codificación de caracteres específica. El parámetro encoding especifica la codificación que se utilizará para la conversión. Devuelve una cadena que representa la secuencia de bytes decodificada.

bytes_codificados = b'Hola mundo'
cadena_decodificada = bytes_codificados.decode("utf-8")
print(cadena_decodificada)  # Esto imprimirá 'Hola mundo', la cadena decodificada a partir de la secuencia de bytes utilizando UTF-8.
