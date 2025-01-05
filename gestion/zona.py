from zooAnimales.animal import Animal
class Zona:
    def __init__(self, nombre, zoo, animales):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []

    def agregarAnimales(self, Animal):
        self._animales.append(Animal)

    def cantidadAnimales(self):
        return len(self._animales)
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getZoo(self):
        return self._zoo
    
    def setZoo(self, zoo):
        self._zoo = zoo
    
    def getAnimales(self):
        return self._animales