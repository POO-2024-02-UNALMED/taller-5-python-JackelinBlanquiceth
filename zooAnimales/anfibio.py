from animal import Animal
class Anfibio(Animal):
    ranas = 0
    salamandras = 0
    def __init__(self, nombre, edad, habitat, genero, zona, colorPiel, venenoso):
      super().__init__(nombre, edad, habitat, genero, zona)
      self._listado = []
      self._colorPiel = colorPiel
      self._venenoso = venenoso
    
    def getListado(self):
       return self._listado
    
    def setListado(self, Anfibio):
       self._listado.append(Anfibio)

    def getColorPiel(self):
       return self._colorPiel
    
    def setColorPiel(self, color):
       self._colorPiel = color

    def getVenenoso(self):
       return self._venenoso
    
    def setVenenoso(self, venenoso):
       self._venenoso = venenoso

    def cantidadAnfibios(self):
       return (Anfibio.ranas + Anfibio.salamandras)
    
    def crearRana(self, nombre, edad, genero, zona):
       self.setColorPiel("rojo")
       self.setVenenoso(True)
       self.setHabitat("selva")
       self.setNombre(nombre)
       self.setEdad(edad)
       self.setGenero(genero)
       self.setZona(zona)
       Anfibio.ranas += 1

    def crearSalamandra(self, nombre, edad, genero, zona):
       self.setColorPiel("negro y amarillo")
       self.setVenenoso(False)
       self.setHabitat("selva")
       self.setNombre(nombre)
       self.setEdad(edad)
       self.setGenero(genero)
       self.setZona(zona)
       Anfibio.salamandras += 1
       
    def movimiento(self):
        return "saltar"