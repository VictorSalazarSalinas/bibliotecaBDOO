class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def mostrar_informacion(self):
        print(f"Título: {self.titulo} | Autor: {self.autor} | Año: {self.anio}")


# NO MODIFICAR
libro1 = Libro(
    "Cien años de soledad",
    "Gabriel García Márquez",
    1967
)

libro2 = Libro(
    "El principito",
    "Antoine de Saint-Exupéry",
    1943
)


# COMPLETAR:
# Crear al menos un tercer libro
libro3 = Libro(
    "1984",
    "George Orwell",
    1949
)

# Mostrar la información de todos los libros
libro1.mostrar_informacion()
libro2.mostrar_informacion()
libro3.mostrar_informacion()

"""
explicacion
Estado:es el conjunto de valores que contienen los atributos de un objeto en un momento determinado
Propiedades:son las variables asociadas al objeto que definen sus características 
Comportamiento:son las funciones o acciones que el objeto puede realizar o ejecutar operando sobre su propio estado
"""