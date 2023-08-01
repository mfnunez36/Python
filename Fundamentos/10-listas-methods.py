lenguajes = ["phyton", "C#", "Java", "Javascript"]
#insertamos un elemento en la posicion indicada
lenguajes.insert(3, "Ruby")
print(lenguajes)

#eliminar un elemento
lenguajes.remove("C#")
print(lenguajes)

#buscar elemento
print("Go" in lenguajes)

#largo
print(len(lenguajes))

#limpiar lista 
lenguajes.clear()
print(lenguajes)