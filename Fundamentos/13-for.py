lenguajes = ["phyton", "C#", "Java", "Javascript", "Go", "C++"]

# recorrer lista
for item in lenguajes:
    print(item)
    

# con range podemos dar un rango de recorrido 
# devuelve la posicion 
for item in range(1, 5):
    print(item)
    
print("--break--")
# para interrumpir la ejecucion utilizamos break
for item in range(2, 5):
    print(item)
    if (item == 4):
        break
    

print("--continue--")
# para continuar fuera de la iteracion utilizamos continue
for item in range(2, 5):
    print(item)
    if (item == 3):
        continue

print("ya esta fuera")