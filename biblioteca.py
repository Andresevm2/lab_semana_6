import modelos_biblioteca

def main():
    print("=== INICIO DE PRUEBAS DE LA BIBLIOTECA ===")
    
    # Inicializar las estructuras de datos vacías
    inventario = {}
    categorias = set()
    usuarios = {}
    
    # 1. Registrar libros y categorías
    modelos_biblioteca.registrar_libro(inventario, "978-0132350884", "Clean Code", "Robert C. Martin", "Tecnología", categorias)
    modelos_biblioteca.registrar_libro(inventario, "978-0201633610", "Design Patterns", "Erich Gamma", "Tecnología", categorias)
    modelos_biblioteca.registrar_libro(inventario, "978-8437604947", "Don Quijote", "Miguel de Cervantes", "Literatura", categorias)
    
    print("\n[Categorías únicas recopiladas]:", categorias)
    print("[Inventario inicial de libros]:", inventario)
    
    # 2. Registrar un usuario
    modelos_biblioteca.registrar_usuario(usuarios, "U001", "Andrés")
    print("\n[Usuarios registrados]:", usuarios)
    
    # 3. Realizar el préstamo de un libro
    print("\n--- Procesando Préstamo ---")
    modelos_biblioteca.prestar_libro("978-0132350884", "U001", inventario, usuarios)
    
    # 4. Ver estado final
    print("\n[Inventario después del préstamo]:", inventario)
    print("[Estado actualizado del usuario U001]:", usuarios["U001"])
    print("\n=== FIN DE LAS PRUEBAS ===")


if __name__ == "__main__":
    main()