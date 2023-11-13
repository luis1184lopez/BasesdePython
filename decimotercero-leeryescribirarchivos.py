#La información almacenada en nuestros programas son volátiles
#a menos que los guardemos en una base de datos o en archivos, 
#cuando cerremos nuestro programa se perderán.

#Para abrir un archivo de texto tenemos la instrucción 
#open("datos.txt") Esto me permite abrir el archivo, sin embargo no puedo trabajar mientras no lo 
#asigne a una variable
#archivo = open("datos.txt") 
archivo = open("datos.txt") 
texto = archivo.read()
print(texto)
archivo.close()
#archivo = open("datos.txt", encoding="utf-8") 
archivo = open("datos.txt", encoding="utf-8") 
#Ahora veamos como acceder al contenido del archivo. Mediante readline
#Si en algún caso el texto a leer dentro del archivo lleva acentos o ñ, debemos indicar que 
#no se usará la codificación predefinida sino usaremos encoding="utf-8", para que no genere detalles.
#Ahora podemos apreciar, que se leyó el archivo sin problemas con el acento.
texto = archivo.read()
#Imprimimos el valor almacenado en texto
print(texto)
#Cuando se abre un archivo el contenido de este se carga en memoria, si no lo cerramos 
#Esto hará que la computadora se vaya saturando y no queremos eso.
#Para solucionar este detalle siempre debemos cerrar el archivo.
#Si probamos como lee el read() cuando agregamos un parámetro, podemos ver que lee pero el cursor no reinicia, 
#queda automaticamente hasta donde llegó la última vez.
archivo1 = open("datos1.txt", encoding="utf-8") 
textouno = archivo1.read(5)
print(textouno)
textouno = archivo1.read(5)
print(textouno)
#Podemos apreciar que el texto se lee con continuación 
#Otra forma de leer un archivo es con readline
archivo.close()
archivo1.close()
#Ya vimos que read lee todo el texto, recordando que el cursor queda donde se le indique read(5)
#queda en la posición 5 y la próxima vez que ejecute read(), continuará en esa posición.
#Pasemos a ver otro tipo readline, este leerá cada linea del archivo.
archivo = open("datos.txt")
textolineas = archivo.readline()
print(textolineas)
textolineas = archivo.readline()
print(textolineas)
textolineas = archivo.readline()
print(textolineas)
#Si se quiere imprimir una nueva línea que no existe por ejemplo la línea 4,
textolineas = archivo.readline()
print(textolineas)
archivo.close()
#No se provocará ningún error, el puntero queda siempre al final de la última línea que tenga contenido.

#Si deseamos saber cuantas lineas de texto tiene nuestro archivo podemos usar readlines()
#Esto retornará una lista de x variables str, observar el \n indicandonos que hay un enter
archivo = open("datos.txt")
cuantaslineas = archivo.readlines()
print(cuantaslineas)
archivo.close()
#Hay otra manera de abrir un archivo y es utilizando with, esto permite que si por alguna razón 
#no se cerró el archivo con close(), de esta forma el with lo cierra automáticamente.
with open("datos.txt", encoding="utf-8") as archivo:
    lineas =archivo.readlines()
    print("Usando  with", lineas)

# Ahora nos podemos preguntar, hasta el momento he leído el contenido de un archivo, pero  
# ¿Qué sucede si quiero escribir en ese archivo?
# Para eso usamos los modos r o w, r no es necesario escribirlo por ser el modo por defecto.

with open("persona.txt","w", encoding="utf-8") as archivo:
    archivo.write("Este es un texto linea 1 agregado desde programación") #Usamos el método write para crear el archivo
    #Podemos verificar que el archivo no existe aún.
    archivo.write("\n")
    archivo.write("Este es un texto linea 2 agregado desde programación") 
    #Después que verifiquemos que el contenido del archivo podemos apreciar que las dos líneas están seguidas,
    #debemos agregar el salto de línea \n, sino se escribirá seguido
    #Hay que tener cuidado con "w" por que sobreescribe la información cada vez que corre el programa
    #Supongamos que cada vez que lo usamos no queremos que nos borre lo anterior, para esto entonces usamos "a"
    #que viene de append(añadir), verifiquemos si es cierto que añade y no reescribe.
with open("persona.txt","a", encoding="utf-8") as archivo:
    archivo.write("\n")
    archivo.write("Este es un texto linea 3 agregado desde programación")
    archivo.write("\n")
    archivo.write("Este es un texto linea 4 agregado desde programación")
#Verificamos que todas las líneas tengan su texto sin estar unidas.
with open("persona.txt", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    print("Usando  with", lineas)

#Hasta aquí tenemos la primera parte del manejo de archivos
#Aquí podemos ver que se ha trabajado con archivos de manera directa en su ruta o su ubicación
#Esto es debido a que están ubicados dentro de mi carpeta de proyecto.
#¿Qué pasaría si usamos un archivo que no está en la misma carpeta?
#Ahora veremos como hacer uso de referencias relativas y absolutas.
#Podemos usar la ayuda de Visual Studio Code y apoyarnos de las opciones de que al dar clic derecho en el archivo
#Muestre ruta relativa y absoluta

#Ahora vamos a hacer uso de estructuras de datos que ya vimos como listas y diccionarios,
#Para el siguiente ejemplo usemos el archivo datosmetro.txt
#Nota: Cuando se trabajan con archivos donde los datos vienen sin separación es un dolor de cabeza para el programador
#Debido a que no se sabe donde termina cada dato, puede venir por ej. con un apellido, con dos, etc.
#Para eso se usan los valores separados por comas, de esta manera podemos apreciar donde finaliza cada dato.

#Usando un diccionario key: [values]
"""Entrada
Estación,Enero,Febrero,Marzo
Buenos Aires,100,200,300
Bellas Artes,400,500,600
Hidalgo, 700,800,900
______________________________
Lo que vamos a hacer
{
"Buenos Aires": [100,200,300]
"Bellas Artes": [400,500,600]
"Hidalgo": [700,800,900]
}
"""
#Crear el diccionario nulo
print("Usando un diccionario y leer archivos")
pasajeros = {}
#Abrir el archivo
#No queremos tomar en cuenta la primera fila de contenido ya que representa ruido para mis datos
with open("datosmetro.txt","r",encoding="utf-8") as archivo:
    archivo.readline() #Quitar el encabezado
    estaciones = archivo.readlines() #Leemos el resto del archivo que es lo principal
    #Verificamos que lo que leimos está correcto
    print(estaciones)
    #Vamos a procesar y vamos a quitar \n(enters) que no nos interesan
    #REcorremos cada uno de las lineas
    for estacion in estaciones:
       lista = estacion.strip().split(",") #Podemos ver que se han quitado los \n 
       print (lista)
       pasajeros[lista[0]] = list(map(int,lista[1:])) #map, permite aplicar una función a un rago de datos 
       #en este caso se aplica int a todos los elementos de la lista[1:]
       
print(pasajeros["Hidalgo"])
print(sum(pasajeros["Hidalgo"]))




