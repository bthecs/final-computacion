class StackQueue():

    def __init__(self):
        self.lista = []

    def getLista(self):
        return (self.lista)

    def push(self, lista): #Metodo para insertar elementos
        self.lista.insert(0,lista)

    def is_empty(self): # Metodo para verificar si la lista esta vacia
        aux = self.lista == []
        if aux == True:
            print("Lista vacía")
        else:
            print("La lista contiene elemnetos")

    def pop(self): #Metodo para eliminar el ultimo elemento de la lista
        return self.lista.pop(0)

    def eliminar(self): #Metodo para eliminar el primer elemento de la lista
        return self.lista.pop()