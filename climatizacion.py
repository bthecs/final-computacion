from final import Electrodomesticos


class Climatizacion(Electrodomesticos):

    def __init__(self,color,tamaño,peso,marca):
        super().__init__(color,tamaño)
        self.peso = peso
        self.marca = marca

    def __str__(self):
        return super().__str__() + ", Peso: {}, Marca: {}".format(self.peso,self.marca)