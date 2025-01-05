from animal import Animal
class Mamifero(Animal):
    caballos = 0
    leones = 0
    def __init__(self,nombre, edad, habitat, genero, zona, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._listado = []
        self._pelaje = pelaje
        self._patas = patas

    def getListado(self):
       return self._listado
    
    def setListado(self, Mamifero):
       self._listado.append(Mamifero)

    def getPelaje(self):
       return self._pelaje
    
    def setPelaje(self, pelaje):
       self._pelaje = pelaje

    def getPatas(self):
       return self._patas
    
    def setPatas(self, patas):
       self._patas = patas

    def cantidadAnfibios(self):
       return (Mamifero.caballos + Mamifero.leones)
    
    def crearCaballo(self, nombre, edad, genero, zona):
       self.setPelaje(True)
       self.setPatas(4)
       self.setHabitat("pradera")
       self.setNombre(nombre)
       self.setEdad(edad)
       self.setGenero(genero)
       self.setZona(zona)
       Mamifero.caballos += 1

    def crearLeon(self, nombre, edad, genero, zona):
       self.setPelaje(True)
       self.setPatas(4)
       self.setHabitat("selva")
       self.setNombre(nombre)
       self.setEdad(edad)
       self.setGenero(genero)
       self.setZona(zona)
       Mamifero.leones += 1
       