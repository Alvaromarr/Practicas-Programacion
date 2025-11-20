from typing import Dict, List, Optional
from book import Book
from user import User

class Library:
    """
    Gestiona una colección de libros y usuarios, permitiendo prestar y devolver.

    Mantiene índices por ISBN para libros y por ID para usuarios, con operaciones
    para alta/baja, búsqueda y circulación de materiales.
    """

    def __init__(self) -> None:
        """Inicializa los contenedores internos de libros y usuarios."""
        self._books_by_isbn: Dict[str, Book] = {}
        self._users_by_id: Dict[str, User] = {}

    def add_book(self, book: Book) -> bool:
        """
        Añade un libro a la biblioteca si el ISBN no existe.

        Parameters
        ----------
        book : Book
            Instancia a registrar.

        Returns
        -------
        bool
            True si se añadió, False si el ISBN ya existía.
        """
        if book.isbn in self._books_by_isbn:
            return False
        self._books_by_isbn[book.isbn] = book
        return True

    def remove_book(self, isbn: str) -> bool:
        """
        Elimina un libro por ISBN si existe y no está prestado.

        Parameters
        ----------
        isbn : str
            ISBN del libro a eliminar.

        Returns
        -------
        bool
            True si se eliminó, False si no existe o está prestado.
        """
        bk = self._books_by_isbn.get(isbn)
        if bk is None or bk.borrowed:
            return False
        del self._books_by_isbn[isbn]
        return True

    def search_by_title(self, title_sub: str) -> List[Book]:
        """
        Busca libros cuyo título contenga el texto dado (insensible a mayúsculas).

        Parameters
        ----------
        title_sub : str
            Subcadena a buscar en títulos.

        Returns
        -------
        List[Book]
            Lista de coincidencias.
        """
        key = title_sub.lower()
        return [b for b in self._books_by_isbn.values() if key in b.title.lower()]

    def search_by_author(self, author_sub: str) -> List[Book]:
        """
        Busca libros cuyo autor contenga el texto dado (insensible a mayúsculas).

        Parameters
        ----------
        author_sub : str
            Subcadena a buscar en autores.

        Returns
        -------
        List[Book]
            Lista de coincidencias.
        """
        key = author_sub.lower()
        return [b for b in self._books_by_isbn.values() if key in b.author.lower()]

    def register_user(self, user: User) -> bool:
        """
        Registra un usuario si el ID no existe.

        Parameters
        ----------
        user : User
            Usuario a registrar.

        Returns
        -------
        bool
            True si se registró, False si ya existía el ID.
        """
        if user.id in self._users_by_id:
            return False
        self._users_by_id[user.id] = user
        return True

    def get_user(self, uid: str) -> Optional[User]:
        """
        Recupera un usuario por su ID.

        Parameters
        ----------
        uid : str
            Identificador del usuario.

        Returns
        -------
        Optional[User]
            Usuario encontrado o None.
        """
        return self._users_by_id.get(uid)

    def borrow(self, user_id: str, isbn: str) -> bool:
        """
        Realiza un préstamo si usuario y libro existen y el libro está disponible.

        Parameters
        ----------
        user_id : str
            ID del usuario solicitante.
        isbn : str
            ISBN del libro a prestar.

        Returns
        -------
        bool
            True si se realizó el préstamo, False en caso contrario.
        """
        u = self._users_by_id.get(user_id)
        b = self._books_by_isbn.get(isbn)
        if u is None or b is None or b.borrowed:
            return False
        b.borrowed = True
        u.borrowed_isbns = u.borrowed_isbns + [isbn]
        return True

    def return_book(self, user_id: str, isbn: str) -> bool:
        """
        Registra la devolución de un libro si el préstamo es válido.

        Parameters
        ----------
        user_id : str
            ID del usuario que devuelve.
        isbn : str
            ISBN del libro a devolver.

        Returns
        -------
        bool
            True si se registró la devolución, False en caso contrario.
        """
        u = self._users_by_id.get(user_id)
        b = self._books_by_isbn.get(isbn)
        if u is None or b is None or not b.borrowed or isbn not in u.borrowed_isbns:
            return False
        b.borrowed = False
        u.borrowed_isbns = [x for x in u.borrowed_isbns if x != isbn]
        return True

    def all_books(self) -> List[Book]:
        """
        Devuelve la lista de todos los libros registrados.

        Returns
        -------
        List[Book]
            Colección de libros.
        """
        return list(self._books_by_isbn.values())

    def all_users(self) -> List[User]:
        """
        Devuelve la lista de todos los usuarios registrados.

        Returns
        -------
        List[User]
            Colección de usuarios.
        """
        return list(self._users_by_id.values())
