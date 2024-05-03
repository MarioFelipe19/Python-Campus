
divisa =  {
    "Euro":"€", "Dolar":"$", "Yen":"¥"
}

d = input("Ingrese la divisa: ").capitalize()
print(divisa.get(d, "No encotrado"))