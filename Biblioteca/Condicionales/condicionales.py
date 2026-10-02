#if → si
#elif → si no, si... / si no, otra condición
#else → si no / de lo contrario


edad = int(input("¿Cuántos años tienes? "))
nivel = int(input("¿Cuál es tu nivel? "))
invitado = input("¿Eres invitado? si/no: ")

if edad >= 16 and nivel >= 5:
    print("Cumples los requisitos")

elif edad >= 16 and invitado == "si":
    print("Puedes entrar como invitado")

else:
    print("No puedes entrar")
