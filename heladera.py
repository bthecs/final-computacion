from cocina import Cocina


class Heladeras(Cocina):

    def __init__(self,color,tamaño,peso,marca,efecener,congelador):
        super().__init__(color,tamaño,peso,marca)
        self.efecener = efecener
        self.congelador = congelador
    
    def __str__(self):
        return super().__str__() + ", Eficiencia energetica: {}, Congelador: {}".format(self.efecener,self.congelador)