from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel=None, venenoso=None):
        super().__init__(nombre, edad, habitat, genero)
        Anfibio._listado.append(self)
        self._colorPiel = colorPiel
        self._venenoso = venenoso

    @classmethod
    def getListado(cls):
        return cls._listado

    @classmethod
    def setListado(cls, anfibio):
        cls._listado = anfibio

    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self, color):
        self._colorPiel = color

    def isVenenoso(self):
        return self._venenoso

    def setVenenoso(self, venenoso):
        self._venenoso = venenoso

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.ranas += 1
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        return rana

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.salamandras += 1
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        return salamandra

    @staticmethod
    def movimiento():
        return "saltar"

    def toString(self):
        return (
            f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()}, "
            f"habito en {self.getHabitat()} y mi genero es {self.getGenero()}"
        )
