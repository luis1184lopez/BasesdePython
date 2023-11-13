#Las estructuras de datos permiten 
#manipular datos
#Veamos el ejemplo con listas [], edades = [25,36,38,40,52]

edades = [25,36,38,40,52]
print(edades)
#Podemos acceder a cualquier elemento de la lista por medio de los indices
#Recuerden que inician en 0.
print(edades[0])
#Igualmente modificar valores de la lista por medio de su indice
#El elemento indice 4, 52 pasa ahora a valer 36
edades[4]= 36
print(edades)
#Igualemente indicar rangos con los valores de la lista [:]
#Observar el detalle que aunque mando a llamar al indice 2, la lista 
#solo regresa los indices 0,1
print(edades[:2])
#Otra variante 
print(edades[2:])

#Hay dunciones con las que podemos trabajar sobre datos numéricos de la lista
#max(),  min(), sum()
print(max(edades)) # debe retornar 40
print(min(edades)) # debe retornar 25
print(sum(edades)) # debe retornar la sumatoria 175

#No hay función de promedio definida pero podemos hacer lo siguiente
#sum(edades/len(edades))
print(sum(edades)/len(edades))

#Las listas son elementos complejos y tienen sus propios métodos.
# Veamos a continuacion una manera de agregar un nuevo elemento a la lista
# insert, que requiere 2 argumentos, primero dato a insertar y segundo en que posición
print(edades)
edades.insert(5,78)
print(edades)
#La otra manera es usar append(), automáticamente lo agrega al final de la lista
print(edades)
edades.append(99)
print(edades)
#Hay un caso mas particular y es el uso de extend()
#Agrega una lista de una lista
edades.extend([56])
print(edades)
edades.extend([36,36,74,75])
print(edades)

#Ahora que hemos visto como agregar elementos, veamos como borrar elementos
#Para esto usamos del 
del edades[9]
print(edades)
#Otra manera es cuando se desea quitar un valor de la lista
#Para esto se usa remove, pero solo remueve el primer valor que coincida
# Veamos como de la lista que tiene 2 valores de 36, solo quita el primero
edades.remove(36)
print(edades)
#Otra manera de remover pero el último elemento de la lista es pop()
#Aqui no pide el indice por que va a remover siempre el último elemento
#Retorna el elemento eliminado
edades.pop()
print(edades)

#Hay algunos otros métodos interesantes
#contar cuantas veces aparece un elemento en la lista
#count()
print(edades.count(38))
print(edades.count(36))

#Podemos hacer búsquedas dentro de las listas
#para esto usamos index
#retorna el indice donde encontró ese valor
print(edades.index(99))

#Para ordenar una lista si quisieramos que los valores no esten desordenados
edades.sort()
print(edades) # Ordena de menor a mayor

edades.sort(reverse=True)
print(edades) # Ordena de mayor a mayor

#Otra manera de ordenar de manera inversa es 
#Usando reverse
edades.sort()
print(edades)
edades.reverse()
print(edades)

#Las listas no sólo son para datos numéricos, 
#se pueden combinar entre datos numéricos, string, float 
estudiante1=["José", 20, 1.78]
print(estudiante1[0])
estudiante2=["Maria", 19, 1.58]
print(estudiante2[0])
#Otra característica de las listas es que se pueden anidar listas dentro de otras listas
estudiantes =[estudiante1,estudiante2]
print(estudiantes)
#Acceder a las listas como si fueran elementos
print(estudiantes[0])
print(estudiantes[1])

#Pero si quisiera acceder al nombre José dentro del estudiante 0, veamos
print(estudiantes[0][0])
print(estudiantes[0][1])
print(estudiantes[0][2])
 