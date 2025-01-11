from zooAnimales.animal import Animal
class Ave(Animal):
   halcones = 0
   aguilas = 0
   _listado = []
   def __init__(self,nombre, edad, habitat, genero, colorPlumas):
      super().__init__(nombre, edad, habitat, genero)
      Ave._listado.append(self)
      self._colorPlumas = colorPlumas

   def getListado(self):
      return self._listado
   
   def setListado(self, ave):
      self._listado = ave

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
      aguila = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
      return aguila
      
   def movimiento(self):
      return "volar"