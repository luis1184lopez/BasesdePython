#Ejemplo de Imprimir en pantalla
print("Bienvenido Hello Word")

#Variables

edad = 17
Edad = 18
altura = 1.75 

#Imprimir variables 
print(edad)
print(Edad)
print(altura)

#Verificar el tipo de variable 
print(type(edad))
print(type(Edad))
print(type(altura))

#Incluso una misma variable puede cambiar de tipo en el camino, pasó de float a int
altura = 200
print (altura, type(altura))

# Operadores aritméticos
# Orden de precedencia
# () ** -negación %  // / * + -

a = 5 
b = 2

print( a + b)  # Suma
print( a - b)  # Resta
print( a * b)   # Multiplicacion
print( a / b)   # Division fraccionaria redondeando hacia abajo
print( a // b)  # División entera
print( a % b)   # Modulo o residuo
print( a ** b)  # Potenciación
print( a + b * a) #Orden de precedencia
print( (a + b) * a) #Orden de precedencia con parentesis, da prioridad

#Varibles de tipo String (cadenas)
nombre = "Juan"
print(nombre[0], nombre[1], nombre[2], nombre[3])
apellido = "Gutierrez"
# Usa el + para concatenar cadenas 
nombre_completo = nombre  + " " + apellido
print(nombre_completo)
# Averiguar el largo de una cadena de texto(len)
print("Longitud: ", len(nombre_completo))
# Funciones de conversion de cadena str(), int(), float()
numeroacadena = 456
print(str(numeroacadena) + " " + str(numeroacadena))
print(" ")
# Incluso se puede multiplicar una cadena con un número 
print(nombre_completo*2)
#Ejemplos de conversiones de datos
entero = 3
decimal = 4.0

entero_string = str(entero)
decimal_string = str(decimal)

print(entero_string + decimal_string)
# Para comentar de una linea se usa #
"""Para comentarios de  
varias lineas"""

#Para trabajar con rangos de cadenas de texto se usa [0:...]
print(nombre_completo[0:4]) #Imprime Juan 
# Se puede obviar el termino 0 al inicio [:] y solo indicar el final.
print(nombre_completo[:5]) #Imprime Juan
# Se puede modificar el rango de Inicio para que no inicie en 0, [8:15]
print(nombre_completo[5:14]) # Imprime Gutierrez
# Se puede usar la función len()
print(nombre_completo[5:len(nombre_completo)])
#También se puede Obviar la parte del final [5:]
print(nombre_completo[5:])
# Se pueden utilizar funciones para convertir todo a mayúscula .upper()
print(nombre_completo.upper()) 
# Se pueden utilizar funciones para convertir todo a minúscula .lower()
print(nombre_completo.lower()) 
# Podemos usar el método capitalize() para escribir el primer caracter de texto en mayúsculas.
print(nombre_completo.capitalize())
# El método strip() permite limpiar carácteres que causan ruido en la cadena de texto.
pruebaconruido ="     Luis López     "  
print(pruebaconruido)
print(pruebaconruido.strip())
# El método replace() reemplaza una letra por otra
nombreconerror = "0ctavi0"
print(nombreconerror.replace("0","o"))
# indice regresa el número de indice de donde se encuentra ubicado el carácter buscado
print(nombreconerror.index("t"))

# Variables boolenas (true o false) 
esbienvenido = True



