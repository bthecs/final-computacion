#clases

class Vehiculo:

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format(self.color,self.ruedas)

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindradas):
        super().__init__(color,ruedas)
        self.velocidad = velocidad
        self.cilindradas = cilindradas

    def __str__(self):
        return super().__str__() + ",{} Km/h, {} cilindradas".format(self.velocidad, self.cilindradas)

class Camioneta(Coche):

    def __init__(self, color, ruedas, velocidad, cilindradas, carga):
        super().__init__(color, ruedas, velocidad, cilindradas)
        self.carga = carga

    def __str__(self):
        return super().__str__() + ",{} Kg".format(self.carga)



class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo


    def __str__(self):
        return super().__str__() + ",tipo {}".format(self.tipo)


class Motocicleta(Bicicleta):
    
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} Km/h, {} cc".format(self.velocidad, self.cilindrada)




# def catalogar(vehiculos):
#    for v in vehiculos:
#        print(type(v).__name__, v)


def catalogar(vehiculos, ruedas=None):

    # Primera pasada, mostrar recuento
    if ruedas != None:
        contador = 0
        for v in vehiculos:
            if v.ruedas == ruedas: 
                contador += 1
        print("\nSe han encontrado {} vehículos con {} ruedas:".format(
            contador, ruedas))

    # Segnda pasada, mostrar vehículos
    for v in vehiculos:
        if ruedas == None:
            print(type(v).__name__, v)
        else:
            if v.ruedas == ruedas:
                print(type(v).__name__, v)




lista = [
    Coche("azul", 4, 150, 1200),
    Camioneta("blanco", 4, 100, 1300, 1500),
    Bicicleta("verde", 2, "urbana"),
    Motocicleta("negro", 2, "deportiva", 180, 900)
]

catalogar(lista)
catalogar(lista, 0)
catalogar(lista, 2)
catalogar(lista, 4)

for i in lista:
    print(i)