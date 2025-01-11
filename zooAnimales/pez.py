from animal import Animal
class Pez(Animal):
    salmones = 0
    bacalaos = 0
    _listado = []
    def __init__(self, nombre, edad, habitat, genero, zona, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero, zona)
        Pez._listado.append(self)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, color):
        self._colorEscamas = color

    def getListado(self):
        return self._listado

    def setListado(self, peces):
        self._listado = peces    

    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self, cantidad):
        self._cantidadAletas = cantidad
    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)
    
    def movimiento(self):
        return "nadar"
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        Pez.salmones += 1
        salmon = Pez(nombre, edad,"océano", genero, "rojo", 6)
        return salmon
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        Pez.bacalaos += 1
        bacalao = Pez(nombre, edad,"océano", genero, "gris", 6)
        return bacalao

