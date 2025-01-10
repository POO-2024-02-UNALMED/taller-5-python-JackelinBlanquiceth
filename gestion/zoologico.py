class Zoologico:
    
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    def agregarZonas(self, zona):
        self._zonas.append(zona)
        
    def cantidadTotalAnimales(self): 
        return sum(zona.cantidadAnimales() for zona in self._zonas)
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getUbicacion(self):
        return self._ubicacion
    
    def setNombre(self, ubicacion):
        self._ubicacion = ubicacion
    
    def getZonas(self):
        return self._zonas
        