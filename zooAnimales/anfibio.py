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
    
    def setListado(self, anfibio):
       if isinstance(anfibio, Anfibio):
            self._listado.append(anfibio) 

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
       rana = Anfibio(nombre, edad, "selva", genero, zona, "rojo", True)
       Anfibio.ranas += 1
       Animal.totalAnimales("Anfibios")
       return rana

    def crearSalamandra(self, nombre, edad, genero, zona):
       salamandra = Anfibio(nombre, edad, "selva", genero, zona, "negro y amarillo", False)
       Anfibio.salamandras += 1
       Animal.totalAnimales("Anfibios")
       return salamandra
       
    def movimiento(self):
        return "saltar"