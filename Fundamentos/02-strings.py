# texto
texto = "Hello World"
print(texto)

# texto con mayusculas
print(texto.upper())

# texto con minusculas
print(texto.lower())

# texto con la primera letra en mayuscula
print(texto.capitalize())

# texto con la primera letra mayuscula de cada palabra
print(texto.title())

# cambio el caracter en mayuscula en minuscula y vice versa
print(texto.swapcase())

'''
busqueda de un caracter/es de texto
devuelve el numero de posicion en donde comienza (indice)
'''
print(texto.find("or"))

# reemplazar caracter/es de texto -> no reemplaza el texto inicial!
print(texto.replace("or", "ar"))

# busqueda dentro de un string -> devuelve verdadero o falso
print("He" in texto)

# podemos crear y asignar valores en una sola linea para ahorrar memoria utilizando ,
nombre, apellido = "nombre", "apellido"
print(nombre, apellido)

# concatenacion
print(nombre + apellido)

# podemos multiplicar un texto -> no se puede dividir aritmeticamente un texto 
print((texto + " ") * 3)

# string con string -> "''"
texto2 = "Cadena con \'Otra cadena\' con comillas simples"
print(texto2)

# salto de linea 
texto3 = "salto de linea \n otra cadena de texto"
print(texto3)

text4 = '''
    podemos tener un string con saltos de linea utilizando triple comillas simples y 
    tambien podemos utilizar para comentar en varias lineas
'''

# debanado de cadena -> segmentar string
texto5 = "texto segmentado en partes"
print(texto5[2:12])
print(texto5[2 : : 4])

# largo de un texto
print(len(texto))
