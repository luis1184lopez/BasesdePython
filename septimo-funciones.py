# Funciones 
# Permiten organizar y ordenar el código
# Una función es como una cajita donde ingresamos 
# Materia prima y obtenemos un producto
# Una funcion se define def nombre_función(parámetro1, parametro2):
def suma(a, b):
    sumar= a+b
    return sumar #Opcional pero se usa cuando se necesita que se retorne un dato 
print("El resultado de la suma de dos números es:", suma(3,5))

#Miremos otro tipo de forma de definir parámetros en una función
#(*parametros) con esto se define una longitud indeterminada de parámetros de entrada

def suma_muchos_numeros(*numeros): #El asterisco indica que lo que sigue es un indicador tipo tupla
#Al ser una tupla se puede procesar con un for
    suma=0
    for numero in numeros:
        suma=suma+numero
    return suma

print("Suma",suma_muchos_numeros(1,2,3,4,5,6) ) #Aqui apreciamos como enviamos muchos parámetros,
#por que en la función utilizamos el * para especificar la recepción de varios parámetros.


#Veamos algunas utilidades de las funciones
def formateo_nombre(nombre, primerapellido, segundoapellido):
    formateo = nombre.upper() + " " + primerapellido.capitalize() + " " + segundoapellido.capitalize()
    return formateo
print(formateo_nombre("LuiS", "CAstro", "MaireNA"))

# Analicemos el siguiente caso 
# Que sucedería si yo solo coloco 2 parámetros a la función
"""def formateo_nombre(nombre, primerapellido, segundoapellido):
    formateo = nombre.upper() + " " + primerapellido.capitalize() + " " + segundoapellido.capitalize()
    return formateo
print(formateo_nombre("LuiS", "CAstro")) # Retorna un error, missing 1 required positional argument: 'segundoapellido'
"""
#Como podriamos solucionar este detalle: 
#Agregando un valor pordefecto

def formateo_nombre(nombre, primerapellido, segundoapellido=""):
    formateo = nombre.upper() + " " + primerapellido.capitalize() + " " + segundoapellido.capitalize()
    return formateo
print(formateo_nombre("LuiS", "CAstro")) # Se soluciona el error de missing argument

#Otra situación que se puede presentar es el envío de los datos con diferente orden al que espera la función
def formateo_nombre(nombre, primerapellido, segundoapellido=""):
    formateo = nombre.upper() + " " + primerapellido.capitalize() + " " + segundoapellido.capitalize()
    return formateo
print(formateo_nombre(segundoapellido="Rivas", primerapellido="sanchez", nombre= "Jose LuiS" )) # Aquí se define cada 
#parámetro en el caso de funciones que tengan muchos datos, aunque sean enviados en otro orden

#Veamos ahora como crear una función para una cédula de identidad de un pais(DNI), de ejemplo para una función mas compleja
#nombre = "JUAN HERNANDEZ JIMENEZ"
#fechanacimiento = 1980
#clave -> JHJ80
# Para esto vamos a usar el método split() que detectará el espacio en el nombre y lo separará
#nombre = "JUAN HERNANDEZ JIMENEZ"
#print(nombre.split())
#retorna ['JUAN', 'HERNANDEZ', 'JIMENEZ']
def crea_clave(nombre, fechanacimiento):
    clave = ""
    for elemento in nombre.split():  #Usamos un for para trabajar explicitamente con las listas 
        clave = clave + elemento[0]
    fechanacimiento = str(fechanacimiento) # Convertimos la fecha a cadena de texto para poder manipular 
                                           # y extraer fácilmente los últimos dos digitos.
    return clave+fechanacimiento[-2:]
print(crea_clave("JUAN JOSE PEREZ", 1985))

# Nota: si notamos en algún caso que en el resultado aparece un None
# Significa que podemos haber olvidado incluir la palabra return para 
# que la función retorne un valor.