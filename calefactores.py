from climatizacion import Climatizacion

class Calefactores(Climatizacion):

    def __init__(self,color,tamaño,peso,marca,tipo,kcal):
        super().__init__(color,tamaño,peso,marca)
        self.tipo = tipo
        self.kcal = kcal

    def __str__(self):
        return super().__str__() + ", Tipo: {}, Kcal/hora: {}".format(self.tipo,self.kcal)