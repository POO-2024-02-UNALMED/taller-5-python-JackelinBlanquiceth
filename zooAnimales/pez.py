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

    def getListado(self):
        return self._listado

    def setListado(self, peces):
        if isinstance(peces, Pez):
            self._listado.append(peces)    

    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self, cantidad):
        self._cantidadAletas = cantidad

    def cantidadPeces(self):
        return (Pez.salmones + Pez.bacalaos)
    
    def movimiento(self):
        return "nadar"
    
    def crearSalmon(self, nombre, edad, genero, zona):
        salmon = Pez(nombre, edad,"océano", genero, zona, "rojo", 6)
        Animal.totalAnimales("Peces")
        Pez.salmones += 1
        return salmon
    
    def crearBacalao(self, nombre, edad, genero, zona):
        bacalao = Pez(nombre, edad,"océano", genero, zona, "gris", 6)
        Pez.bacalaos += 1
        return bacalao

