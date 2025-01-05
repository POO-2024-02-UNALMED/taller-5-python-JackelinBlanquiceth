from gestion.zoologico import Zoologico
class Animal:
    _totalAnimales = {"Mammiferos":0, "Aves":0, "Reptiles":0, "Peces":0, "Anfibios":0}
    def __init__(self, nombre, edad, habitat, genero, zona):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
    @classmethod
    def totalPorTipo(cls):
        return cls.totalAnimales
    
    def movimiento(self):
        return "desplazarse"
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad  

    def getHabitat(self):
        return self._habitat
    
    def setHabitat(self, habitat):
        self._habitat = habitat
    
    def getGenero(self):
        return self._genero
    
    def setGenero(self, genero):
        self._genero = genero

    def getZona(self):
        return self._zona
    
    def setZona(self, zona):
        self._zona = zona

    def __str__(self):
        if self._zona == None:
          print(f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()} /
                , habito en {self.getHabitat()} y mi género es {self.getGenero()}")
        else:
            print(f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()} /
                , habito en {self.getHabitat()} y mi género es {self.getGenero()}, /
                la zona en la que me ubico es {self.getZona()}, en el {Zoologico.getNombre()}.")