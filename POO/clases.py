# pass sirve para seguir adelante
# para crear una clase 
# por convencion en las clases su nombre siempre parte con Mayuscula 
class PrimeraClase():
    pass

print(type(PrimeraClase))


# para crear una clase de tipo funcion
def ObjetoFuncion(): 
    pass

print(type(ObjetoFuncion))




# Self
# self se utiliza para englobar los atributos a nuestra clase
# self se transforma en el contexto de si mismo / con self podemos acceder a sus atributos
class SegundaClase():
    atributo1 = 'valor1'
    atributo2 = 'valor2'
    
    def cambiarAtributo(self):
        self.atributo1 = "nuevo valor1"
        

# creamos (instanciamos) la clase SegundaClase   
clase2 = SegundaClase()
print("marca antes de cambiar es: ", clase2.atributo1)

# ejecutamos su metodo
print(clase2.cambiarAtributo())

print("atributo1 nuevo es: ", clase2.atributo1)



# Atributos inicializados
class Fabrica():
    marca = 'La Marca'
    anio_inicio = '1800'
    # con __ antes de un atributo este queda como un atributo privado
    # que solo sera accedido desde dentro de la clase 
    # a esto se le llama encapsulamiento   
    __cuenta = "4321-123-4324-1232"


# creamos (instanciamos) la clase Fabrica    
fabrica = Fabrica()

# podemos agregar un atributo temporal
fabrica.atributoTmp = "temporal"
print(fabrica.atributoTmp)

# accedemos a sus propiedades
print(fabrica.marca)





# Metodos
class Fabrica2():
    marca = 'La Marca2'
    anio_inicio = '1990'
    
    def metodo1():
        print('metodo1 ejecutado')
        
    def metodo2():
        print('metodo2 ejecutado')

    def entregaPedido(self, pedido):
        print('metodo entregaPedido ejecutado')
        return 'El pedido a entregar es: {}'.format(pedido)

# creamos (instanciamos) la clase Fabrica2   
fabrica2 = Fabrica2()

# llamamos(ejecutamos) su metodo entregaPedido(pedido)
print(fabrica2.entregaPedido(1234))






# __init__ (constructor)
# init sirve para inicializar nuestra clase en el momento que se llama
# init es nuestro metodo constructor de clase
class Fabrica3():
    def __init__(self, marca, anio_inicio):
        self.marca = marca
        self.anio_inicio = anio_inicio
        
        # este print como esta dentro del constructor (__init__) 
        # cuando se instancie la clase se ejecutara
        print(self.marca, self.anio_inicio)
        
# creamos (instanciamos) la clase Fabrica3 
# le pasamos sus parametros dentro del parentesis
fabrica3 = Fabrica3('Marca Fab3', '1990')





# __del__ (destructor)
# sirve para destruir un objeto una vez finalice la ejecucion
# se ejecuta al final de todo el codigo / es el ultimo metodo a ejecutar 
class Fabrica4():
    def __init__(self, marca, anio_inicio):
        self.marca = marca
        self.anio_inicio = anio_inicio
        
        # este print como esta dentro del constructor (__init__) 
        # cuando se instancie la clase se ejecutara
        print('Se creo la fabrica 4 {}, {}'.format(self.marca, self.anio_inicio))
        
    def __del__(self):
        print('el objeto ha sido destruido')
        
# creamos (instanciamos) la clase Fabrica4 
# le pasamos sus parametros dentro del parentesis
fabrica4 = Fabrica4('Marca Fab3', '1990')
print(fabrica4)   