class Libro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"Libro prestado correctamente.")
        else:
            print(f"El libro no está disponible.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print("Libro devuelto correctamente.")
        else:
            print("El libro ya estaba disponible.")

    def mostrar_estado(self):
        estado = "Libro disponible." if self.disponible else "El libro no está disponible."
        print(estado)


libro = Libro(
    "Don Quijote de la Mancha",
    "Miguel de Cervantes"
)


libro.mostrar_estado()

# COMPLETAR:
# Prestar el libro
libro.prestar()

# COMPLETAR:
# Mostrar nuevamente el estado
libro.mostrar_estado()

# COMPLETAR:
# Intentar prestar nuevamente el libro
libro.prestar()

# COMPLETAR:
# Devolver el libro
libro.devolver()