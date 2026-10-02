#
hijos = int(input("Cuando hijos tienes"))
edad = int(input("Escribe tu edad"))

def mayor(edad):
    if edad > 18:
        hijos = 0
        return "Es mayor de edad"
    else:
        return "NO, NO es mayor de edad"
    
print(mayor(edad))