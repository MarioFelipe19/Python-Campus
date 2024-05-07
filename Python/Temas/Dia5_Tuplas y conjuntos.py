mi_lista = [1,2,3,4]
mi_lista.append(2)

#las tuplas no son modificalbles son reasicnables 
mi_lista = [3,5,6,7,9]

mi_tupla = tuple(mi_lista)
print(type(mi_tupla))
#lista dentro de otra lista 
mi_tabla = [[1,2,3],[4,5,6],[7,8,9]]
print(mi_tabla[1][1])

#Agregar elementos
mi_tabla = [[1,2,3],[4,5,6],[7,8,9]]
mi_tabla[1].append(7)
print(mi_tabla[1][1])

#iterar tupla
mi_tupla = (1,2,3,4,5,6)
for i in mi_tupla:
    print(i)

#conjuntos
#tambien se puede crearlo con "set"
#no puede tener elementos repetidos
# se recorre como los demas con "for"
mi_conjunto = {1,2,3,4}
print(type(mi_conjunto))

mi_conjunto = set([2,4,56,7,8,9])
print(mi_conjunto)

#combertir en lista
mi_lista = list(mi_conjunto)
print(mi_lista)

#añadir al conjunto se usa "add"




