class Dron:
    def __init__(self, codigo, modelo, bateria, capacidad_kg, distancia_maxima_km):
        self._codigo = codigo
        self._modelo = modelo
        self._bateria = bateria
        self._capacidad_kg = capacidad_kg
        self._distancia_maxima_km = distancia_maxima_km
        self._estado = "Disponible"

    def get_codigo(self):
        return self._codigo

    def get_modelo(self):
        return self._modelo

    def get_bateria(self):
        return self._bateria

    def get_capacidad_kg(self):
        return self._capacidad_kg

    def get_distancia_maxima_km(self):
        return self._distancia_maxima_km

    def get_estado(self):
        return self._estado

    def set_bateria(self, bateria):
        if 0 <= bateria <= 100:
            self._bateria = bateria
        else:
            print("Error: la batería debe estar entre 0 y 100.")

    def set_estado(self, estado):
        estados_validos = ["Disponible", "Ocupado", "Mantenimiento"]

        if estado in estados_validos:
            self._estado = estado
        else:
            print("Error: estado no válido.")

    def puede_entregar(self, peso_pedido, distancia_km):
        return (
            self._estado == "Disponible"
            and self._bateria >= 30
            and peso_pedido <= self._capacidad_kg
            and distancia_km <= self._distancia_maxima_km
        )

    def asignar(self):
        self._estado = "Ocupado"

    def liberar(self):
        self._estado = "Disponible"

    def mostrar_info(self):
        print("----- INFORMACIÓN DEL DRON -----")
        print(f"Código: {self._codigo}")
        print(f"Modelo: {self._modelo}")
        print(f"Batería: {self._bateria}%")
        print(f"Capacidad máxima: {self._capacidad_kg} kg")
        print(f"Distancia máxima: {self._distancia_maxima_km} km")
        print(f"Estado: {self._estado}")