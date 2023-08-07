import keyword
'''REGLAS:
 no pueden comenzar con numero
 las variables no pueden ser llamadas como palabras reservadas del lenguaje
 para ver las palabras reservadas podemos utilizar keyword
'''
print(keyword.kwlist)
'''
 no pueden llevar caracteres especiales en su nombre ej: unavaria@ble = "valor"
 no pueden ser nombradas con espacio
 los strings son sensible a mayusculas y minusculas
'''

texto = "String"
print(type(texto))

numero = 30
print(type(numero))

decimal = 0.10
print(type(decimal))

verdadero = True
print(type(verdadero))

falso = False
print(type(falso))



# para crear variables globales
# no se pueden inicializar en su creacion ej:(global nombre = "valor")
global varGlobal
varGlobal = "valor"
print(varGlobal)