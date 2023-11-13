# A continuación veremos como pasar parametros por valor 
# y parámetros por referencia
"""En el paso de parámetros por valor, se crea una copia local de la variable
en la memoria de la función. Cualquier cambio realizado en la variable en la 
función no afectará al valor original de la variable en el código de llamada.

En el paso de parámetros por referencia, no se crea una copia local de la variable. 
En cambio, la función recibe una referencia a la variable original. Cualquier 
cambio realizado en la variable en la función también afectará al valor original 
de la variable en el código de llamada."""

""" Tomando una referencia de algo de la vida real, sería como cuando prestas 
o alquilas una casa, la casa no te la puedes llevar con todo y los cimientos,
pero si puedes brindar la dirección donde está esa casa. Esto es un parámetro por 
valor,
El parámetro por valor es como prestar un lapicero, ese si fisicamente se lo puedes 
dar a un compañero, este es por valor.
"""

#Cuando se usan las funciones y se les pasan estructuras de datos como listas, tuplas, conjuntos
#python determina que estas estructuras pueden contener grandes cantidades de datos,
#decide que serán pasados por valor, pasando la dirección de memoria donde están esos datos
#Mientrás que con las  primitivas(int, float, string) acá se pasa el dato, no la dirección
#Por lo tanto estos no se modifican.

# Veamos a continuación los ejemplos
# tomaremos parámetros por valor y por referencias
# por valor multiplicaremos una lista por 2

def doble(referencia, valor):
    referencia *= 2
    valor *=  2
    print ("Durante", referencia, valor)

estructura= ["a","b","c"]
primitiva = "abc"
#imprimamos los valores antes para comparar
print("Antes", estructura, primitiva)
print("Durante", doble (estructura, primitiva))
print("Antes", estructura, primitiva)

