class Electrodomesticos():

    def __init__(self,color,tamaño):
        self.color = color
        self.tamaño = tamaño

    def __str__(self):
        return "Color: {} , Tamaño: {}, ".format(self.color,self.tamaño)