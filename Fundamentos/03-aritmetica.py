print(1 + 2)
print(1 - 2)
print(1 * 2)
print(1 / 2)

# division entera -> solo devuelve la parte entera de la division sin decimales
print(20 // 3)

# elevado a
print(10 ** 2)

# tambien podemos utilizar pow() que recibe como primer parametro el numero a elevar
# como segundo parametro recibe el numero de exponencial
print(pow(10, 2))

# modulo de un numero -> es lo que resta de la division de 2 numeros
print(10 % 4)

# jerarquia de ejecucion aritmetica
# 1ero aritmetica dentro de parentecis
# 2do elevacion o exponenciacion
# 3ro multiplicacion division
# 4to suma resta
# ejemplo: (3 + 2 / 2 * 5)^2 :
print(((3 + 2) / (2*5)) ** 2)

# o
dividendo = (3 + 2)
divisor = (2 * 5)
elevado = 2

print((dividendo / divisor) ** elevado)