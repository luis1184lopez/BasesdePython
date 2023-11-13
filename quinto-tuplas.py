"""Tuplas: Tienen la caracteristicas de no poder
ser modificado una vez defininas, ni agregar ni quitar
elementos"""
#1. Es una estructura de datos mas eficiente que las listas
#2. Evitar la modificación de datos.
# Para definir una tupla usamos el ()
tupla = ("Luis", 38)
print(tupla)
#Comprobemos que no podemos agregar un elemento nuevo
print(tupla[0])
#tupla[0] = "José" #Error

#Hay un forma de añadir un elemento a la "tupla"
lista = list(tupla)
print (lista)
lista[0]= "Juana"
print (lista)

# Ahora el proceso inverso convertir una lista en tupla
tupla = tuple(lista)
print(lista)

#Incluso pasar a un conjunto 
conjunto = set(tupla)
print(conjunto) #Nótese las llaves 

#El uso de cada uno de los ejemplos vistos,
# Listas, conjuntos y tuplas va a depender 
# En gran medida de la necesidad de cada tarea a realizar.