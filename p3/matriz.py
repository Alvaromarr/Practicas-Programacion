# matriz.py
import numpy as np

class CMatFloat:
    """
    Clase que representa una matriz dinámica 1D/2D basada en numpy.
    Atributos:
        _Matriz (np.ndarray | None)
        _m_nFilas (int)
        _m_nColumnas (int)
    """

    def __init__(self):
        """
        Inicializa la matriz a None y filas/columnas a 0.
        """
        self._Matriz = None
        self._m_nFilas = 0
        self._m_nColumnas = 0

    def CrearMatriz2D(self, nFilas: int, nColumnas: int):
        """
        Crea matriz bidimensional de ceros con dimensiones dadas.
        """
        if not isinstance(nFilas, int) or not isinstance(nColumnas, int):
            raise TypeError("nFilas y nColumnas deben ser enteros")
        if nFilas <= 0 or nColumnas <= 0:
            raise ValueError("nFilas y nColumnas deben ser > 0")
        self._Matriz = np.zeros((nFilas, nColumnas), dtype=float)
        self._m_nFilas = nFilas
        self._m_nColumnas = nColumnas

    def CrearMatriz1D(self, nElementos: int):
        """
        Crea matriz unidimensional (1 x nElementos) de ceros.
        """
        self.CrearMatriz2D(1, nElementos)

    def Introducir(self, lector_float=None):
        """
        Introduce elementos de la matriz como números decimales.
        lector_float: función compatible con leer_float(mensaje) para inyección de dependencia en tests.
        """
        if not self.Existe():
            raise RuntimeError("La matriz no existe; créala antes")
        if lector_float is None:
            lector_float = leer_float

        for i in range(self._m_nFilas):
            for j in range(self._m_nColumnas):
                val = lector_float(f"Elemento[{i},{j}]: ")
                self._Matriz[i, j] = float(val)

    def Mostrar(self):
        """
        Muestra los elementos de la matriz.
        """
        if not self.Existe():
            print("No hay matriz para mostrar")
            return
        # Formateo compacto si es 1D
        if self._m_nFilas == 1:
            fila = "  ".join(f"{x:.6g}" for x in self._Matriz[0, :])
            print(f"[ {fila} ]")
        else:
            for i in range(self._m_nFilas):
                fila = "  ".join(f"{x:.6g}" for x in self._Matriz[i, :])
                print(f"[ {fila} ]")

    def Existe(self) -> bool:
        """
        Verifica si la matriz está creada y no vacía.
        """
        return isinstance(self._Matriz, np.ndarray) and self._Matriz.size > 0

    def SumarMatrices(self, otra_matriz: "CMatFloat") -> np.ndarray:
        """
        Suma la matriz actual con otra matriz (dimensiones deben coincidir).
        Retorna: numpy.ndarray con el resultado.
        """
        if not self.Existe() or not otra_matriz or not otra_matriz.Existe():
            raise RuntimeError("Ambas matrices deben existir")
        if self._Matriz.shape != otra_matriz._Matriz.shape:
            raise ValueError("Las dimensiones no coinciden")
        return self._Matriz + otra_matriz._Matriz

    def RestarMatrices(self, otra_matriz: "CMatFloat") -> np.ndarray:
        """
        Resta la matriz actual con otra matriz (dimensiones deben coincidir).
        Retorna: numpy.ndarray con el resultado.
        """
        if not self.Existe() or not otra_matriz or not otra_matriz.Existe():
            raise RuntimeError("Ambas matrices deben existir")
        if self._Matriz.shape != otra_matriz._Matriz.shape:
            raise ValueError("Las dimensiones no coinciden")
        return self._Matriz - otra_matriz._Matriz


def leer_int(mensaje: str = "Introduce un número entero: ") -> int:
    """
    Lee un entero del teclado; repite hasta valor válido.
    """
    while True:
        try:
            txt = input(mensaje)
            return int(txt.strip())
        except (ValueError, TypeError):
            print("Entrada no válida; introduce un entero.")


def leer_float(mensaje: str = "Introduce un número decimal: ") -> float:
    """
    Lee un float del teclado; repite hasta valor válido.
    """
    while True:
        try:
            txt = input(mensaje)
            return float(txt.strip().replace(",", "."))
        except (ValueError, TypeError):
            print("Entrada no válida; introduce un número decimal.")


def crear_menu(opciones_menu: list[str]) -> int:
    """
    Muestra un menú numerado desde 1 y retorna la opción elegida dentro del rango.
    """
    if not opciones_menu:
        raise ValueError("El menú no puede estar vacío")
    for idx, opc in enumerate(opciones_menu, start=1):
        print(f"{idx}. {opc}")
    while True:
        sel = leer_int("Selecciona una opción: ")
        if 1 <= sel <= len(opciones_menu):
            return sel
        print(f"Opción inválida; elige entre 1 y {len(opciones_menu)}.")
