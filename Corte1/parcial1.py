
categorias = ("Tecnologia", "Ropa", "Comida", "Otros")


inventario = []

print("=== BIENVENIDO AL SISTEMA DE INVENTARIO ===")

while True:
    print("\n--- MENÚ ---")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        codigo = input("Código: ")
        nombre_producto = input("Nombre del producto: ")

        if nombre_producto == "":
            print("El nombre no puede estar vacío")
            continue

        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))

        print("Categorías disponibles:", categorias)
        categoria = input("Categoría: ")

        producto = {
            "codigo": codigo,
            "nombre_producto": nombre_producto,
            "precio": precio,
            "cantidad": cantidad,
            "categoria": categoria
        }

        inventario.append(producto)
        print("Producto agregado correctamente")

    elif opcion == "2":
        if len(inventario) == 0:
            print("No hay productos")
        else:
            for p in inventario:
                print("Código:", p["codigo"],
                      "| Nombre:", p["nombre_producto"],
                      "| Precio:", p["precio"],
                      "| Cantidad:", p["cantidad"],
                      "| Categoría:", p["categoria"])

    elif opcion == "3":
        buscar = input("Ingrese el nombre del producto: ")
        encontrado = False

        for p in inventario:
            if p["nombre_producto"] == buscar:
                print("Producto encontrado:", p)
                encontrado = True
        
        if not encontrado:
            print("No se encontró el producto")

    elif opcion == "4":
        eliminar = input("Nombre del producto a eliminar: ")

        for p in inventario:
            if p["nombre_producto"] == eliminar:
                inventario.remove(p)
                print("Producto eliminado")
                break
        else:
            print("Producto no encontrado")

    elif opcion == "5":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")