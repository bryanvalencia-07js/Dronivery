class Producto:
    def __init__(self, codigo, nombre, precio, peso_kg):
        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio
        self._peso_kg = peso_kg

    def get_codigo(self):
        return self._codigo

    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio

    def get_peso_kg(self):
        return self._peso_kg

    def set_precio(self, precio):
        if precio > 0:
            self._precio = precio
        else:
            print("Error: el precio debe ser mayor que 0.")

    def set_peso_kg(self, peso_kg):
        if peso_kg > 0:
            self._peso_kg = peso_kg
        else:
            print("Error: el peso debe ser mayor que 0.")

    def calcular_subtotal(self, cantidad):
        return self._precio * cantidad

    def calcular_peso_total(self, cantidad):
        return self._peso_kg * cantidad

    def mostrar_info(self):
        print("----- INFORMACIÓN DEL PRODUCTO -----")
        print(f"Código: {self._codigo}")
        print(f"Nombre: {self._nombre}")
        print(f"Precio: ${self._precio}")
        print(f"Peso: {self._peso_kg} kg")