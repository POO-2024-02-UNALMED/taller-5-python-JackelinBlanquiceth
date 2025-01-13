class Animal():
    _totalAnimales = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, zona=None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal._totalAnimales += 1
    def totalPorTipo():
        from zooAnimales.ave import Ave
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil

        return (
        f"Mamiferos : {Mamifero.cantidadMamiferos()}\n"
        f"Aves : {Ave.cantidadAves()}\n"
        f"Reptiles : {Reptil.cantidadReptiles()}\n"
        f"Peces : {Pez.cantidadPeces()}\n"
        f"Anfibios : {Anfibio.cantidadAnfibios()}"
    )

    def toString(self):
        if self._zona is None:
            return (
                f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()}, "
                f"habito en {self.getHabitat()} y mi genero es {self.getGenero()}"
            )
        else:
            return (
                f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()}, "
                f"habito en {self.getHabitat()} y mi genero es {self.getGenero()}, "
                f"la zona en la que me ubico es {self.getZona().getNombre()}, en el {self.getZona().getZoo().getNombre()}"
            )


    @staticmethod
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
