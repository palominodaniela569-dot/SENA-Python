#Habrá momentos en tu programa en los que necesites verificar que una variable
# en particular sea de un tipo específico antes de realizar operaciones sobre 
#ella. Aquí es donde la función isinstance() resulta útil.

#Si intentas realizar operaciones matemáticas como la división
#usando la variable account_balance, recibirás un mensaje de error


account_balance = '12'

print(isinstance(account_balance, int)) # False

#La función integrada isinstance() te permite verificar si una variable
# coincide con un tipo de dato específico. Toma un valor y el tipo contra 
# el que quieres comprobarlo, y luego devuelve un booleano. En este caso,
# como account_balance es una cadena, devolverá False.


#Aquí tienes un ejemplo verificando si account_balance es un int o float:
account_balance = 12
print(isinstance(account_balance, (int, float))) # True