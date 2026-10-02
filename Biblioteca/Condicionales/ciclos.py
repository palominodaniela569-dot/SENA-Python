for numero in range(1, 11):

    if numero % 2 == 0:
        print(numero, "es par")
    else:
        print(numero, "es impar")
        
        numero = int(input("Escribe un número: "))

multiplicador = 1

while multiplicador <= 10:
    resultado = numero * multiplicador
    print(numero, "x", multiplicador, "=", resultado)

    multiplicador += 1