#importar del archivo calculadora 
import Calculadora

print(Calculadora.sumar(3,5))

#------------------------------------
#traer funciones especificas 
from Calculadora import sumar, restar

print(sumar(3,5))
print(restar(3,5))


#-------------------------------
#importar todo

from Calculadora import *
print(sumar(3,5))
print(restar(3,5))

#----------------------
# colocar alias, el modulos. es la carpeta donde se encuentra 
from modulos.calculadora import sumar as suma, IVA as impuesto

print(suma(3,5))
print(impuesto(3,5))