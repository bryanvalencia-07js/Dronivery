class Pedido:
    def __init__(self, numero, cliente, producto, cantidad, distancia_km):
        self._numero = numero
        self._cliente = cliente
        self._producto = producto
        self._cantidad = cantidad
        self._distancia_km = distancia_km
        self._total = producto.calcular_subtotal(cantidad)
        self._peso_total = producto.calcular_peso_total(cantidad)
        self._estado = "Creado"
        self._dron_asignado = None

    def get_numero(self):
        return self._numero

    def get_cliente(self):
        return self._cliente

    def get_producto(self):
        return self._producto

    def get_cantidad(self):
        return self._cantidad

    def get_distancia_km(self):
        return self._distancia_km

    def get_total(self):
        return self._total

    def get_peso_total(self):
        return self._peso_total

    def get_estado(self):
        return self._estado

    def get_dron_asignado(self):
        return self._dron_asignado

    def set_estado(self, estado):
        estados_validos = [
            "Creado",
            "Preparando",
            "Dron asignado",
            "En camino",
            "Entregado",
            "Cancelado"
        ]

        if estado in estados_validos:
            self._estado = estado
        else:
            print("Error: estado del pedido no válido.")

    def asignar_dron(self, dron):
        self._dron_asignado = dron
        self._estado = "Dron asignado"
        dron.asignar()

    def cambiar_estado(self, nuevo_estado):
        self.set_estado(nuevo_estado)

        if nuevo_estado == "Entregado" and self._dron_asignado is not None:
            self._dron_asignado.liberar()

    def mostrar_resumen(self):
        print("----- RESUMEN DEL PEDIDO -----")
        print(f"Número de pedido: {self._numero}")
        print(f"Cliente: {self._cliente.get_nombre()}")
        print(f"Producto: {self._producto.get_nombre()}")
        print(f"Cantidad: {self._cantidad}")
        print(f"Peso total: {self._peso_total} kg")
        print(f"Distancia de entrega: {self._distancia_km} km")
        print(f"Total a pagar: ${self._total}")
        print(f"Estado: {self._estado}")

        if self._dron_asignado is not None:
            print(f"Dron asignado: {self._dron_asignado.get_codigo()}")
        else:
            print("Dron asignado: Ninguno")