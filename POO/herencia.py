class Persona: 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
# heredamos al poner el nombre de la clase dentro del parentesis
class Estudiante(Persona):
    def __init__(self, curso, tutor, nombre, edad):
        # cuando heredamos debemos representar las propiedades heredadas con super() 
        super().__init__(nombre, edad)
        self.curso = curso
        self.tutor = tutor


estudiante = Estudiante("Desarrollo", "Profesor X","Pedro", 20)
print(estudiante.curso, estudiante.tutor, estudiante.nombre, estudiante.edad)




class Deportista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    
    def imprimirHabilidad(self):
        print("Mi habilidad es: ", self.habilidad)

# herencia multiple al poner mas de una clase dentro del parentesis
class EstudianteDeportista(Persona, Deportista):
    def __init__(self, salario, equipo, nombre, edad, habilidad):
        ''' cuando heredamos mas de una clase 
            debemos representar las propiedades heredadas 
            utilizando cada clase 
        '''
        Persona.__init__(self, nombre, edad)
        Deportista.__init__(self, habilidad)
        
        self.salario = salario
        self.equipo = equipo
        
    # podemos acceder a los metodos de la clase heredada podemos utilizar super()
    def datosDeportista(self):
        return super().imprimirHabilidad()

estudianteDeportista = EstudianteDeportista("50000", "Colo-colo", "Pedro", 20, "Rapidez")
print(estudianteDeportista.salario, estudianteDeportista.equipo, estudianteDeportista.edad)
estudianteDeportista.datosDeportista()