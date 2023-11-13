# Veamos un tipo de función especial en python
# Funciones Lambda o Funciones anónimas
# están limitadas a una sola expresión

#Veamos los siguientes ejemplos

suma = lambda a, b : a + b
multiplicacion = lambda a, b, c: a * b * c
constante = lambda: 10
# Veamos a continuación como se llaman las funciones lambdas
print(suma(2,3), multiplicacion(1,2,3), constante())
# por que se les conoce como anónimas
# Por que no tienen un nombre definido como los otros Tipos de funciones
# Vamos a realizar ahora un ejemplo para ordenar una lista
personas = [("Juan", 82, 5), ("Luisa", 41, 10 ), ("Arnulfo", 75, 20)]
print("Desorden", personas)
#Recordemos el método sort de las listas
personas.sort()
print("Orden por nombre ", personas)
# Que pasaría si en vez de usar sort que ordena por el primer elemento de las listas 
# Ordenamos por la edad
personas.sort(key = lambda persona: persona[1] )
print ("Orden por edad ",personas)
personas.sort(key= lambda persona: persona[1] + persona[2])
print ("Orden por edad + años de préstamo ",personas)