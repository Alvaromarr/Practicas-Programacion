# Cliente.py
from Ficha import Ficha

class Cliente(Ficha):
    def __init__(self, nombre="", edad=0, nacio=None, dni=""):
        from Time import Time
        if nacio is None:
            nacio = Time(0, 0, 0)
        super().__init__(nombre, edad, nacio)
        self._dni = dni

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, valor):
        self._dni = valor

    def visualizar(self):
        print("=== CLIENTE ===")
        super().visualizar()
        print(f"DNI: {self._dni}")

    def __eq__(self, other):
        if not isinstance(other, Cliente):
            return NotImplemented
        return self.nombre == other.nombre and self.edad == other.edad
