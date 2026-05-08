import json


from models.Dron import Dron
from models.Producto import Producto
from models.Cliente import Cliente
from models.Pedido import Pedido


class SistemaDronivery:
    def __init__(self):
        self._drones = []
        self._productos = []
        self._pedidos = []
        self._contador_pedidos = 1
        self._ruta_datos = "data/datos.json"
        self.cargar_datos()
    
    def guardar_datos(self):
        datos = {
            "drones": [],
            "productos": [],
            "pedidos": [],
            "contador_pedidos": self._contador_pedidos
        }

        for dron in self._drones:
            datos["drones"].append({
                "codigo": dron.get_codigo(),
                "modelo": dron.get_modelo(),
                "bateria": dron.get_bateria(),
                "capacidad_kg": dron.get_capacidad_kg(),
                "distancia_maxima_km": dron.get_distancia_maxima_km(),
                "estado": dron.get_estado()
            })

        for producto in self._productos:
            datos["productos"].append({
                "codigo": producto.get_codigo(),
                "nombre": producto.get_nombre(),
                "precio": producto.get_precio(),
                "peso_kg": producto.get_peso_kg()
            })

        for pedido in self._pedidos:
            cliente = pedido.get_cliente()
            producto = pedido.get_producto()
            dron = pedido.get_dron_asignado()

            datos["pedidos"].append({
                "numero": pedido.get_numero(),
                "cliente": {
                    "nombre": cliente.get_nombre(),
                    "telefono": cliente.get_telefono(),
                    "direccion": cliente.get_direccion(),
                    "barrio": cliente.get_barrio()
                },
                "producto": {
                    "codigo": producto.get_codigo(),
                    "nombre": producto.get_nombre(),
                    "precio": producto.get_precio(),
                    "peso_kg": producto.get_peso_kg()
                },
                "cantidad": pedido.get_cantidad(),
                "distancia_km": pedido.get_distancia_km(),
                "total": pedido.get_total(),
                "peso_total": pedido.get_peso_total(),
                "estado": pedido.get_estado(),
                "dron_asignado": dron.get_codigo() if dron is not None else None
            })

        with open(self._ruta_datos, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

        print("Datos guardados correctamente en JSON.")

    def cargar_datos(self):
        try:
            with open(self._ruta_datos, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

            for dato_dron in datos["drones"]:
                dron = Dron(
                    dato_dron["codigo"],
                    dato_dron["modelo"],
                    dato_dron["bateria"],
                    dato_dron["capacidad_kg"],
                    dato_dron["distancia_maxima_km"]
                )

                dron.set_estado(dato_dron["estado"])
                self._drones.append(dron)

            for dato_producto in datos["productos"]:
                producto = Producto(
                    dato_producto["codigo"],
                    dato_producto["nombre"],
                    dato_producto["precio"],
                    dato_producto["peso_kg"]
                )

                self._productos.append(producto)

            for dato_pedido in datos["pedidos"]:
                dato_cliente = dato_pedido["cliente"]
                dato_producto = dato_pedido["producto"]

                cliente = Cliente(
                    dato_cliente["nombre"],
                    dato_cliente["telefono"],
                    dato_cliente["direccion"],
                    dato_cliente["barrio"]
                )

                producto = Producto(
                    dato_producto["codigo"],
                    dato_producto["nombre"],
                    dato_producto["precio"],
                    dato_producto["peso_kg"]
                )

                pedido = Pedido(
                    dato_pedido["numero"],
                    cliente,
                    producto,
                    dato_pedido["cantidad"],
                    dato_pedido["distancia_km"]
                )

                pedido.set_estado(dato_pedido["estado"])

                codigo_dron = dato_pedido["dron_asignado"]

                if codigo_dron is not None:
                    for dron in self._drones:
                        if dron.get_codigo() == codigo_dron:
                            pedido._dron_asignado = dron

                self._pedidos.append(pedido)

            self._contador_pedidos = datos["contador_pedidos"]

            print("Datos cargados correctamente desde JSON.")

        except FileNotFoundError:
            print("No se encontró el archivo datos.json. Se iniciará el sistema vacío.")

        except json.JSONDecodeError:
            print("El archivo datos.json está vacío o tiene un formato incorrecto.")

    def registrar_dron(self):
        print("\n***** REGISTRAR DRON *****")

        codigo = input("Ingrese el código del dron: ")
        modelo = input("Ingrese el modelo del dron: ")
        bateria = int(input("Ingrese la batería del dron (%): "))
        capacidad_kg = float(input("Ingrese la capacidad máxima en kg: "))
        distancia_maxima_km = float(input("Ingrese la distancia máxima en km: "))

        nuevo_dron = Dron(codigo, modelo, bateria, capacidad_kg, distancia_maxima_km)
        self._drones.append(nuevo_dron)
        self.guardar_datos()

        print("\nDron registrado correctamente.")

    def ver_drones(self):
        print("\n**** LISTA DE DRONES ****")

        if len(self._drones) == 0:
            print("No hay drones registrados.")
        else:
            for dron in self._drones:
                dron.mostrar_info()
                print("--------------------------")

    def registrar_producto(self):
        print("\n***** REGISTRAR PRODUCTO *****")

        codigo = input("Ingrese el código del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        peso_kg = float(input("Ingrese el peso del producto en kg: "))

        nuevo_producto = Producto(codigo, nombre, precio, peso_kg)
        self._productos.append(nuevo_producto)
        self.guardar_datos()

        print("\nProducto registrado correctamente.")

    def ver_productos(self):
        print("\n**** MENÚ DE PRODUCTOS ****")

        if len(self._productos) == 0:
            print("No hay productos registrados.")
        else:
            for producto in self._productos:
                producto.mostrar_info()
                print("--------------------------")

    def buscar_producto_por_codigo(self, codigo):
        for producto in self._productos:
            if producto.get_codigo() == codigo:
                return producto
        return None

    def buscar_dron_disponible(self, pedido):
        for dron in self._drones:
            if dron.puede_entregar(pedido.get_peso_total(), pedido.get_distancia_km()):
                return dron
        return None
    
    def obtener_barrios_cobertura(self):
        return {
            "1": ["Centro", 1.5],
            "2": ["La Pradera", 2.3],
            "3": ["Milán", 3.0],
            "4": ["Los Naranjos", 3.5],
            "5": ["Santa Mónica", 4.0],
            "6": ["Jardín", 4.5],
            "7": ["El Poblado", 5.0],
            "8": ["Villa del Campo", 5.5],
            "9": ["Bosques de la Acuarela", 6.0]
        }

    def seleccionar_barrio(self):
        barrios = self.obtener_barrios_cobertura()

        print("\n===== BARRIOS EN COBERTURA =====")
        for opcion, datos in barrios.items():
            nombre_barrio = datos[0]
            distancia = datos[1]
            print(f"{opcion}. {nombre_barrio} - {distancia} km")

        opcion_barrio = input("Seleccione el número del barrio: ")

        if opcion_barrio in barrios:
            barrio = barrios[opcion_barrio][0]
            distancia_km = barrios[opcion_barrio][1]
            return barrio, distancia_km
        else:
            print("Barrio no válido o fuera de cobertura.")
            return None, None

    def crear_pedido(self):
        print("\n===== CREAR PEDIDO =====")

        if len(self._productos) == 0:
            print("No hay productos registrados. Primero registre un producto.")
            return

        if len(self._drones) == 0:
            print("No hay drones registrados. Primero registre un dron.")
            return

        nombre = input("Ingrese el nombre del cliente: ")
        telefono = input("Ingrese el teléfono del cliente: ")
        direccion = input("Ingrese la dirección del cliente: ")

        barrio, distancia_km = self.seleccionar_barrio()

        if barrio is None:
            print("No se pudo crear el pedido porque el barrio no está en cobertura.")
            return

        cliente = Cliente(nombre, telefono, direccion, barrio)

        print("\n===== PRODUCTOS DISPONIBLES =====")
        for producto in self._productos:
            producto.mostrar_info()
            print("--------------------------")

        codigo_producto = input("Ingrese el código del producto que desea pedir: ")
        producto_encontrado = self.buscar_producto_por_codigo(codigo_producto)

        if producto_encontrado is None:
            print("Producto no encontrado.")
            return

        cantidad = int(input("Ingrese la cantidad: "))

        nuevo_pedido = Pedido(
            self._contador_pedidos,
            cliente,
            producto_encontrado,
            cantidad,
            distancia_km
        )

        dron_disponible = self.buscar_dron_disponible(nuevo_pedido)

        if dron_disponible is not None:
            nuevo_pedido.asignar_dron(dron_disponible)
            print("\nPedido creado correctamente y dron asignado.")
        else:
            print("\nPedido creado, pero no hay dron disponible para esta entrega.")

        self._pedidos.append(nuevo_pedido)
        self._contador_pedidos += 1
        self.guardar_datos()

        print("\n===== RESUMEN DEL PEDIDO =====")
        nuevo_pedido.mostrar_resumen()