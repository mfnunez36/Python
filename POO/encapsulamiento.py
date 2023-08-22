# los atributos solo deben ser utilizados dentro de su clase
class A():
    def __init__(self):
        # encapsulamos los atributos con guion bajo
        self._contador = 0
        
    def incrementar(self):
        self._contador += 1
        
    def cuenta(self):
        return self._contador
    
a = A()

print(a.cuenta())
a.incrementar()
print(a.cuenta())
# no puede ser accedido ya que es un atributo encapsulado
print(a._contador)