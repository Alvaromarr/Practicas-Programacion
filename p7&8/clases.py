# clases.py
from excepciones import ErrorBiblioteca

# Clase Base
class Publicacion:
    """Clase base para la gestión de publicaciones."""
    
    def __init__(self, titulo: str, autor: str, anio: int):
        """Inicializa los atributos de la publicación con validación."""
        if not titulo or not autor:
            raise ErrorBiblioteca("Título o autor no pueden estar vacíos.")
        if not isinstance(anio, int) or anio <= 0:
            raise ErrorBiblioteca("El año debe ser un entero positivo.")
            
        # Atributos protegidos [cite: 12]
        self._titulo = titulo
        self._autor = autor
        self._anio = anio

    # Decoradores para acceso al atributo 'titulo' [cite: 16]
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, nuevo_titulo):
        if not nuevo_titulo:
            raise ErrorBiblioteca("El título no puede estar vacío.")
        self._titulo = nuevo_titulo

    # Decoradores para acceso al atributo 'autor' [cite: 16]
    @property
    def autor(self):
        return self._autor
    
    @autor.setter
    def autor(self, nuevo_autor):
        if not nuevo_autor:
            raise ErrorBiblioteca("El autor no puede estar vacío.")
        self._autor = nuevo_autor

    # Decoradores para acceso al atributo 'anio' [cite: 16]
    @property
    def anio(self):
        return self._anio
    
    @anio.setter
    def anio(self, nuevo_anio):
        if not isinstance(nuevo_anio, int) or nuevo_anio <= 0:
            raise ErrorBiblioteca("El año debe ser un entero positivo.")
        self._anio = nuevo_anio

    def Descripcion(self) -> str:
        """Permite visualizar los datos del objeto (se redefine en derivadas)[cite: 17]."""
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio}"


# Clase Derivada: Libro
class Libro(Publicacion):
    """Clase para la gestión de libros."""
    
    def __init__(self, titulo: str, autor: str, anio: int, genero: str):
        """Inicializa los atributos de la base y el género del libro[cite: 23]."""
        super().__init__(titulo, autor, anio)
        
        if not genero:
            raise ErrorBiblioteca("El género no puede estar vacío.")
            
        # Atributo adicional protegido [cite: 19, 21]
        self._genero = genero

    # Decoradores para acceso al atributo 'genero' [cite: 24]
    @property
    def genero(self):
        return self._genero
    
    @genero.setter
    def genero(self, nuevo_genero):
        if not nuevo_genero:
            raise ErrorBiblioteca("El género no puede estar vacío.")
        self._genero = nuevo_genero

    def Descripcion(self) -> str:
        """Muestra los datos del libro[cite: 24]."""
        # Se llama a la descripción de la clase base y se añade el atributo de Libro
        base_desc = super().Descripcion()
        return f"LIBRO: {base_desc}, Género: {self.genero}"


# Clase Derivada: Revista
class Revista(Publicacion):
    """Clase para la gestión de revistas."""
    
    def __init__(self, titulo: str, autor: str, anio: int, num_edicion: int):
        """Inicializa los atributos de la base y el número de edición de la revista[cite: 31]."""
        super().__init__(titulo, autor, anio)
        
        if not isinstance(num_edicion, int) or num_edicion <= 0:
            raise ErrorBiblioteca("El número de edición debe ser un entero positivo.")
            
        # Atributo adicional protegido [cite: 26]
        self._num_edicion = num_edicion

    # Decoradores para acceso al atributo 'num_edicion' [cite: 31]
    @property
    def num_edicion(self):
        return self._num_edicion
    
    @num_edicion.setter
    def num_edicion(self, nuevo_num):
        if not isinstance(nuevo_num, int) or nuevo_num <= 0:
            raise ErrorBiblioteca("El número de edición debe ser un entero positivo.")
        self._num_edicion = nuevo_num

    def Descripcion(self) -> str:
        """Muestra los datos de la revista[cite: 32]."""
        # Se llama a la descripción de la clase base y se añade el atributo de Revista
        base_desc = super().Descripcion()
        return f"REVISTA: {base_desc}, Número de Edición: {self.num_edicion}"