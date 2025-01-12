from  zooAnimales.animal import Animal

class Mamifero(Animal):
   caballos = 0
   leones = 0
   _listado = []
   def __init__(self,nombre=None, edad=None, habitat=None, genero=None, pelaje=None, patas=None):
      super().__init__(nombre, edad, habitat, genero)
      Mamifero._listado.append(self)
      self._pelaje = pelaje
      self._patas = patas
   @classmethod
   def getListado(self):
      return self._listado   
   @classmethod
   def setListado(self, mamifero):
      self._listado.append(mamifero)
   def getPelaje(self):
      return self._pelaje   
   def isPelaje(self, pelaje):
      self._pelaje = pelaje
   def getPatas(self):
      return self._patas    
   def setPatas(self, patas):
      self._patas = patas

   @classmethod
   def cantidadMamiferos(cls):
      return len(cls._listado)
   @classmethod
   def crearCaballo(cls, nombre, edad, genero):
      Mamifero.caballos += 1
      caballo = Mamifero(nombre, edad, "pradera", genero, True, 4)
      return caballo
   @classmethod
   def crearLeon(cls, nombre, edad, genero):
      Mamifero.leones += 1
      leon = Mamifero(nombre, edad, "selva", genero, True, 4)
      return leon
   def toString(self):
      return f"Mi nombre es {self.getNombre}, tengo una edad de {self.getEdad}, habito en {self.getHabitat} y mi genero es\
         {self.getGenero}"
      