# manejo de expectiones ejemplo de ingresar un tipo de dato erroneo 
try:
    monto = int(input("ingrese su monto: "))
    print('monto: {}'.format(monto))
except ValueError:
    print('el tipo de dato que ingreso es incorrecto')
finally:
    print('finalizo')