from animal import Animal
class Reptil(Animal):
    iguanas = 0
    serpientes = 0
    def __init__(self,nombre, edad, habitat, genero, zona, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._listado = []
        self._colorEscamas = colorEscamas
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

    def cantidadAnfibios(self):
       return (Reptil.iguanas + Reptil.serpientes)
    
    def crearIguana(self, nombre, edad, genero, zona):
       iguana = Reptil(nombre, edad, "humedal", genero, zona, "verde", 3 )
       Reptil.iguanas += 1
       Animal.totalAnimales("Reptiles")
       return iguana

    def crearSerpiente(self, nombre, edad, genero, zona):
       serpiente = Reptil(nombre, edad, "jungla", genero, zona, "blanco", 1 )
       Animal.totalAnimales("Reptiles")
       Reptil.serpientes += 1
       return serpiente
       
    def movimiento(self):
        return "reptar"