class Animal:
    _totalAnimales = 0
    def __init__(self, nombre, edad, habitat, genero, zona):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal._totalAnimales +=1
   
    def totalPorTipo(cls):
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        from zooAnimales.ave import Ave
        return "Mamiferos : " + str(Mamifero.cantidadMamiferos()) + "\n" + "Aves : " + str(Ave.cantidadAves()) + "\n" + "Reptiles : " + str(Reptil.cantidadReptiles()) + "\n" + "Peces : " + str(Pez.cantidadPeces()) + "\n" +"Anfibios : " + str(Anfibio.cantidadAnfibios())
        return
    
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
        if self._zona is None:
           return (f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()} \
                , habito en {self.getHabitat()} y mi género es {self.getGenero()}")
        else:
            return (f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()} \
                , habito en {self.getHabitat()} y mi género es {self.getGenero()}, \
                la zona en la que me ubico es {self.getZona()}, en el {self._zona.getNombre()}.")