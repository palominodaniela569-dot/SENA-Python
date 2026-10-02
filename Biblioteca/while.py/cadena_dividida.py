#En una lección anterior, aprendiste cómo cada carácter en una cadena puede ser identificado por su índice 
# (comenzando desde cero) y accedido usando la notación de corchetes:

my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w
print(my_str[-1]) # d

#El corte de cadenas te permite extraer una porción de una cadena o trabajar solo con una parte específica de ella.
# Aquí está la sintaxis básica:


#string[start:stop]

#Si deseas extraer caracteres desde un cierto índice hasta otro, simplemente separa los índices start y stop
# con dos puntos:

my_str = 'Hello world'
print(my_str[1:4]) # ell

#También puedes omitir los índices de start y stop, y Python predeterminadamente tomará 0 o el final
# de la cadena, respectivamente. Por ejemplo, esto es lo que ocurre si omites el índice de start:

my_str = 'Hello world'
print(my_str[:7])  # Hello w

#Esto extrae todo desde el índice 0 hasta (pero sin incluir), el carácter en el índice 7. Y esto es lo 
# que ocurre si omites el índice de stop:

my_str = 'Hello world'
print(my_str[8:])  # rld

#Esto extrae todo desde el carácter en el índice 8 hasta el final de la cadena.

#Ten en cuenta que cortar una cadena no modifica la cadena original:

my_str = 'Hello world'
print(my_str[8:])  # rld
print(my_str)  # Hello world

#También puedes omitir tanto los índices de start como de stop, lo que extraerá toda la cadena:

my_str = 'Hello world'
print(my_str[:])  # Hello world

#Además de los índices start y stop, también existe un parámetro opcional step, que se usa para especificar el incremento entre cada índice en el slice.

#Aquí está la sintaxis para eso:

#string[start:stop:step]

#En el ejemplo a continuación, la división comienza en el índice 0, se detiene antes del 11, y extrae cada segundo 
# carácter:

my_str = 'Hello world'
print(my_str[0:11:2])  # Hlowrd

#Una truco útil que puedes hacer con el parámetro step es invertir una cadena configurando el paso a -1,
# y dejando en blanco start y stop:

my_str = 'Hello world'
print(my_str[::-1]) # dlrow olleH