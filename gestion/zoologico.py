class Zoologico():
    def __init__(self, nombre=None, ubicacion=None):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre
        
    def getUbicacion(self):
        return self._ubicacion
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion
        
    def getZona(self):
        return self._zonas
    def agregarZonas(self, zona):
        self._zonas.append(zona)
        
    def cantidadTotalAnimales(self):
        cantidadTotal = 0
        for zona in self._zonas:
            cantidadTotal += zona.cantidadAnimales()
        return cantidadTotal
    def toString(self):
        return (
            f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()}, "
            f"habito en {self.getHabitat()} y mi genero es {self.getGenero()}"
        )

