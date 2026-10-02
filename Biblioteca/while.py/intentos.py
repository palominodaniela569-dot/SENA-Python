contraseña = ""
intentos = 0

while contraseña != "python123" and intentos < 3:
    contraseña = input("Escribe la contraseña: ")
    intentos = intentos + 1

    if contraseña != "python123":
        print("Contraseña incorrecta")
        print("Te quedan", 3 - intentos, "intentos")

if contraseña == "python123":
    print("Acceso permitido")
else:
    print("Has agotado los intentos")