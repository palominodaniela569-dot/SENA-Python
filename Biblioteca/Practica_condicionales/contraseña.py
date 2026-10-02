#Pide al usuario una contraseña.

#Si la contraseña es exactamente:

#python123

#muestra:

#Acceso permitido

#si es diferente, muestra:

#Contraseña incorrecta

contraseña = str(input("Escribe tu contraseña: "))
contra = "python123"

if contraseña ==  contra:
    print("ES CORRECTO")

else:
    print("Es incorrecto vuelve a intentarlo")