from datos import *


def masempleados():

    for i in Empresas:
        for j in Empresas.get(i):
                if j["departamento"] == "Recursos Humanos" and j["empleados"] > 10:
                    print(i, " ", j["empleados"])

def promedioempleados():
    v = 0
    for i in Empresas:
        for j in Empresas.get(i): 
            
            print(v)
    

def dobleempleados():
    return print("hola3")

def reorganizar():
    return print("hola4")

