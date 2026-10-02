#Una cadena es una secuencia de caracteres rodeada por comillas simples o dobles.
# Python trata ambas formas como cadenas, así que puedes usar cualquiera de las
# dos. Aquí tienes algunos ejemplos:
my_str_1 = 'Hello'
my_str_2 = "World"
my_str_3 = """Multiline
string"""
my_str_4 = '''Another
multiline
string'''
#Usa el tipo opuesto de comillas. Es decir, si tu cadena contiene comillas simples
# , usa comillas dobles para envolver la cadena, y viceversa:
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'

#A veces, puede que necesites verificar si una cadena contiene uno o más
# caracteres. Para eso, Python proporciona el operador in, que devuelve un 
# booleano que especifica si el carácter o los caracteres existen en la cadena o no.

my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False
print("l" in my_str)

#Para obtener la longitud de una cadena, puedes usar la función incorporada len().
# Aquí tienes un ejemplo:

my_str = 'Hello world'
print(len(my_str))  # 11

# Cada carácter en una cadena tiene una posición llamada índice. El índice es cero basado, 
##lo que significa que el índice del primer carácter de una cadena es 0, el índice del segundo
#carácter es 1, y así sucesivamente. Para acceder a un carácter por su índice, usas corchetes 
#([]) con el índice del carácter que deseas acceder dentro. Aquí hay algunos ejemplo

my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w

#La indexación negativa también está permitida, por lo que puedes obtener el último carácter 
# de cualquier cadena con -1, el penúltimo carácter con -2, y así sucesivamente:

my_str = 'Hello world'
print(my_str[-1])  # d
print(my_str[-2]) # l

#Puedes apuntar una variable a un nuevo valor, lo que se llama reasignación, pero no puedes cambiar un valor
#inmutable agregando, eliminando o reemplazando alguno de sus elementos.
#Las cadenas son inmutables en Python. Esto significa que puedes reasignar una cadena diferente a una variable:

greeting = 'hi'
greeting = 'hello'
print(greeting) # hello