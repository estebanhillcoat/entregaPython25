# Lista donde vamos a guardar los productos, arranca vacía
productos = []

# Función que guarda los productos en un archivo de texto
def escribir():
    # Abrimos el archivo en modo escritura. Si no existe, lo crea.
    with open("base.txt", "w") as base:
        # Por cada producto, lo escribimos en una línea
        for producto in productos:
            base.write(f"{producto}\n")

# Leemos los productos que ya estaban guardados del archivo, si hay
with open("base.txt", "r") as base:
    productos = base.read().splitlines()  # Cortamos por línea, así tenemos una lista

# Arranca el menú para que el usuario elija qué quiere hacer
while True:
    print("\n--- Menú ---")
    print("1) Agregar producto")        # Para sumar uno nuevo
    print("2) Borrar producto")         # Para eliminar uno que ya no va
    print("3) Salir")                   # Cierra el programa
    print("4) Mostrar productos")       # Te muestra todo lo que hay cargado
    print("5) Buscar producto")         # Buscás si hay stock de algo puntual

    opcion = input("Ingrese una opción: ")  # Acá el usuario elige qué hacer

    match opcion:
        case "1":
            # Le pedimos el nombre del nuevo producto
            nuevo_producto = input("Ingrese el nombre del producto: ")
            if nuevo_producto not productos:
                productos.append(nuevo_producto)  # Lo sumamos a la lista
                print(f"Producto '{nuevo_producto}' agregado.")
                escribir()  # Lo guardamos en el archivo
            else:
                print("producto ya en stock")

        case "2":
            # Pedimos cuál quiere eliminar
            borrar_producto = input("Ingrese el nombre del producto a borrar: ")
            if borrar_producto in productos:
                productos.remove(borrar_producto)  # Si está, lo sacamos
                print(f"Producto '{borrar_producto}' borrado.")
                escribir()  # Actualizamos el archivo
            else:
                print(f"El producto '{borrar_producto}' no se encontró en la lista.")

        case "3":
            # Si elige salir, chau programa
            break

        case "4":
            # Mostramos lo que hay en stock
            print("\nLista de productos:")
            for producto in productos:
                print(f"- {producto}")

        case "5":
            # Buscamos un producto específico
            buscar = input("Ingrese el nombre del producto a buscar: ")
            if buscar in productos:
                print(f"Producto '{buscar}' en stock.")
            else:
                print(f"Producto '{buscar}' no encontrado.")

        case _:
            # Por si se manda cualquiera
            print("Opción no válida. Intente nuevamente.")
