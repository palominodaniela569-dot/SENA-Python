#Si ambos son positivos, muestra Los dos números son positivos
#Si alguno de los dos es negativo, muestra Hay al menos un número negativo
#Si ninguno de los dos es negativo ni positivo, muestra Hay un cero

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

if num1 > 0 and num2 > 0:
    print("El primer y segundo numero son positivos")
    
elif num1 < 0 or num2 < 0:
    print("Hay al menos un numero negativo")

else:
    print("Hay un 0 es neutro")