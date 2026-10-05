from persistent import Persistent
from persistent.mapping import PersistentMapping
from persistent.list import PersistentList
from ZODB import DB
from ZODB.FileStorage import FileStorage
import transaction


class Autor(Persistent):

    def __init__(self, nombre):
        self.nombre = nombre


class Libro(Persistent):

    def __init__(self, titulo, isbn, autor, anio=2000, editorial="", categoria="", numero_paginas=0):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor
        self.anio = anio
        self.editorial = editorial
        self.categoria = categoria
        self.numero_paginas = numero_paginas
        self.disponible = True


class Usuario(Persistent):

    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula

        # COMPLETAR
        self.prestamos = PersistentList()


class Prestamo(Persistent):

    def __init__(self, usuario, libro, fecha):
        self.usuario = usuario
        self.libro = libro

        # COMPLETAR
        self.fecha = fecha
        
        # Actualizar disponibilidad
        self.libro.disponible = False


# Conexión y poblado de la base de datos
storage = FileStorage("biblioteca.fs")
db = DB(storage)
connection = db.open()
root = connection.root()

# Inicializar listas persistentes
root["autores"] = PersistentList()
root["libros"] = PersistentList()
root["usuarios"] = PersistentList()
root["prestamos"] = PersistentList()

# 3 Autores
a1 = Autor("Gabriel García Márquez")
a2 = Autor("George Orwell")
a3 = Autor("Carlos Ruiz Zafón")
root["autores"].extend([a1, a2, a3])

# 5 Libros (asociados a autores)
l1 = Libro("Cien años de soledad", "9780307474728", a1, 1967, "Editorial Sudamericana", "Novela", 471)
l2 = Libro("El amor en los tiempos del cólera", "9780307387264", a1, 1985, "Oveja Negra", "Novela", 368)
l3 = Libro("1984", "9780451524935", a2, 1949, "Secker & Warburg", "Distopía", 328)
l4 = Libro("Rebelión en la granja", "9780451526342", a2, 1945, "Secker & Warburg", "Fábula", 112)
l5 = Libro("La sombra del viento", "9788408163381", a3, 2001, "Planeta", "Misterio", 576)
root["libros"].extend([l1, l2, l3, l4, l5])

# 3 Usuarios
u1 = Usuario("Laura Gómez", "U001")
u2 = Usuario("Carlos Pérez", "U002")
u3 = Usuario("María López", "U003")
root["usuarios"].extend([u1, u2, u3])

# Registrar préstamos y relaciones
p1 = Prestamo(u1, l3, "2026-03-01")
u1.prestamos.append(p1)

p2 = Prestamo(u2, l5, "2026-03-02")
u2.prestamos.append(p2)

root["prestamos"].extend([p1, p2])

transaction.commit()
print("Estructura de BDOO creada y guardada correctamente.")

connection.close()
db.close()