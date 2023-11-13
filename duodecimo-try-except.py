# Uso de try-except para control  de errores.
# Declaramos dos variables
try: 
    monto = float(input("Escriba el monto del crédito: ")) #Recordemos que input siempre regresa str(string)
    numero_pagos = int(input("Escriba el número de pagos que desea realizar para dicho monto: "))
    pago_mensual = monto/numero_pagos
    print("El pago mensual será de: ", pago_mensual)
    # Para controlar un ingreso de datos negativos podemos usar un if, que verifique que los datos ingresados 
    # no son negativos, esto es por que el dato negativo no me dará un error pero si me dará una respuesta incorrecta
    if(numero_pagos <0 ):
        raise Exception("Ingresa valores positivos para el número de pagos")
    #Con raise lo que hago es invocar una excepción que yo estoy controlando, pero al mismo tiempo se ejecutará
    #la parte Except de las exepciones predefinidas, incluso puedo asignarle un nombre propio de exepción
    #except exception as mi_error
    elif(numero_pagos>12):
        raise Exception("Tienes que pagar máximo en 12 meses o menos") #Esto igual va a lanzar except Exception
except(ValueError):
    print("Hubo un error, ingresastes un valor que no es válido") #Esta parte solo se va  a ejecutar si hay algún error.
except(ZeroDivisionError):
    print("Hubo un error, estás dividiendo por cero")
except Exception as mi_error:
    print(mi_error.args[0]) # Se puede colocar args sin valores pero regresa una tupla,
    # si deseamos que se regrese sin que sea tupla usamos el args[0], de esta manera solo retorna el mensaje 
    # del error. 
#Veamos el primer caso de errores
#Incluir el cero en pagos, esto provocará una división por cero.
#Error al dividir por zero: ZeroDivisionError
#Error al ingrsar un caracter en donde se espera un valor: ValueError

#Cuando se incluye el except, ahora el programa termina pero no de manera abrupta sino con el mensaje
#que está en el except
#Hasta aquí vimos excepciones preestablecidas, pero también puedo lanzar otras exepciones propias

#Por último si no hubo ninguna excepción se ejecutará un else:
else:
    print("La solicitud de tu crédito se ha aprovado exitosamente")

#Por último esta parte se va a ejecutar si o si después de todo finally
finally:
    print("Gracias por usar nuestros servicios")
