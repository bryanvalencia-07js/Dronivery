from sistema.SistemaDronivery import SistemaDronivery


def mostrar_menu():
    print("\n===== DRONIVERY.PY =====")
    print("1. Registrar dron")
    print("2. Ver drones")
    print("3. Registrar producto")
    print("4. Ver productos")
    print("5. Crear pedido")
    print("6. Ver pedidos")
    print("7. Salir")


def main():
    sistema = SistemaDronivery()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sistema.registrar_dron()

        elif opcion == "2":
            sistema.ver_drones()

        elif opcion == "3":
            sistema.registrar_producto()

        elif opcion == "4":
            sistema.ver_productos()

        elif opcion == "5":
            sistema.crear_pedido()

        elif opcion == "6":
            sistema.ver_pedidos()

        elif opcion == "7":
            print("Gracias por usar Dronivery")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()