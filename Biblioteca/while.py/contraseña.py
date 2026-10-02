#Ahora vamos a hacer algo un poquito más real.

#Crea un programa que le pida al usuario una contraseña.

#Mientras la contraseña sea incorrecta, debe seguir preguntándola.

#La contraseña correcta será:

#python123

#Cuando la escriba correctamente, debe mostrar:

#Acceso permitido

contraseña = input("Escribe la contraseña: ")

while contraseña != "python123":
    contraseña = input("Contraseña incorrecta. Inténtalo otra vez: ")

print("Acceso permitido")
