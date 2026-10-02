#Pide al usuario su edad y dile el precio de una entrada:

#Menor de 12 años → $5
#De 12 a 17 años → $8
#De 18 años o más → $12

edad = int(input("Escribe tu edad"))

if edad < 12:
    print("La entrada vale $5")
    
elif edad >= 12 and edad <= 17:
    print("La entrada vale 8$")
    
else:
    print("Ya que eres mayor de edad te vale $12 la entrada")
    