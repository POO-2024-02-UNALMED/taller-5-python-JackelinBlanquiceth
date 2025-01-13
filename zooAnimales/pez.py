from zooAnimales.animal import Animal

class Pez(Animal):
    salmones = 0
    bacalaos = 0
    _listado = []
    def __init__(self, nombre, edad, habitat, genero, colorEscamas =None, cantAletas =None):
        super().__init__(nombre, edad, habitat, genero)
        Pez._listado.append(self)
        self._colorEscamas = colorEscamas
        self._cantidadAletas =cantAletas

    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)
    @classmethod
    def crearSalmon(self, nombre, edad, genero):
        Pez.salmones +=1
        salmon = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        return salmon
    @classmethod
    def crearBacalao(self, nombre, edad, genero):
        Pez.bacalaos +=1
        bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6)
        return bacalao
    def novimiento(self):
        return "nadar"
    def getListado(self):
        return self._listado
    def setListado(self, list):
        self._listado = list
    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self, colEs):
        self._colorEscamas =colEs
    def getCantidadAletas(self):
        return self._cantidadAletas
    def setCantidadAletas(self, cantAletas):
        self._cantidadAletas = cantAletas