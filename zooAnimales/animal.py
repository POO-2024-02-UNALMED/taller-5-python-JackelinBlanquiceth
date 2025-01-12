class Animal():
    _totalAnimales = 0
    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, zona=None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal._totalAnimales += 1
    
    def totalPorTipo(self):
        from ave import Ave
        from anfibio import Anfibio
        from mamifero import Mamifero
        from pez import Pez
        from reptil import Reptil
        return "Mamiferos : " + str(Mamifero.cantidadMamiferos()) + "\n" \
        + "Aves : " + str(Ave.cantidadAves()) + "\n" + "Reptiles : " + str(Reptil.cantidadReptiles()) + "\n" \
        + "Peces : " + str(Pez.cantidadPeces()) + "\n" +"Anfibios : " + str(Anfibio.cantidadAnfibios())
    
    def toString(self):
        from gestion.zona import Zona
        if self._zona is None:
            return f"Mi nombre es {self.getNombre}, tengo una edad de {self.getEdad}, habito en {self.getHabitat}t \
                y mi g enero es {self.getGenero}."
        else:
            return f"Mi nombre es {self.getNombre}, tengo una edad de {self.getEdad}, habito en {self.getHabitat}t \
                y mi g enero es {self.getGenero}, la zona en la que me ubico es {self.getZona}, en el {self.getZoo}."
        
    def movimiento():
        return "desplazarse"
    
    def getNombre(self):
        return self._nombre
    def setNombre(self, nom):
        self._nombre = nom
    def getEdad(self):
        return self._edad
    def setEdad(self, edad):
        self._edad = edad
    def getHabitat(self):
        return self._habitat
    def setHabitat(self, habi):
        self._habitat = habi
    def getGenero(self):
        return self._genero
    def setGenero(self, gene):
        self._genero = gene
    def getZona(self):
        return self._zona
    def setZona(self, zona):
        self._zona = zona
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    @classmethod
    def setTotalAnimales(cls, total):
        cls._totalAnimales = total



        
        

