from final import Electrodomesticos
from cocina import Cocina
from microondas import Microondas
from heladera import Heladeras
from climatizacion import Climatizacion
from aires import Aires
from calefactores import Calefactores
from StackQueue import StackQueue


class Main():

    def run(self):
        L = StackQueue()

        while True:
            print("""
                1.Añadir electrodomestico
                2.Mostrar todos los electrodomesticos
                3.Eliminar el primer electrodomesticos
                4.Eliminar el ultimo electrodomesticos
                5.Comprobar si la lista esta vacia
                6.Salir
                """)
            
            opt = input("Ingrese opcion: ")
            print("\n")
            if opt == "1":

               color = input("Ingrese el color: ")
               tamaño = int(input("Ingrese 2 para cocina y 4 para climatizador: "))

               if tamaño == 2:
                   cocina_peso = int(input("Ingrese el peso de la cocina: "))
                   cocina_marca = input("Ingrese la marca: ")

                   opC = input("¿Si es un microondas presione M si es una heladera presione H y si es una cocina presione C? Y/N/C: ")
                   if opC.upper() == "M":
                       microondas_potencia = int(input("Ingrese la potencia: "))
                       L.push(Microondas(color,tamaño,cocina_peso,cocina_marca,microondas_potencia))
                   elif opC.upper() == "H":
                       heladeras_efecener = input("Ingrese la eficiencia energetica: ")
                       heladeras_congelador = input("Ingrese si posee congelador: ")
                       L.push(Heladeras(color,tamaño,cocina_peso,cocina_marca,heladeras_efecener,heladeras_congelador))
                   elif opC.upper() == "C":
                       L.push(Cocina(color,tamaño,cocina_peso,cocina_marca))
                
               else:
                   climati_peso = int(input("Ingrese el peso: "))
                   climati_marca = input("Ingrese marca: ")

                   opC1 = input("Ingrese A si es un Aireacondicionado y C si es un calefactor: ")
                   if opC1.upper() == "A":
                       aire_potencia = int(input("Ingrese potencia: "))
                       aire_frigorias = int(input("Ingrese frigorias: "))
                       L.push(str(Aires(color,tamaño,climati_peso,climati_marca,aire_potencia,aire_frigorias)))
                   elif opC1.upper() == "C":
                       cale_tipo = input("Ingrese si es electrico o gas: ")
                       cale_kcal = int(input("Ingrese Kcal/hora: "))
                       L.push(str(Calefactores(color,tamaño,climati_peso,climati_marca,cale_tipo,cale_kcal)))
            
            if opt == "2":
                print("\nExtraído de la Clase StackQueue:")
                cola = L.getLista()
                list(set(cola))
                for i in cola:
                    print(i)
                

            if opt == "3":
                L.eliminar()
            
            if opt == "4":
                L.pop()

            if opt == "5":
                L.is_empty()
                   
            if opt == "6":
                break

