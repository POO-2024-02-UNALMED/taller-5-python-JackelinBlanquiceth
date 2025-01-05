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
    
    def setListado(self, Reptil):
       self._listado.append(Reptil)

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
       self.setColorEscamas("verde")
       self.setLargoCola(3)
       self.setHabitat("humedal")
       self.setNombre(nombre)
       self.setEdad(edad)
       self.setGenero(genero)
       self.setZona(zona)
       Reptil.iguanas += 1

    def crearSalamandra(self, nombre, edad, genero, zona):
       self.setColorEscamas("blanco")
       self.setLargoCola(1)
       self.setHabitat("jungla")
       self.setNombre(nombre)
       self.setEdad(edad)
       self.setGenero(genero)
       self.setZona(zona)
       Reptil.serpientes += 1
       
    def movimiento(self):
        return "reptar"