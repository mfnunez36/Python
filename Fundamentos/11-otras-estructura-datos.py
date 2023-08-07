# CONJUNTOS
# no se puden repetir los valores en un conunto
# otra manera de crear un conjunto con -> set(( 'dato1', 'dato2', 'dato3' ))
conjunto = { 'dato1', 'dato1', 'dato2', 'dato3' }

print(type(conjunto))
print(conjunto)


# para agregar un dato 
conjunto.add('dato4')
print(conjunto)

# para eliminar un dato
conjunto.remove('dato1')
print(conjunto)

# con pop tambien podemos eliminar al azar
conjunto.pop()
print(conjunto)

# para actualizar un conjunto
conjunto.update(['dato5', 'dato1'])
print(conjunto)


# TUPLAS
# otra forma de crear una tupla es sin parentesis -> tupla = 1, 2, 3, 4
# no se puden modificar sus valores pero funcionan como listas 
tupla = (1, 2, 3, 4)
print(type(tupla))
print(tupla)


