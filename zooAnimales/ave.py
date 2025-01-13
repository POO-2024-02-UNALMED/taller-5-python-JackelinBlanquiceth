from zooAnimales.animal import Animal

class Ave(Animal):
   halcones = 0
   aguilas = 0
   _listado = []
   def __init__(self,nombre=None, edad=None, habitat=None, genero=None, colorPlumas=None):
      super().__init__(nombre, edad, habitat, genero)
      Ave._listado.append(self)
      self._colorPlumas = colorPlumas
   @classmethod
   def getListado(cls):
      return cls._listado
   
   @classmethod
   def setListado(cls, ave):
      cls._listado.append(ave)

   def getColorPlumas(self):
      return self._colorPlumas
   
   def setColorPlumas(self, color):
      self._colorPlumas = color

   @classmethod
   def cantidadAves(cls):
      return len(cls._listado)
   @classmethod
   def crearHalcon(cls, nombre, edad, genero):
      Ave.halcones += 1
      halcon = Ave(nombre, edad, "montañas", genero, "café glorioso")
      return halcon
   @classmethod
   def crearAguila(cls, nombre, edad, genero):
      Ave.aguilas += 1
      aguila = Ave(nombre, edad, "montañas", genero, "blanco y amarillo")
      return aguila
   @staticmethod  
   def movimiento():
      return "volar"
   
   def toString(self):
      return f"Mi nombre es {self.getNombre}, tengo una edad de {self.getEdad}, habito en {self.getHabitat} y mi genero es\
         {self.getGenero}"