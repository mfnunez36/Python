''' 
para crear una funcion

def <nombre funcion>(<parametros: opcional>):
    <accion de funcion>

'''

# sin parametros
def caminar():
    print("Esta caminando")

caminar()



# con parametros
def suma(num1, num2): 
    print("la suma de {} + {} = {}".format(num1, num2, (num1 + num2)))
    
suma(4, 2)



# con return
def saludar(nombre):
    return "Hola {}".format(nombre)

# guardamos lo que retorna para poder mostrarlo
saludo = saludar("Pedro")
print(saludo)



# para recibir una tupla como parametros debemos anteponer *
# sirve para recibir varios datos con mismo o diferente tipo
def recibeTupla(*parametros):
    print(parametros)
    # retornamos type para que veamos que tipo de parametro recibe
    return type(parametros)

print(recibeTupla("dato1"))
print(recibeTupla("valor1", 1, 2, 3, "cuatro"))