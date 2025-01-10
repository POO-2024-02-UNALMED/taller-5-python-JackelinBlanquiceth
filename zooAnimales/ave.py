from animal import Animal
class Ave(Animal):
    halcones = 0
    aguilas = 0
    def __init__(self,nombre, edad, habitat, genero, zona, colorPlumas):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._listado = []
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

    def cantidadAnfibios(self):
       return (Ave.halcones + Ave.aguilas)
    
    def crearHalcon(self, nombre, edad, genero, zona):
       halcon = Ave(nombre, edad, "montañas", genero, zona, "café glorioso")
       Ave.halcones += 1
       Animal.totalAnimales("Aves")
       return halcon

    def crearAguila(self, nombre, edad, genero, zona):
       aguila = Ave(nombre, edad, "montanas", genero, zona, "blanco y amarillo")
       Ave.aguilas += 1
       Animal.totalAnimales("Aves")
       return aguila
       
    def movimiento(self):
        return "volar"