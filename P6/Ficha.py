from Time import Time   # de la práctica 3

class Ficha:
    def __init__(self, nombre: str = "", edad: int = 0,
                 nacio: Time = Time(0, 0, 0)):
        self._nombre = nombre
        self._edad = edad
        self._nacio = nacio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        self._edad = valor

    @property
    def nacio(self):
        return self._nacio

    @nacio.setter
    def nacio(self, valor):
        self._nacio = valor

    def visualizar(self):
        print(f"Nombre: {self._nombre}")
        print(f"Edad: {self._edad}")
        print(f"Nació (hora): {self._nacio}")