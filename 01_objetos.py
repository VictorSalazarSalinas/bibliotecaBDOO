class Libro:
    def __init__(self, titulo, autor_nombre, isbn):
        # Propiedades / Estado inicial
        self.titulo = titulo
        self.autor_nombre = autor_nombre
        self.isbn = isbn

    # Comportamiento: Método para mostrar la información del objeto
    def mostrar_informacion(self):
        print(f"Título: {self.titulo} | Autor: {self.autor_nombre} | ISBN: {self.isbn}")


# Crear instancias (objetos)
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "978-0307474728")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "978-8424115807")
# Crear un tercer libro
libro3 = Libro("Pedro Páramo", "Juan Rulfo", "978-8437604183")

# Mostrar todos los libros
biblioteca = [libro1, libro2, libro3]
print("--- LISTA DE LIBROS ---")
for libro in biblioteca:
    libro.mostrar_informacion()

"""
explicacion
Estado:es el conjunto de valores que contienen los atributos de un objeto en un momento determinado
Propiedades:son las variables asociadas al objeto que definen sus características 
Comportamiento:son las funciones o acciones que el objeto puede realizar o ejecutar operando sobre su propio estado
"""