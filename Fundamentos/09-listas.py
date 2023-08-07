# para crear arreglo con []
lista = ["phyton", "C#", "Java", "Javascript", 1, 3.14]
print(type(lista))
print(lista)

# para saber el tamaño de la lista
print(len(lista))

#reemplazar un dato por posicion
lista[1] = "Go"
print(lista)

#buscar elemento
print("Go" in lista)

#podemos seleccionar posiciones de elementos 
#siempre restara un valor al segundo indice
print(lista[1:2])

#sin valor inicial o final tomara desde la primera o ultima posicion 
print(lista[:2])
print(lista[2:])

# podemos obtener en negativo
print(lista[-1]) 
print(lista[-2:])

# para agregar un dato / se agrega al final de la lista
print(lista)
print(lista.append("nuevo"))
print(lista)

# para agregar en un espacio especifico 
lista2 = ["uno", "dos", 3]
print(lista2)

# utilizamos insert y recibe la posicion y el dato que queremos agregar
lista2.insert(2, "tres")
print(lista2)

lista3 = [1, 1, 2, 3, 4, 5, 5, 1]
print(lista3)
# para poder contar cuantas veces se repite un dato 
print(lista3.count(1))

# para el dato mayor de la lista
print(max(lista3))

# para el dato menor de la lista
print(min(lista3))


# para buscar la posicion del primer valor encontrado 
print(lista3.index(1))
print(lista3.index(3))

# para eliminar elementos
# pop elimina el ultimo valor de la lista
lista.pop()
print(lista)

# remove recibe el valor a eliminar
lista.remove("Go")
print(lista)

# para sumar listas
# NOTA: no se pueden restar, multiplicar ni dividir aritmeticamente
nuevaLista = lista + lista2
print(nuevaLista)


