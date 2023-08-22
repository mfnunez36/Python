class A():
    def __init__(self):
        self._contador = 0
        self._cuenta = 0

    # getters
    @property
    def contador(self):
        return self._contador
    
    @property
    def cuenta(self):
        return self._cuenta
    
    # setters
    @contador.setter
    def contador(self, contador):
        self._contador = contador
    
    @cuenta.setter
    def cuenta(self, cuenta):
        self._cuenta = cuenta
    
    
    def incrementar(self):
        self._contador += 1
        
    def marcador(self):
        return self._contador
a = A()

print(a.marcador())
a.contador = 50
a.incrementar()
print(a.marcador())