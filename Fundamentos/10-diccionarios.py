datos = {
    'username': 'locoJonny',
    'password': 'Oi$U%Kn*1/761',
    'email': 'a@b.com'
}

print(type(datos))
print(datos)

# obtener las claves del diccionario
print(datos.keys())

# obtener los valores del diccionario
print(datos.values())

# obtener por llave
print(datos['username'])

# para obtener un valor
print(datos.get('password'))

# agregar un dato
datos['edad'] = 25
print(datos)

# agregar un dato con setDefault
datos.setdefault('nombre', 'Jonny')
print(datos)

# para actualizar o agregar datos
datos.update({ 'username' : 'lukyJonny', 'nuevoKey': 'nuevoValue' })
print(datos)

# para eliminar un dato
datos.pop('edad')
datos.pop('password')
print(datos)

# para limpiar el diccionario
datos.clear()
print(datos)