# Ahora veremos como funciona el Scope(Alcance de las variables)
# La variables tienen un ciclo de vida y esto va a depender 
# de manera de donde se encuentren por ejemplo
# Una varible definida dentro de una función no tiene el mismo
# tiempo de vida que una variable fuera de una función

externa = "EXTERNA" # Variable global

def alcance(parametro): # Variable interna 
    interna = "INTERNA"  # Variable interna 
   #probemos el alcance de cada variable dentro de la función
    print("Adentro de la función", externa, parametro, interna) 
alcance("parametro")
#Este error en la siguiente linea significa que las variables parametro e interna
#ya no existen o no son visibles desde afuera de la función
#Con la finalidad de ahorrar espacio en memoria
print("Adentro de la función", externa, parametro, interna) # Vemos que las 
#variables no son reconocidas, por que solo existen dentro de la función.
