class Libro:

    def __init__(self, titulo, autor, isbn, anio, editorial="", categoria="", numero_paginas=0, disponible=True):

        self.titulo = titulo
        self.autor = autor

        # COMPLETAR
        self.isbn = isbn

        # COMPLETAR
        self.anio = anio

        # COMPLETAR (Propiedades requeridas)
        self.editorial = editorial
        self.categoria = categoria
        self.numero_paginas = numero_paginas

        self.disponible = disponible


libro = Libro(
    "1984",
    "George Orwell",
    "9780451524935",
    1949,
    editorial="Secker & Warburg",
    categoria="Distopía",
    numero_paginas=328
)


print("Título:", libro.titulo)
print("Autor:", libro.autor)

# COMPLETAR:
# Mostrar ISBN
print("ISBN:", libro.isbn)

# COMPLETAR:
# Mostrar año
print("Año:", libro.anio)

# COMPLETAR:
# Mostrar disponibilidad
print("Disponible:", "Sí" if libro.disponible else "No")
print("Editorial:", libro.editorial)
print("Categoría:", libro.categoria)
print("Número de páginas:", libro.numero_paginas)