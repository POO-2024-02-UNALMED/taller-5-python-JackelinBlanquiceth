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
    
    def setListado(self, Ave):
       self._listado.append(Ave)

    def getColorPlumas(self):
       return self._colorPlumas
    
    def setColorPlumas(self, color):
       self._colorPlumas = color

    def cantidadAnfibios(self):
       return (Ave.halcones + Ave.aguilas)
    
    def crearHalcon(self, nombre, edad, genero, zona):
       self.setColorPlumas("café glorioso")
       self.setHabitat("montañas")
       self.setNombre(nombre)
       self.setEdad(edad)
       self.setGenero(genero)
       self.setZona(zona)
       Ave.halcones += 1

    def crearAguila(self, nombre, edad, genero, zona):
       self.setColorPlumas("blanco y amarillo")
       self.setHabitat("montañas")
       self.setNombre(nombre)
       self.setEdad(edad)
       self.setGenero(genero)
       self.setZona(zona)
       Ave.aguilas += 1
       
    def movimiento(self):
        return "volar"