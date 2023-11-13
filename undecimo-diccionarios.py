# Diccionarios 
#Llaves: nombre, edad, dirección, altura, peso
#valores: "Juan",  33, "Lomas de Monserrat", 1.70, 70kg

#Para declarar un diccionario se usan {clave:valor}
persona = {"Nombre":"Juan", "Edad": 33, "Direccion": "Lomas de Monserrat", "Altura":1.70 }

print(persona)
print(persona["Edad"])
print(persona.get("Edad"))
#Accediendo a Claves
print(persona.keys())
#Accediendo a los valores
print(persona.values())
#Accediendo a Ambos
print(persona.items())

#Recorriendo valores, llaves, items del diccionario
for value in persona.values():
    print(value)
for key in persona.keys():
    print(key)
for item in persona.items():
    print(item)
for llave, valor in persona.items():
    print(llave,":"," ",valor)

#Si necesitamos editar un valor del diccionario tomamos de referencia la llave.
persona["Direccion"] = "Reforma 300"
print(persona["Direccion"])
#Si queremos modificar varias llaves del diccionario podemos utilizar el siguiente método .update({})
# Update permite agregar un nuevo clave:valor, dentro del mismo diccionario en este caso agregamos ID:408
persona.update({"Direccion":"Santo Domingo", "Altura":1.75, "ID": 408})
print(persona)
#Otra manera de agregar un nuevo clave valor al diccionario es:
persona["Peso"] = 70
print(persona)
#Para borrar valores podemos utilizar el método pop, indicando la llave que queremos quitar, peso
persona.pop("Peso")
#Verificamos que peso ya no está en el diccionario 
print(persona)

#Ahora vamos a realizar un ejercicio para contar palabras para poner en práctica los diccionarios
texto = "Nos recuerdan que los hombres han evolucionado para admirar se de las cosas, que comprender es una alegría, que el conocimiento es requisito esencial para la supervivencia. Creo que nuestro futuro depende del grado de comprensión que tengamos del Cosmos en el cual flotamos como una mota de polvo en el cielo de la mañana. Estas exploraciones exigieron a la vez escepticismo e imaginación. La imaginación nos llevará a menudo a mundos que no existieron nunca. Pero sin ella no podemos llegar a ninguna parte. El escepticismo nos permite distinguir la fantasía de la realidad, poner a prueba nuestras especulaciones. La riqueza del Cosmos lo supera todo: riqueza en hechos elegantes, en exquisitas interrelaciones, en la maquinaria sutil del asombro. La superficie de la Tierra es la orilla del océano cósmico. Desde ella hemos aprendido la mayor parte de lo que sabemos. Recientemente nos hemos adentrado un poco en el mar, vadeando lo suficiente para mojamos los dedos de los pies, o como máximo para que el agua nos llegara al tobillo. El agua parece que nos invita a continuar. El océano nos llama. Hay una parte de nuestro ser conocedora de que nosotros venimos de allí. Deseamos retomar. No creo que estas aspiraciones sean irreverentes, aunque puedan disgustar a los dioses, sean cuales fueren los dioses posibles. Las dimensiones del Cosmos son tan grandes que el recurrir a unidades familiares de distancia, como metros o kilómetros, que se escogieron por su utilidad en la Tierra, no serviría de nada. En lugar de ellas medimos la distancia con la velocidad de la luz. En un segundo un rayo de luz recorre casi 300.000 kilómetros, es decir que da diez veces la vuelta a la Tierra. Podemos decir que el Sol está a ocho minutos luz de distancia. La luz en un año atraviesa casi diez billones de kilómetros por el espacio. Esta unidad de longitud, la distancia que la luz recorre en un año, se llama año luz. No mide tiempo sino distancias, distancias enormes."
simbolos_a_quitar = (",", ".", "(", ")")

for simbolo in simbolos_a_quitar:
    texto = texto.replace(simbolo,"")

texto = texto.upper()
vocablos = texto.split()
palabras = {} #Creamos un diccionario nulo
for vocablo in vocablos:
# "nombre" in persona.keys() --> Retorna True
# 33 in persona.values() --> Retorna True
# Entonces vamos a utilizar esta manera para contar las veces que aparece una frase en todo el texto

    if vocablo in palabras.keys():
        palabras[vocablo] = palabras[vocablo] + 1
    else: 
        palabras[vocablo] = 1
# Ahora para contar las palabras que mas aparecen en el texto necesitamos ordenar 
# Pero un diccionario ya trae su manera de ordenar y no podemos cambiarlo
# Como alternativa a esto podemos convertir el diccionario a lista y las listas si 
# podemos ordenarlas, usando la palabra clave list()

lista = list(palabras.items()) #Aqui vamos a tomar algo que probamos anteriormente, 
#que fué obtener claves:valores con item()
#Ahora ordenemos la lista
lista.sort()
#ahora imprimamos para verificar el estado de lista
print(lista)
# Utilicemos una función lambda para cambiar el orden de la lista esto lo vimos en la clase anterior
lista.sort(key= lambda palabra : palabra [1])
print(lista)

