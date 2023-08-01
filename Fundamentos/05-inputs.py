dato = input("Ingresa un dato: ")
print("El dato es: ", dato)

'''
para obtener un tipo de dato diferente a un string 
debemos hacer la conversion
'''
edad = int(input("Ingresa tu edad: "))
print(edad)
print(type(edad))

# con format podemos utilizar variables dentro de la cadena 
nombre = input("ingresa tu nombre para tu saludo: ")
edad = int(input("Ingresa tu edad: "))
print("Hola {} bienvenido, tu edad es {}".format(nombre, edad))



'''
Ejercicio:
- Dada esta ecuacion 3x^2-5x+2=0
- Determinar el valor de x1 y x2
- Utilize la formula cuadratica de ecuaciones de segundo grado 
- Los numeros de a b y c deben ser ingresados por consola
'''
from math import sqrt

A = int(input("ingrese el valor de A: "))
B = int(input("ingrese el valor de B: "))
C = int(input("ingrese el valor de C: "))

if ((B**2) - (4 * A * C)) < 0:
    print("Fallo el calculo de la raiz por numero negativo")
else:
    X1 = ( -B + sqrt((B**2) - (4 * A * C)) )/(2 * A)
    X2 = ( -B - sqrt((B**2) - (4 * A * C)) )/(2 * A)
    print("el valor de X1 = ", X1)
    print("el valor de X2 = ", X2)