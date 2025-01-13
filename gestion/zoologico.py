class Zoologico():
    def __init__(self, nombre = None, ubicacion = None):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    def getNombre(self):
        return self._nombre
    def setNombre(self, nom):
        self._nombre = nom

    def getUbicacion(self):
        return self._ubicacion
    def setUbicacion(self, ubi):
        self._ubicacion = ubi

    def agregarZonas(self, zona):
        self._zonas.append(zona)
    def getZona(self):
        return self._zonas

    def cantidadTotalAnimales(self):
        cantidadTotal = 0
        for zona in self._zonas:
            cantidadTotal += zona.cantidadAnimales()
        return cantidadTotal



