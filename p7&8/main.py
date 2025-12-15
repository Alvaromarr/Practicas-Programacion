# main.py
from clases import Libro, Revista, Publicacion
from excepciones import ErrorBiblioteca, ErrorArchivo
from utils import (
    leer_entero_positivo,
    leer_cadena_no_vacia,
    guardar_publicaciones,
    cargar_publicaciones
)

def agregar_publicacion(publicaciones: list[Publicacion]):
    """Opción 1: Permite al usuario registrar un nuevo Libro o Revista."""
    print("\n--- Añadir Publicación ---")
    
    while True:
        tipo = input("Desea añadir un (L)ibro o una (R)evista? ").upper()
        if tipo in ['L', 'R']:
            break
        print("Opción no válida. Por favor, escriba 'L' o 'R'.")

    try:
        # Recopilación de datos comunes (con validación de utils)
        titulo = leer_cadena_no_vacia("Título: ")
        autor = leer_cadena_no_vacia("Autor: ")
        anio = leer_entero_positivo("Año de Publicación: ")
        
        # Creación de instancia específica (con validación de clases.py)
        if tipo == 'L':
            genero = leer_cadena_no_vacia("Género: ")
            nueva_publicacion = Libro(titulo, autor, anio, genero)
            print("Libro añadido con éxito.")
        elif tipo == 'R':
            num_edicion = leer_entero_positivo("Número de Edición: ")
            nueva_publicacion = Revista(titulo, autor, anio, num_edicion)
            print("Revista añadida con éxito.")
            
        publicaciones.append(nueva_publicacion)

    # Captura las excepciones de validación de utils.py y clases.py
    except ErrorBiblioteca as e:
        print(f"\nError al crear la publicación: {e}")

def mostrar_publicaciones(publicaciones: list[Publicacion]):
    """Opción 2: Muestra en pantalla todas las publicaciones registradas."""
    print("\n--- Catálogo de Publicaciones ---")
    if not publicaciones:
        print("El catálogo está vacío. No hay publicaciones disponibles.")
        return

    # Uso del polimorfismo: cada objeto llama a su propia versión de Descripcion()
    for i, publicacion in enumerate(publicaciones):
        print(f"{i+1}. {publicacion.Descripcion()}")

def guardar_datos(publicaciones: list[Publicacion]):
    """Opción 3: Guarda las publicaciones en un fichero."""
    print("\n--- Guardar Publicaciones ---")
    if not publicaciones:
        print("No hay publicaciones para guardar.")
        return

    try:
        # El nombre del fichero se valida para que no esté vacío
        nombre_fichero = leer_cadena_no_vacia("Introduce el nombre del fichero a guardar (ej. datos.dat): ")
        guardar_publicaciones(publicaciones, nombre_fichero)
    except ErrorArchivo as e:
        print(f"\nError de Archivo: {e}")
    except ErrorBiblioteca as e:
        print(f"\nError de entrada: {e}")

def cargar_datos(publicaciones: list[Publicacion]):
    """Opción 4: Carga publicaciones desde un fichero y las añade al catálogo."""
    print("\n--- Cargar Publicaciones ---")
    
    try:
        # El nombre del fichero se valida para que no esté vacío
        nombre_fichero = leer_cadena_no_vacia("Introduce el nombre del fichero a cargar: ")
        
        # Carga los datos (puede lanzar ErrorArchivo si falla)
        publicaciones_cargadas = cargar_publicaciones(nombre_fichero)
        
        # Se añaden las publicaciones cargadas al catálogo existente
        publicaciones.extend(publicaciones_cargadas)
        print(f"Se han cargado {len(publicaciones_cargadas)} publicaciones y añadido al catálogo.")
        
    except ErrorArchivo as e:
        print(f"\nError de Archivo: {e}")
    except ErrorBiblioteca as e:
        print(f"\nError de entrada: {e}")

def main():
    """Función principal que ejecuta el menú de la biblioteca."""
    # Lista para almacenar objetos Libro y Revista (el catálogo)
    publicaciones: list[Publicacion] = []
    
    while True:
        print("\n===============================")
        print("Biblioteca Digital - MENÚ")
        print("1. Añadir publicaciones (libros o revistas)")
        print("2. Mostrar publicaciones disponibles")
        print("3. Guardar publicaciones en un fichero")
        print("4. Cargar publicaciones desde un fichero")
        print("5. Salir")
        print("===============================")
        
        opcion = input("Elige una opción (1-5): ")
        
        if opcion == '1':
            agregar_publicacion(publicaciones)
        elif opcion == '2':
            mostrar_publicaciones(publicaciones)
        elif opcion == '3':
            guardar_datos(publicaciones)
        elif opcion == '4':
            cargar_datos(publicaciones)
        elif opcion == '5':
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, introduce un número entre 1 y 5.")

if __name__ == "__main__":
    main()