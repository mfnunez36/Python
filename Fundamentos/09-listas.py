lenguajes = ["phyton", "C#", "Java", "Javascript"]
#reemplazar un dato por posicion
lenguajes[1] = "Go"
print(lenguajes)

#podemos seleccionar posiciones de elementos 
#siempre restara un valor al segundo indice
print(lenguajes[1:2])
#sin valor inicial o final tomara desde la primera o ultima posicion 
print(lenguajes[:2])
print(lenguajes[2:])
