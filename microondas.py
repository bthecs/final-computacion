from cocina import Cocina

class Microondas(Cocina):

    def __init__(self,color,tamaño,peso,marca,potencia):
        super().__init__(color,tamaño,peso,marca)
        self.potencia = potencia
    
    def __str__(self):
        return super().__str__() + ", Potencia: {}".format(self.potencia)