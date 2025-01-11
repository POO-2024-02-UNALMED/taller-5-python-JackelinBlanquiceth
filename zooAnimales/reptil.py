from animal import Animal
class Reptil(Animal):
    iguanas = 0
    serpientes = 0
    _listado = []
    def __init__(self,nombre, edad, habitat, genero, zona, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorEscamas = colorEscamas
        Reptil._listado.append(self)
        self._largoCola = largoCola

    def getListado(self):
       return self._listado
    
    def setListado(self, reptil):
       if isinstance(reptil, Reptil):
            self._listado.append(reptil) 

    def getColorEscamas(self):
       return self._colorEscamas
    
    def setColorEscamas(self, color):
       self._colorEscamas = color

    def getLargoCola(self):
       return self._largoCola
    
    def setLargoCola(self, largo):
       self._largoCola = largo
    @classmethod
    def cantidadReptiles(cls):
       return len(cls._listado)
    @classmethod
    def crearIguana(cls, nombre, edad, genero, zona):
       iguana = Reptil(nombre, edad, "humedal", genero, zona, "verde", 3 )
       Reptil.iguanas += 1
       return iguana
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero, zona):
       serpiente = Reptil(nombre, edad, "jungla", genero, zona, "blanco", 1 )
       Reptil.serpientes += 1
       return serpiente
       
    def movimiento(self):
        return "reptar"