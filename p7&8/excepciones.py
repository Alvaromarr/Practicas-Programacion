# excepciones.py
class ErrorBiblioteca(Exception):
    """Excepción base para errores en la biblioteca[cite: 34]."""
    def __init__(self, mensaje="Ocurrió un error en la gestión de la biblioteca."):
        # Se sobrescribe el mensaje predeterminado [cite: 35]
        super().__init__(mensaje)

class ErrorArchivo(ErrorBiblioteca):
    """Excepción para problemas relacionados con ficheros[cite: 36]."""
    def __init__(self, mensaje="Ocurrió un error al manipular el archivo."):
        super().__init__(mensaje)