# #Funcion con argumentos y retornos de datos

# def sumar(a,b):
#     resultado = a+b
#     return resultado

# #toda funcion devuelve un resultado
# #LLAMO LA FUNCION
# total = sumar(1,5)
# print(total)

# print(sumar(2,3)) #

#----------------------------

#solito clave que ternga bien claro que es una variable local o global
#crear una funcion no se pude dividir entre 0 restar multiplicar y dividir

a = int(input("\nEscribe tu primer número: "))
b = int(input("Escribe tu segundo número: "))

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

print("Suma:", sumar(a, b))
print("Resta:", restar(a, b))
print("Multiplicación:", multiplicar(a, b))

if b == 0:  
    print ("No se puede dividir entre 0")
else:
        print("División:", dividir(a, b))
    
    
