nota = int(input("Digite su nota: "))
def mayor(nota):
    if nota >= 90:
        return "Tu nota es excelente "
    elif nota <= 60:
        return "Reprobado"
    else:
        return "APROBASTE"
    
print(mayor(nota))