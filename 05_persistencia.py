from ZODB import DB
from ZODB.FileStorage import FileStorage
import persistent
import transaction


class Libro(persistent.Persistent):
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio


# CONEXIÓN A LA BASE DE DATOS

storage = FileStorage("biblioteca.fs")

# COMPLETAR:
db = DB(storage)

# COMPLETAR:
connection = db.open()

# COMPLETAR:
root = connection.root()


# CREAR LIBRO

libro = Libro(
    "La sombra del viento",
    "Carlos Ruiz Zafón",
    2001
)


# COMPLETAR:
# Guardar el libro dentro de root
if "libros" not in root:
    root["libros"] = []
root["libros"].append(libro)


# COMPLETAR:
# Confirmar la transacción
transaction.commit()


print("Libro almacenado correctamente.")


# CERRAR CONEXIONES

connection.close()
db.close()