#En Python, puedes combinar múltiples cadenas juntas con el operador más (+). Este proceso se llama concatenación 
# de cadenas. Aquí te mostramos cómo concatenar dos cadenas con el operador más:

my_str_1 = "Hello"
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World

#Repetir cadenas
#También puedes repetir una cadena multiplicándola por un entero usando el operador *.
# La cadena se repite el número especificado de veces:

sound = 'ha'
repeated_sound = sound * 100
print(repeated_sound) # hahaha

#Concatenar cadenas con números
#La concatenación solo funciona con cadenas. Si intentas concatenar una cadena con un número, 
#obtendrás un TypeError:
name = 'John Doe'
age = 26

#name_and_age = name + age
#print(name_and_age) # TypeError: can only concatenate str (not "int") to str


#python requiere que todos los elementos sean cadenas antes de poder concatenarlos. 
# Para solucionar eso, puedes convertir el número en una cadena con la función integrada str()
name = 'John Doe'
age = 26

name_and_age = name + str(age)
print(name_and_age) # John Doe26

#También puedes usar el operador de asignación aumentada para la concatenación. 
# Este se representa con un más y un signo igual (+=), y realiza tanto la concatenación
# como la asignación en un solo paso. Aquí tienes cómo funciona:

name = 'John Doe'
age = 26

name_and_age = name  # Start with the name
name_and_age += str(age)  # Append the age as string

print(name_and_age)  # John Doe26

nombre = "Ivan"
edad = "16"

id = nombre
id += str(edad)
print (id)