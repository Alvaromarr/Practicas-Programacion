# utils.py
import pickle
from clases import Libro, Revista
from excepciones import ErrorBiblioteca, ErrorArchivo

def leer_entero_positivo(prompt: str) -> int:
    """Extensión de utils.py: Lee y valida un entero positivo, maneja excepciones[cite: 54]."""
    while True:
        try:
            valor = input(prompt)
            numero = int(valor)
            if numero <= 0:
                # Usar la excepción personalizada para valores no válidos [cite: 44]
                raise ErrorBiblioteca("El valor debe ser un entero positivo.")
            return numero
        except ValueError:
            print("Error: Entrada no es un entero válido.")
        except ErrorBiblioteca as e:
            print(f"Error de validación: {e}")

def leer_cadena_no_vacia(prompt: str) -> str:
    """Lee y valida una cadena de texto no vacía."""
    while True:
        try:
            cadena = input(prompt).strip()
            if not cadena:
                # Usar la excepción personalizada para valores vacíos [cite: 44]
                raise ErrorBiblioteca("La cadena de texto no puede estar vacía.")
            return cadena
        except ErrorBiblioteca as e:
            print(f"Error de validación: {e}")

def guardar_publicaciones(publicaciones: list, nombre_fichero: str):
    """Guarda todas las publicaciones en un fichero usando pickle[cite: 47, 55]."""
    try:
        with open(nombre_fichero, 'wb') as f:
            pickle.dump(publicaciones, f)
        print(f"✅ Publicaciones guardadas con éxito en '{nombre_fichero}'.")
    except IOError as e:
        # Captura errores de IO y lanza la excepción personalizada [cite: 49]
        raise ErrorArchivo(f"Error al guardar el fichero: {e}")

def cargar_publicaciones(nombre_fichero: str) -> list:
    """Carga publicaciones desde un fichero usando pickle[cite: 50, 55]."""
    try:
        with open(nombre_fichero, 'rb') as f:
            publicaciones = pickle.load(f)
            
            # Verificación básica para asegurar que el formato es correcto [cite: 51]
            if not isinstance(publicaciones, list):
                raise ErrorArchivo("El formato del fichero es incorrecto (no es una lista).")
                
            return publicaciones
    except FileNotFoundError:
        # Captura errores si el fichero no existe [cite: 51]
        raise ErrorArchivo(f"Error: El fichero '{nombre_fichero}' no se encontró.")
    except EOFError:
        # Captura errores si el fichero está vacío [cite: 51]
        raise ErrorArchivo(f"Error: El fichero '{nombre_fichero}' está vacío.")
    except pickle.UnpicklingError:
        # Captura errores si el formato es incorrecto (no es un objeto serializado) [cite: 51]
        raise ErrorArchivo(f"Error: El fichero '{nombre_fichero}' tiene un formato incorrecto o corrupto.")
    except IOError as e:
        # Captura otros errores de IO
        raise ErrorArchivo(f"Error al cargar el fichero: {e}")