# Ciclos while y for
# Similitudes y diferencias 
# Estructuras ciclicas
# Permiten ejecutar instrucciones bajo 
# Ciertas condiciones 
# while(Boolean expression)
"""
edad = 0
while(edad < 10):
    print("Contando...",edad)
    edad+=1 #Otra manera de usarlo es edad = edad +1 
print("Terminó el while")
# Recordar el uso de las tabulaciones que 
# permiten definir los bloques a ejecutar
"""
"""
total = 0 # Acumulador que guardará la suma
numerodesumas = 5
contador = 0
while (contador < numerodesumas):
    num= int(input("Escribe un número "))
    total = total + num
    contador+=1
print("El total de la suma es: ",total)
"""
#Probemos con un pequeño ejercicio
# Simulemos una autenticación de usuario
"""
acceso = False
while acceso == False:
    ingreso = input("Ingrese la contraseña:")
    if ingreso == "123456":
        acceso = True
        print("Bienvenido al Sistema")
    else:
        print("Ingrese otra contraseña")
        acceso = False
"""
#Veamos ahora el otro tipo de ciclo
#for
#La primera forma es usando una lista
#La finalidad del for es trabajar con listas
for numero in [1,2,3,4,5,6,7,8,9]:
    print(numero)
# Veamos como se repite 3 veces por que hay 3 elementos
# Luego imprime cada elemento
for numero in [80,45,78]:
    print(numero)

# Pinturas
colores = ["rojo", "verde", "azul", "amarillo"]

for color in colores:
    print("Hay pintura de color: ", color)
print("-----------------")
#Veamos como funcionaría este mismo ciclo con un while
indice = 0 
while indice < len(colores):
    print("Hay pintura de color: ", colores[indice])
    indice += 1

# Otra manera en la que trabaja el for es con un range(), rango
# Para el caso en que la lista sea grande
# Aqui va desde 0 hasta el 20 
for numero in range(20):
    print(numero)
#Otra manera es que vaya desde un rango especifico
for numero in range(10,20):
    print(numero)