from zooAnimales.animal import Animal
class Pez(Animal):
    salmones = 0
    bacalaos = 0
    _listado = []
    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, zona=None, colorEscamas=None, cantidadAletas=None):
        super().__init__(nombre, edad, habitat, genero, zona)
        Pez._listado.append(self)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, color):
        self._colorEscamas = color
    @classmethod
    def getListado(cls):
        return cls._listado
    @classmethod
    def setListado(self, peces):
        self._listado = peces    

    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self, cantidad):
        self._cantidadAletas = cantidad
    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)
    @staticmethod
    def movimiento(self):
        return "nadar"
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        Pez.salmones += 1
        salmon = Pez(nombre, edad,"oceano", genero, "rojo", 6)
        return salmon
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        Pez.bacalaos += 1
        bacalao = Pez(nombre, edad,"oceano", genero, "gris", 6)
        return bacalao
    def toString(self):
      return f"Mi nombre es {self.getNombre}, tengo una edad de {self.getEdad}, habito en {self.getHabitat} y mi genero es\
         {self.getGenero}"

