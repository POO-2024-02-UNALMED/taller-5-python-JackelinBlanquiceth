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
    
    def setListado(self, mamifero):
       if isinstance(mamifero, Mamifero):
          self._listado.append(mamifero)

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
       caballo = Mamifero(nombre, edad, "pradera", genero, zona, True, 4)
       Mamifero.caballos += 1
       Animal.totalAnimales("Mamiferos")
       return caballo

    def crearLeon(self, nombre, edad, genero, zona):
       leon = Mamifero(nombre, edad, "selva", genero, zona, True, 4)
       Mamifero.leones += 1
       Animal.totalAnimales("Mamiferos")
       return leon
       