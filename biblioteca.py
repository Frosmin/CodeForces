from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# Clase abstracta para representar un elemento de biblioteca
class ElementoBiblioteca(ABC):
    def __init__(self, titulo, codigo, año):
        self._titulo = titulo
        self._codigo = codigo
        self._año = año
        self._disponible = True
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def codigo(self):
        return self._codigo
    
    @property
    def disponible(self):
        return self._disponible
    
    @disponible.setter
    def disponible(self, valor):
        self._disponible = valor
    
    def __str__(self):
        estado = "disponible" if self._disponible else "prestado"
        return f"{self._titulo} ({self._año}) - {estado}"
    
    @abstractmethod
    def informacion_detallada(self):
        pass


# Clases derivadas para diferentes tipos de elementos
class Libro(ElementoBiblioteca):
    def __init__(self, titulo, codigo, año, autor, editorial, genero, paginas):
        super().__init__(titulo, codigo, año)
        self._autor = autor
        self._editorial = editorial
        self._genero = genero
        self._paginas = paginas
    
    def informacion_detallada(self):
        return (f"LIBRO: {self._titulo}\n"
                f"Autor: {self._autor}\n"
                f"Editorial: {self._editorial}\n"
                f"Género: {self._genero}\n"
                f"Año: {self._año}\n"
                f"Páginas: {self._paginas}")


class Revista(ElementoBiblioteca):
    def __init__(self, titulo, codigo, año, editor, numero, categoria):
        super().__init__(titulo, codigo, año)
        self._editor = editor
        self._numero = numero
        self._categoria = categoria
    
    def informacion_detallada(self):
        return (f"REVISTA: {self._titulo}\n"
                f"Editor: {self._editor}\n"
                f"Número: {self._numero}\n"
                f"Categoría: {self._categoria}\n"
                f"Año: {self._año}")


class DVD(ElementoBiblioteca):
    def __init__(self, titulo, codigo, año, director, duracion, genero):
        super().__init__(titulo, codigo, año)
        self._director = director
        self._duracion = duracion
        self._genero = genero
    
    def informacion_detallada(self):
        return (f"DVD: {self._titulo}\n"
                f"Director: {self._director}\n"
                f"Duración: {self._duracion} minutos\n"
                f"Género: {self._genero}\n"
                f"Año: {self._año}")


# Clase para representar a un usuario de la biblioteca
class Usuario:
    def __init__(self, id, nombre, email):
        self._id = id
        self._nombre = nombre
        self._email = email
        self._prestamos = []
        self._historico = []
    
    @property
    def id(self):
        return self._id
    
    @property
    def nombre(self):
        return self._nombre
    
    def __str__(self):
        return f"Usuario: {self._nombre} (ID: {self._id})"
    
    def tiene_prestamo(self, elemento):
        return any(prestamo["elemento"].codigo == elemento.codigo for prestamo in self._prestamos)
    
    def cantidad_prestamos(self):
        return len(self._prestamos)


# Clase para manejar excepciones personalizadas
class BibliotecaError(Exception):
    """Clase base para excepciones de la biblioteca"""
    pass

class ElementoNoDisponibleError(BibliotecaError):
    """Excepción lanzada cuando un elemento no está disponible"""
    pass

class LimitePrestamoExcedidoError(BibliotecaError):
    """Excepción lanzada cuando un usuario supera el límite de préstamos"""
    pass


