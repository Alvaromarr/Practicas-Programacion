from Empleado import Empleado
from Cliente import Cliente

class RegistroDiario:
    def __init__(self):
        self._personas = []

    def agregar_persona(self, persona):
        if isinstance(persona, (Empleado, Cliente)):
            self._personas.append(persona)
        else:
            raise TypeError("Solo se aceptan Empleado o Cliente")

    def visualizar_registro(self):
        if not self._personas:
            print("Registro vacío")
        for p in self._personas:
            p.visualizar()
            print("-" * 30)

    def es_empleado(self, persona):
        return isinstance(persona, Empleado)

    def visualizar_empleados(self):
        hay = False
        for p in self._personas:
            if isinstance(p, Empleado):
                p.visualizar()
                print("-" * 30)
                hay = True
        if not hay:
            print("No hay empleados en el registro")

    def __getitem__(self, index):
        return self._personas[index]

    def __add__(self, other):
        if not isinstance(other, RegistroDiario):
            return NotImplemented
        nuevo = RegistroDiario()
        for p in self._personas:
            nuevo.agregar_persona(p)
        for p in other._personas:
            nuevo.agregar_persona(p)
        return nuevo