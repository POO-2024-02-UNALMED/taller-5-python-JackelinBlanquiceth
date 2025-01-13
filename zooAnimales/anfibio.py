from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel =None, venenoso =None):
        super().__init__(nombre, edad, habitat, genero)
        Anfibio._listado.append(self)
        self._colorPiel = colorPiel
        self._venenoso = venenoso

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
    @classmethod
    def crearRana(self, nombre, edad, genero):
        Anfibio.ranas +=1
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        return rana
    @classmethod
    def crearSalamandra(self, nombre, edad, genero):
        Anfibio.salamandras +=1
        sala = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        return sala
    def novimiento(self):
        return "saltar"
    def getListado(self):
        return self._listado
    def setListado(self, list):
        self._listado = list
    def getColorPiel(self):
        return self._colorPiel
    def setColorPiel(self, colPi):
        self._colorPiel = colPi
    def isVenenoso(self):
        return self._venenoso
    def setVenenoso(self, ven):
        self._venenoso = ven