# Clase principal que gestiona la biblioteca
class Biblioteca:
    def __init__(self, nombre):
        self._nombre = nombre
        self._catalogo = {}
        self._usuarios = {}
        self._MAX_PRESTAMOS = 3
        self._DIAS_PRESTAMO = 15
    
    def agregar_elemento(self, elemento):
        if elemento.codigo in self._catalogo:
            raise ValueError(f"Ya existe un elemento con el código {elemento.codigo}")
        self._catalogo[elemento.codigo] = elemento
        return True
    
    def registrar_usuario(self, usuario):
        if usuario.id in self._usuarios:
            raise ValueError(f"Ya existe un usuario con ID {usuario.id}")
        self._usuarios[usuario.id] = usuario
        return True
    
    def buscar_por_titulo(self, titulo):
        return [elem for elem in self._catalogo.values() if titulo.lower() in elem.titulo.lower()]
    
    def realizar_prestamo(self, codigo_elemento, id_usuario):
        # Verificamos que existan el elemento y el usuario
        if codigo_elemento not in self._catalogo:
            raise ValueError(f"No existe un elemento con código {codigo_elemento}")
        if id_usuario not in self._usuarios:
            raise ValueError(f"No existe un usuario con ID {id_usuario}")
        
        elemento = self._catalogo[codigo_elemento]
        usuario = self._usuarios[id_usuario]
        
        # Verificamos que el elemento esté disponible
        if not elemento.disponible:
            raise ElementoNoDisponibleError(f"El elemento '{elemento.titulo}' no está disponible")
        
        # Verificamos que el usuario no exceda el límite de préstamos
        if usuario.cantidad_prestamos() >= self._MAX_PRESTAMOS:
            raise LimitePrestamoExcedidoError(f"El usuario ha alcanzado el límite de {self._MAX_PRESTAMOS} préstamos")
        
        # Realizamos el préstamo
        fecha_prestamo = datetime.now()
        fecha_devolucion = fecha_prestamo + timedelta(days=self._DIAS_PRESTAMO)
        
        prestamo = {
            "elemento": elemento,
            "fecha_prestamo": fecha_prestamo,
            "fecha_devolucion": fecha_devolucion
        }
        
        usuario._prestamos.append(prestamo)
        elemento.disponible = False
        
        return prestamo
    
    def devolver_elemento(self, codigo_elemento, id_usuario):
        # Verificamos que existan el elemento y el usuario
        if codigo_elemento not in self._catalogo:
            raise ValueError(f"No existe un elemento con código {codigo_elemento}")
        if id_usuario not in self._usuarios:
            raise ValueError(f"No existe un usuario con ID {id_usuario}")
        
        elemento = self._catalogo[codigo_elemento]
        usuario = self._usuarios[id_usuario]
        
        # Buscamos el préstamo
        for i, prestamo in enumerate(usuario._prestamos):
            if prestamo["elemento"].codigo == codigo_elemento:
                # Registramos en el histórico
                prestamo["fecha_devolucion_real"] = datetime.now()
                usuario._historico.append(prestamo)
                
                # Eliminamos del registro de préstamos activos
                usuario._prestamos.pop(i)
                
                # Marcamos el elemento como disponible
                elemento.disponible = True
                
                return prestamo
        
        raise ValueError(f"El usuario no tiene prestado el elemento con código {codigo_elemento}")
    
    def listar_elementos(self):
        return list(self._catalogo.values())
    
    def listar_usuarios(self):
        return list(self._usuarios.values())


# Ejemplo de uso
if __name__ == "__main__":
    # Creamos la biblioteca
    biblioteca = Biblioteca("Biblioteca Municipal")
    
    # Agregamos algunos elementos al catálogo
    libro1 = Libro("Cien años de soledad", "L001", 1967, "Gabriel García Márquez", 
                  "Sudamericana", "Realismo mágico", 471)
    libro2 = Libro("1984", "L002", 1949, "George Orwell", "Secker & Warburg", 
                  "Distopía", 326)
    revista1 = Revista("National Geographic", "R001", 2023, "National Geographic Society", 
                      "Mayo 2023", "Ciencia")
    dvd1 = DVD("El Padrino", "D001", 1972, "Francis Ford Coppola", 175, "Drama")
    
    biblioteca.agregar_elemento(libro1)
    biblioteca.agregar_elemento(libro2)
    biblioteca.agregar_elemento(revista1)
    biblioteca.agregar_elemento(dvd1)
    
    # Registramos usuarios
    usuario1 = Usuario("U001", "Ana García", "ana@email.com")
    usuario2 = Usuario("U002", "Carlos López", "carlos@email.com")
    
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)
    
    # Realizamos préstamos
    try:
        prestamo1 = biblioteca.realizar_prestamo("L001", "U001")
        print(f"Préstamo realizado: {prestamo1['elemento']} a {usuario1.nombre}")
        
        prestamo2 = biblioteca.realizar_prestamo("R001", "U001")
        print(f"Préstamo realizado: {prestamo2['elemento']} a {usuario1.nombre}")
        
        prestamo3 = biblioteca.realizar_prestamo("D001", "U002")
        print(f"Préstamo realizado: {prestamo3['elemento']} a {usuario2.nombre}")
        
        # Intentamos prestar un libro que ya está prestado
        prestamo_error = biblioteca.realizar_prestamo("L001", "U002")
    except ElementoNoDisponibleError as e:
        print(f"Error: {e}")
    except LimitePrestamoExcedidoError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    
    # Devolvemos un elemento
    try:
        devolucion = biblioteca.devolver_elemento("L001", "U001")
        print(f"Devolución realizada: {devolucion['elemento'].titulo}")
        
        # Verificamos que ahora está disponible
        print(f"Estado actual: {libro1}")
    except Exception as e:
        print(f"Error en devolución: {e}")
    
    # Mostramos información detallada
    print("\n----- INFORMACIÓN DETALLADA -----")
    print(libro1.informacion_detallada())
    print("\n" + revista1.informacion_detallada())
    print("\n" + dvd1.informacion_detallada())
    
    # Buscamos por título
    print("\n----- BÚSQUEDA POR TÍTULO -----")
    resultados = biblioteca.buscar_por_titulo("El")
    for elemento in resultados:
        print(elemento)