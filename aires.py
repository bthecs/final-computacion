from climatizacion import Climatizacion

class Aires(Climatizacion):

    def __init__(self,color,tamaño,peso,marca,potencia,frigorias):
        super().__init__(color,tamaño,peso,marca)
        self.potencia = potencia
        self.frigorias = frigorias

    def __str__(self):
        return super().__str__() + ", Potencia: {}, Frigorias: {}".format(self.potencia,self.frigorias)