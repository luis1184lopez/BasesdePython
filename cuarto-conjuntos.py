""" Los sets tienen una caracteristica especial
que los diferencia de las listas,
estos no aceptan valores repetidos"""

#Para definir un conjunto (set) se utilizan {} Llaves

estudiantes2022= {"Juan", "Pedro", "Carla", "Maria", "Juan"}
#No marca error al declarar que hay dos nombres iguales "Juan", pero
# podemos ver que al imprimir solo hay un "Juan"
print(estudiantes2022)
#Otro detalle es que no hay garantía del Orden de los elementos en el conjunto 
estudiantes2023 = {"Luis", "Rosa", "Carla", "Javier", "Juan"}

#Para agregar valores al conjunto, se hace usando el método .add(value)
#Sin embargo si el valor está repetido este no dará error pero siempre
#Habrá solo un valor 
print(estudiantes2023)
estudiantes2023.add("Luis")
print(estudiantes2023)
#Si el nombre no existe en el conjunto si será agregado.
estudiantes2023.add("Pedro") 
print(estudiantes2023)

#De esta manera agregamos valores al conjunto
#Ahora veamos como remover elementos del conjunto
# Para eso usamos el método .remove(value)
print(estudiantes2023)
estudiantes2023.remove("Rosa")
print(estudiantes2023)

#Ahora veamos algunas operaciones que podemos realizar con los conjuntos
# Por ejemplo ver los nombres utilizados en los dos años
# Uniendo dos conjuntos 
# union
print(estudiantes2022)
print(estudiantes2023)
estudiantestotal = estudiantes2022.union(estudiantes2023)
#Al realizar la union de los conjuntos se eliminan los elementos repetidos
print(estudiantestotal)

#Podemos también ver que nombres se repiten en ambos años 
# intersection
nombresrepetidos = estudiantes2022.intersection(estudiantes2023)
print(nombresrepetidos)

#Podriamos también hacer una operación para mostrar los nombres 
#sin los que se repiten
print("------------------------")
estudiantessinrepetir = estudiantestotal.difference(nombresrepetidos)
print(estudiantessinrepetir)

#Otra operación es validar si dentro del conjunto que contiene todos los nombres
#Se encuentran todos los nombres de un conjunto mas pequeño
#issubset
esteconjunto = estudiantes2022.issubset(estudiantestotal)
print(esteconjunto) # True 
#Podemos probar lo inverso 
#Si dentro del conjunto estudiantes 2022 están todos los nombres del conjunto estudiantestotal
esteconjunto = estudiantestotal.issubset(estudiantes2022)
print(esteconjunto) # False

#Otra alternativa es ver si un conjunto le pertenece a un conjunto mayor
#Esto lo podemos lograr por medio de 
#issuperset
esteconjunto = estudiantestotal.issuperset(estudiantes2022)
print(esteconjunto) # True 
# Ya que el conjunto estudiantestotal es como el padre de estudiantes2022 
# y contiene todos los elementos.
