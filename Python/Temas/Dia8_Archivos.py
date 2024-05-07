file = open("archivo.txt")
print(file.read)
file.close()
#-----------------------------
#leer una linea 
file = open("archivo.txt")
print(type(file.readline))
file.close()

#--------------------------
#lista con las lienas 
file = open("archivo.txt")
print(type(file.readlines))
file.close()

