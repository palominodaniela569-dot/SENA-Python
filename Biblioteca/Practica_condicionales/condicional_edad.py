edad = int(input("Escribe tu edad"))

if edad >= 18:
    print("Eres adulto")
    
elif edad <= 17 and edad >= 13:
    print("eres adolescente")
    
else:
    print("Eres niño")