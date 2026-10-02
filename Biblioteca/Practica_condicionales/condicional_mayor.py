#Pide al usuario dos números.

#Si el primero es mayor que el segundo, muestra El primer número es mayor.
#Si el segundo es mayor que el primero, muestra El segundo número es mayor.
#Si son iguales, muestra Los números son iguales.

a = int(input(" Ingresa el primer numero: "))
b = int(input(" Ingresa el segundo numero: "))

if a > b:
    print("El primer numero es mayor")

elif b > a:
    print("El segundo numero es mayor")
    
else:
    print("Son iguales")