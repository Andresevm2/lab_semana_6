def agregar_categoria(categorias: set, nueva_categoria: str) -> set:
    """Agrega una categoría al conjunto y retorna el conjunto actualizado."""
    categorias.add(nueva_categoria)
    return categorias


def registrar_libro(inventario: dict, isbn: str, titulo: str, autor: str, categoria: str, categorias: set):
    """
    Crea una tupla con la información del libro, la guarda en el inventario usando el ISBN,
    actualiza las categorías y retorna ambos elementos.
    """
    # Tupla con datos fijos del libro
    metadatos_libro = (titulo, autor, categoria)
    
    # Asignar al diccionario del inventario
    inventario[isbn] = metadatos_libro
    
    # Agregar la categoría al conjunto
    agregar_categoria(categorias, categoria)
    
    return inventario, categorias


def registrar_usuario(usuarios: dict, id_usuario: str, nombre: str) -> dict:
    """Registra un usuario con su nombre y una lista vacía para sus libros prestados."""
    usuarios[id_usuario] = {
        "nombre": nombre,
        "libros_prestados": []
    }
    return usuarios


def prestar_libro(isbn: str, id_usuario: str, inventario: dict, usuarios: dict) -> dict:
    """Gestiona el préstamo verificando existencias, moviendo el ISBN y actualizando el inventario."""
    if isbn not in inventario:
        print(f"Error: El libro con ISBN {isbn} no está disponible.")
        return inventario
        
    if id_usuario not in usuarios:
        print(f"Error: El usuario con ID {id_usuario} no existe.")
        return inventario
        
    # Mover el libro al historial del usuario
    usuarios[id_usuario]["libros_prestados"].append(isbn)
    
    # Eliminar del inventario activo
    del inventario[isbn]
    
    print(f"Préstamo exitoso: Libro {isbn} entregado a {usuarios[id_usuario]['nombre']}.")
    return inventario