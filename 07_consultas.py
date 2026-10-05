from ZODB import DB
from ZODB.FileStorage import FileStorage


storage = FileStorage("biblioteca.fs")

# COMPLETAR
db = DB(storage)

# COMPLETAR
connection = db.open()

# COMPLETAR
root = connection.root()


# CONSULTA 1
# Mostrar todos los libros

print("\n--- LIBROS ---")

# COMPLETAR
for libro in root.get("libros", []):
    autor_nombre = libro.autor.nombre if hasattr(libro.autor, 'nombre') else libro.autor
    print(f"Título: {libro.titulo} | Autor: {autor_nombre} | ISBN: {getattr(libro, 'isbn', 'N/A')}")


# CONSULTA 2
# Buscar un libro por título

titulo_buscar = "1984"

# COMPLETAR
print(f"\n--- BÚSQUEDA DE LIBRO: '{titulo_buscar}' ---")
encontrado = False
for libro in root.get("libros", []):
    if libro.titulo.lower() == titulo_buscar.lower():
        autor_nombre = libro.autor.nombre if hasattr(libro.autor, 'nombre') else libro.autor
        print(f"Encontrado: {libro.titulo} por {autor_nombre} (Disponible: {libro.disponible})")
        encontrado = True
        break

if not encontrado:
    print("Libro no encontrado.")


# CONSULTA 3
# Mostrar únicamente libros disponibles

print("\n--- LIBROS DISPONIBLES ---")

# COMPLETAR
for libro in root.get("libros", []):
    if libro.disponible:
        print(f"- {libro.titulo}")


# CONSULTA 4
# Buscar libros publicados después del año 2000

print("\n--- LIBROS DESPUÉS DEL AÑO 2000 ---")

# COMPLETAR
for libro in root.get("libros", []):
    anio = getattr(libro, "anio", 0)
    if anio > 2000:
        print(f"- {libro.titulo} ({anio})")


connection.close()
db.close()