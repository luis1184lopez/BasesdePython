#Ahora veremos como importar algunos módulos que ya traen funciones predefinidas
#Veamos el ejemplo con el moódulo math

#help ("modules")
import math  #Cargamos el módulo
#help ("math") #Nos permite visualizar todas las funciones que posee el módulo math
#Ahora que ya importamos el módulo math, vamos a usar dos funciones que vienen dentro de este ceil,floor
#Veamos que hace cada una de ellas.
#ceil
print(math.ceil(2.1)) #me devuelve el valor entero hacia arriba
print(math.ceil(2.9)) #revisemos con otro valor

print(math.floor(2.1)) #me devuelve el valor entero hacia abajo
print(math.floor(2.9))

#Otra manera de importar una libreria o módulo
# como un apodo  as x
import math as m
print(m.ceil(2.1), m.floor(2.9))

#Otra forma es importar solo las funciones con las que voy a trabajar
from math import ceil,floor #equivalente a from math import *
print(ceil(2.1), floor(2.9))

