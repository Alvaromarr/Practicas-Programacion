from dataclasses import dataclass

@dataclass
class Book:
    """
    Representa un libro con título, autor, ISBN y estado de préstamo.

    Attributes
    ----------
    _title : str
        Título del libro (privado).
    _author : str
        Autor del libro (privado).
    _isbn : str
        Identificador ISBN (privado).
    _borrowed : bool
        Estado de préstamo: True si está prestado, False si disponible.
    """
    _title: str
    _author: str
    _isbn: str
    _borrowed: bool = False

    @property
    def title(self) -> str:
        """Obtiene el título del libro."""
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        """Establece el título del libro."""
        self._title = value

    @property
    def author(self) -> str:
        """Obtiene el autor del libro."""
        return self._author

    @author.setter
    def author(self, value: str) -> None:
        """Establece el autor del libro."""
        self._author = value

    @property
    def isbn(self) -> str:
        """Obtiene el ISBN del libro."""
        return self._isbn

    @isbn.setter
    def isbn(self, value: str) -> None:
        """Establece el ISBN del libro."""
        self._isbn = value

    @property
    def borrowed(self) -> bool:
        """Indica si el libro está prestado (True) o disponible (False)."""
        return self._borrowed

    @borrowed.setter
    def borrowed(self, value: bool) -> None:
        """Establece el estado de préstamo del libro."""
        self._borrowed = bool(value)

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena con todos los datos del libro.

        Returns
        -------
        str
            Cadena con título, autor, ISBN y estado.
        """
        estado = "Prestado" if self._borrowed else "Disponible"
        return f"{self._title} | {self._author} | ISBN:{self._isbn} | {estado}"
