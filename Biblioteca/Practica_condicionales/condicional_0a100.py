#Pide al usuario una nota de 0 a 100.

#Si la nota es 90 o más → Excelente
#Si está entre 70 y 89 → Aprobado
#Si está entre 0 y 69 → Reprobado

nota = int(input("Escribe tu nota de 0 a 100: "))

if nota >= 90 and nota <= 100:
    print("Excelente nota")   

elif nota >= 70 and nota <= 89:
    print("Aprobaste, bien pero tienes que ser mejor")

elif nota >= 0 and nota <= 69:
    print("Reprobaste")

else:
    print("ERROR AL COLOCAR LA NOTA")
    