#Funcion sencilla SIN ARGUMENTO

def saludo():
    nombre = str(input("¿Como te llamas?: "))
    
    edad = int(input("¿Cuantos años tienes?: "))
    
    sitio = input ("¿Donde vives?:  ")
    print(f" hola mi querido {nombre.upper()},Tienes {edad} !! y tambien vives en {sitio} wow!! 👌👌")
    
    
#Termino la funcion

#LLAMAMOS LA FUNCION
saludo()

