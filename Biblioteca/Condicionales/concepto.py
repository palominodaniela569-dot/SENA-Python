#execelnte aprobado o reprobado 90 pa arriba exelente de setenta pa abajo es reprobado

def sumar_lista(numeros):
    total = 0
    for num in numeros:
        total += num
    return total


notas = [0, 0, 0, 50]#Esto es una lista
total = sumar_lista(notas)
print(total)
