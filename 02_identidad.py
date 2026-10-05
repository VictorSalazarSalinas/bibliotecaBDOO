class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

# Se asigna el objeto a libro1
libro1 = Libro("Rayuela", "Julio Cortázar")

# libro1 a libro2 
libro2 = libro1

# Comprobación experimental de identidad
print(f"¿libro1 == libro2? -> {libro1 == libro2}")  
print(f"¿libro1 is libro2? -> {libro1 is libro2}")  
print(f"ID libro1: {id(libro1)}")
print(f"ID libro2: {id(libro2)}")

# Modificar el título de libro1
libro1.titulo = "Rayuela (Edición Conmemorativa)"

# Imprimir las propiedades de ambos objetos
print("\n--- Estado tras modificar libro1.titulo ---")
print(f"Propiedades de Libro 1: Título: '{libro1.titulo}', Autor: '{libro1.autor}'")
print(f"Propiedades de Libro 2: Título: '{libro2.titulo}', Autor: '{libro2.autor}'")

#como libro1 y libro2 comparten la misma identidad en memoria
#modificar libro1 altera automáticamente lo que se visualiza desde libro2