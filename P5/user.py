from dataclasses import dataclass, field
from typing import List

@dataclass
class User:
    """
    Representa un usuario de la biblioteca con nombre, ID e historial de préstamos.

    Attributes
    ----------
    _name : str
        Nombre del usuario (privado).
    _id : str
        Identificador único del usuario (privado).
    _borrowed_isbns : List[str]
        Lista de ISBN de libros actualmente prestados (privado).
    """
    _name: str
    _id: str
    _borrowed_isbns: List[str] = field(default_factory=list)

    @property
    def name(self) -> str:
        """Obtiene el nombre del usuario."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Establece el nombre del usuario."""
        self._name = value

    @property
    def id(self) -> str:
        """Obtiene el identificador del usuario."""
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        """Establece el identificador del usuario."""
        self._id = value

    @property
    def borrowed_isbns(self) -> List[str]:
        """Obtiene la lista de ISBN de libros prestados por el usuario."""
        return self._borrowed_isbns

    @borrowed_isbns.setter
    def borrowed_isbns(self, value: List[str]) -> None:
        """Establece la lista de ISBN de libros prestados por el usuario."""
        self._borrowed_isbns = list(value)

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena con los datos del usuario.

        Returns
        -------
        str
            Cadena con nombre, ID y lista de libros prestados.
        """
        libros = ", ".join(self._borrowed_isbns) if self._borrowed_isbns else "Sin préstamos"
        return f"{self._name} | ID:{self._id} | Libros:{libros}"
