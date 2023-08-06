class Auto:
    # para crear un constructor de la clase utilizamos __init__
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        
    # para crear un metodo debemos siempre pasarle self para su correcto uso
    def encender(self):
        print("El auto se encendio")
        

auto = Auto("hiunday", "i20 MT", "2023")
print(auto.marca)
auto.encender()





class Estudiante:
    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso
        
    def estudiar(self):
        print(self.nombre, "esta estudiando", self.curso)
    
nombre = input("Ingrese su nombre: ")
curso = input("Ingrese el curso: ")
estudiante = Estudiante(nombre, curso)

print(estudiante.nombre)
estudiante.estudiar()
        
        