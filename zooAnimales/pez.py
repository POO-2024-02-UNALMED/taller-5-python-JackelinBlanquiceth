from animal import Animal
class Pez(Animal):
    salmones = 0
    bacalaos = 0
    def __init__(self, nombre, edad, habitat, genero, zona, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._listado = []
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, color):
        self._colorEscamas = color

    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self, cantidad):
        self._cantidadAletas = cantidad

    def cantidadPeces(self):
        return (Pez.salmones + Pez.bacalaos)
    
    def movimiento(self):
        return "nadar"
    
    def crearSalmon(self, nombre, edad, genero, zona):
        self.setColorEscamas("rojo")
        self.setCantidadAletas(6)
        self.setHabitat("océano")
        self.setNombre(nombre)
        self.setEdad(edad)
        self.setGenero(genero)
        self.setZona(zona)
        Pez.salmones += 1
    
    def crearBacalao(self, nombre, edad, genero, zona):
        self.setColorEscamas("gris")
        self.setCantidadAletas(6)
        self.setHabitat("océano")
        self.setNombre(nombre)
        self.setEdad(edad)
        self.setGenero(genero)
        self.setZona(zona)
        Pez.bacalaos += 1

