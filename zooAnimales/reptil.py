from zooAnimales.animal import Animal

class Reptil(Animal):
    iguanas = 0
    serpientes = 0
    _listado = []
    def __init__(self, nombre, edad, habitat, genero, colorEscamas =None, largoCola =None):
        super().__init__(nombre, edad, habitat, genero)
        Reptil._listado.append(self)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
    
    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)
    @classmethod
    def crearIguana(self, nombre, edad, genero):
        Reptil.iguanas +=1
        iguana = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        return iguana
    @classmethod
    def crearSerpiente(self, nombre, edad, genero):
        Reptil.serpientes +=1
        serp = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        return serp
    def novimiento(self):
        return "resptar"
    def getListado(self):
        return self._listado
    def setListado(self, list):
        self._listado = list
    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self, colEs):
        self._colorEscamas =colEs
    def getLargoCola(self):
        return self._largoCola
    def setLargoCola(self, larCol):
        self._largoCola =larCol