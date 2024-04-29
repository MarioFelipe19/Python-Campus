#agrgar elementos
dulces = ["barrilete","chocolatina","mani cubireto"]
print(type(dulces))
print(dulces)
dulces.append("chicle")
print(dulces)

#------------------------------------------------------
#aumentar lista
dulces = ["barrilete","chocolatina","mani cubireto"]
dulce2 = ["nucita","bon bon bum"]
print(type(dulces))
print(dulces)
dulces.append("chicle")
print(dulces)
#Concatena las listas,las une 
dulces.extend(dulce2)
print(dulces)
#Busco el elemento
print(dulces[1])
#Remplazo el elmento
dulces[1] = "Fruna"
print(dulces)
#Isertar elemento
dulces.insert(2, "malteada")
#Eliminar el primer elemento que encuentra 
dulces.remove("chocolatina")
#Eliminar el elemento en una posicion dada y tambien lo devuelve, si no se el pasa valores devuelve el ultimo balor 
dulces.pop(2)
#Eliminar todos los elementos de la lista 
dulces.clear()
#Me cuenta cuantos elementos hay 
dulces.count("nucita")
#Oredenar la lista
dulces.sort()
#Revertir el orden 
dulces.reverse()
#Verificar si un elemento es verdadero
any(dulces)
#Hacer copia de una lista
dulces2 = dulces.copy()
#Recorrer lista 
for i in dulces:
    print(i)
#Recorrer por elemento 
for i in range(len(dulces)):
    print(dulces[i])
for i in range(len(dulces)):
    print(i ,"->",dulces[i])
#Leer alrevez la lista
for i in range(len(dulces)-1,-1,-1):
    print(i ,"->",dulces[i])


