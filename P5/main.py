from typing import Optional
from utils import crear_menu, generar_id8
from library import Library
from book import Book
from user import User

def pedir_libro() -> Book:
    """
    Solicita al usuario los datos de un libro por entrada estándar.

    Returns
    -------
    Book
        Instancia creada con título, autor e ISBN proporcionados.
    """
    title = input("Título: ").strip()
    author = input("Autor: ").strip()
    isbn = input("ISBN: ").strip()
    return Book(title, author, isbn)

def pedir_usuario() -> User:
    """
    Solicita el nombre y genera un ID único de 8 caracteres para el usuario.

    Returns
    -------
    User
        Usuario creado con nombre e ID generado automáticamente.
    """
    name = input("Nombre: ").strip()
    uid = generar_id8()
    print(f"ID generado: {uid}")
    return User(name, uid)

def mostrar_libros(lib: Library) -> None:
    """
    Imprime en consola todos los libros de la biblioteca.

    Parameters
    ----------
    lib : Library
        Instancia de biblioteca desde la que leer los libros.
    """
    print("\n-- Libros --")
    for b in lib.all_books():
        print(b)
    if not lib.all_books():
        print("Sin libros")

def mostrar_usuarios(lib: Library) -> None:
    """
    Imprime en consola todos los usuarios de la biblioteca.

    Parameters
    ----------
    lib : Library
        Instancia de biblioteca desde la que leer los usuarios.
    """
    print("\n-- Usuarios --")
    for u in lib.all_users():
        print(u)
    if not lib.all_users():
        print("Sin usuarios")

def buscar(lib: Library) -> None:
    """
    Realiza una búsqueda de libros por título y autor e imprime resultados.

    Parameters
    ----------
    lib : Library
        Instancia de biblioteca sobre la que ejecutar las búsquedas.
    """
    sub = input("Texto a buscar: ").strip()
    print("\nPor título:")
    for b in lib.search_by_title(sub):
        print(b)
    print("\nPor autor:")
    for b in lib.search_by_author(sub):
        print(b)

def main() -> None:
    """
    Punto de entrada de la aplicación de consola de la biblioteca.

    Presenta un menú interactivo para gestionar libros, usuarios y préstamos.
    """
    lib = Library()
    while True:
        sel = crear_menu("Biblioteca", [
            "Añadir libro",
            "Eliminar libro",
            "Registrar usuario",
            "Realizar préstamo",
            "Realizar devolución",
            "Mostrar libros",
            "Mostrar usuarios",
            "Buscar libros",
        ])
        if sel == 0:
            break
        elif sel == 1:
            b = pedir_libro()
            ok = lib.add_book(b)
            print("Añadido" if ok else "Ya existe ese ISBN")
        elif sel == 2:
            isbn = input("ISBN a eliminar: ").strip()
            ok = lib.remove_book(isbn)
            print("Eliminado" if ok else "No se puede eliminar (no existe o está prestado)")
        elif sel == 3:
            u = pedir_usuario()
            ok = lib.register_user(u)
            print("Registrado" if ok else "Ya existe ese usuario")
        elif sel == 4:
            uid = input("ID usuario: ").strip()
            isbn = input("ISBN: ").strip()
            ok = lib.borrow(uid, isbn)
            print("Préstamo realizado" if ok else "No se pudo realizar el préstamo")
        elif sel == 5:
            uid = input("ID usuario: ").strip()
            isbn = input("ISBN: ").strip()
            ok = lib.return_book(uid, isbn)
            print("Devolución realizada" if ok else "No se pudo realizar la devolución")
        elif sel == 6:
            mostrar_libros(lib)
        elif sel == 7:
            mostrar_usuarios(lib)
        elif sel == 8:
            buscar(lib)

if __name__ == "__main__":
    main()
