from animal import Animal
class Reptil(Animal):
   iguanas = 0
   serpientes = 0
   _listado = []
   def __init__(self,nombre=None, edad=None, habitat=None, genero=None, colorEscamas=None, largoCola=None):
      super().__init__(nombre, edad, habitat, genero)
      self._colorEscamas = colorEscamas
      Reptil._listado.append(self)
      self._largoCola = largoCola
   @classmethod
   def getListado(cls):
      return cls._listado
   @classmethod
   def setListado(cls, reptil):
      cls._listado.append(reptil) 

   def getColorEscamas(self):
      return self._colorEscamas
   
   def setColorEscamas(self, color):
      self._colorEscamas = color

   def getLargoCola(self):
      return self._largoCola
   
   def setLargoCola(self, largo):
      self._largoCola = largo
   @classmethod
   def cantidadReptiles(cls):
      return len(cls._listado)
   @classmethod
   def crearIguana(cls, nombre, edad, genero):
      Reptil.iguanas += 1
      iguana = Reptil(nombre, edad, "humedal", genero, "verde", 3 )
      return iguana
   @classmethod
   def crearSerpiente(cls, nombre, edad, genero):
      Reptil.serpientes += 1
      serpiente = Reptil(nombre, edad, "jungla", genero, "blanco", 1 )
      return serpiente
   @staticmethod  
   def movimiento():
      return "reptar"
   def toString(self):
      return f"Mi nombre es {self.getNombre}, tengo una edad de {self.getEdad}, habito en {self.getHabitat} y mi genero es\
         {self.getGenero}"