class Animal:
    _totalAnimales = 0
    def __init__(self, nombre=None, edad =None, habitat=None, genero=None,zona=None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        self._totalAnimales +=1

    def novimiento(self):
        return "desplazarse"
    
    def totalPorTipo():
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        from zooAnimales.ave import Ave
        return "Mamiferos : " + str(Mamifero.cantidadMamiferos()) + "\n" + "Aves : " + str(Ave.cantidadAves()) + "\n" + "Reptiles : " + str(Reptil.cantidadReptiles()) + "\n" + "Peces : " + str(Pez.cantidadPeces()) + "\n" +"Anfibios : " + str(Anfibio.cantidadAnfibios())
    def toString(self):
        if self._zona ==None:
            return "Mi nombre es "+ str(self.getNombre())+", tengo una edad de " +str(self.getEdad())+ ", habito en "+str(self.getHabitat())+" y mi genero es "+str(self.getGenero())
        else:
            return "Mi nombre es "+ str(self.getNombre())+", tengo una edad de " +str(self.getEdad())+ ", habito en "+str(self.getHabitat())+" y mi genero es "+str(self.getGenero())+", la zona en la que me ubico es "+str(self.getZona().getNombre())+", en el "+ str(self.getZona().getZoo().getNombre())+"."
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
    def setGenero(self, gen):
        self._genero = gen
    def getZona(self):
        return self._zona
    def setZona(self, zon):
        self._zona = zon
    def getTotalAnimales(self):
        return self._totalAnimales
    def setTotalAnimales(self, totAn):
        self._totalAnimales = totAn