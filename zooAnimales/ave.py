from animal import Animal
class Ave(Animal):
    halcones = 0
    aguilas = 0
    _listado = []
    def __init__(self,nombre, edad, habitat, genero, zona, colorPlumas):
        super().__init__(nombre, edad, habitat, genero, zona)
        Ave._listado.append(self)
        self._colorPlumas = colorPlumas

    def getListado(self):
       return self._listado
    
    def setListado(self, ave):
       if isinstance(ave, Ave):
          self._listado.append(ave)

    def getColorPlumas(self):
       return self._colorPlumas
    
    def setColorPlumas(self, color):
       self._colorPlumas = color

    @classmethod
    def cantidadAves(cls):
       return len(cls._listado)
    @classmethod
    def crearHalcon(self, nombre, edad, genero, zona):
       halcon = Ave(nombre, edad, "montañas", genero, zona, "café glorioso")
       Ave.halcones += 1
       return halcon
    @classmethod
    def crearAguila(self, nombre, edad, genero, zona):
       aguila = Ave(nombre, edad, "montanas", genero, zona, "blanco y amarillo")
       Ave.aguilas += 1
       return aguila
       
    def movimiento(self):
        return "volar"