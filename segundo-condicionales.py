#El signo = permite asignar un valor a una variable
a=3
print(a)
#El signo == permite comparar dos valores o variables.
print(a==3)

#Ejemplo de estructura condicional
#Si encuentra un valor que se hace verdad entra e imprime y luego se sale de la estructura if
#Se requieren if independendientes en el caso que se requiera que las desiciones se evaluen una a una
artes = True
deportes = True
matematicas = True

if artes == True:
    print("Estudia teatro")
elif deportes == True:
    print("Estudia medicina deportiva")
elif matematicas == True:
    print ("Estudia matemáticas")
else:
    print("Consulta a un asesor vocacional")

#Hay otro método donde no es necesario especificar si una condición es True.
if artes:
    print("Artes es verdadero")

# También podemos combinar con otros operadores lógicos como and y or
# True and True es igual a True 
if artes and deportes:
    print("Artes y deportes es verdadero")
# True or False, True es igual a True 
# False or False es igual a False
if artes or deportes:
    print("Artes o deportes es verdadero")

#Otro operador condicional es not, que cambia un valor False a True y viceversa
if not artes or deportes:
    print("Artes esta negado")
# Investigar tablas de verdad de operadores booleanos de and y or

# Operadores de comparación, permiten comparar valores
#Ejemplo solo comparamos una altura
altura = 151
if altura < 160:
    print("Eres de baja estatura")
if altura > 170:
    print("Eres de alta estatura")
#En este ejemplo comparamos mas de una altura, permite trabajar con rangos.
altura= 190
if altura >= 150 and altura <= 160:
    print("Eres de baja estatura master")
elif altura >= 170 and altura <= 180:
    print("Eres de estatura mediana master")
else: 
    print("Altura no determinada")

#Aqui se ha evaluado con un valor fijo, pero también el valor 
#puede ser ingresado por el usuario
#Ahora conozcamos a la función input()

entrada_datos= input("Ingrese su edad: ")
#Al capturar el dato con input obtenemos
#un string, lo cual no nos funciona para comparar 
#por eso debemos utilizar la función  int() y 
#pasarlo en este caso a número.
edad = int(entrada_datos)
#La otra manera es: una función dentro de otra función
# entrada_datos= int(input("Ingrese su edad")) 
if edad < 30:
    print("Eres bastante joven")
else: 
    print("Eres muy adulto")
