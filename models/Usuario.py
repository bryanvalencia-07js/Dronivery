class Cliente:
    def __init__(self, nombre, telefono, direccion, barrio):
        self._nombre = nombre
        self._telefono = telefono
        self._direccion = direccion
        self._barrio = barrio

    def get_nombre(self):
        return self._nombre

    def get_telefono(self):
        return self._telefono

    def get_direccion(self):
        return self._direccion

    def get_barrio(self):
        return self._barrio

    def set_nombre(self, nombre):
        if nombre.strip() != "":
            self._nombre = nombre
        else:
            print("Error: el nombre no puede estar vacío.")

    def set_telefono(self, telefono):
        if telefono.strip() != "":
            self._telefono = telefono
        else:
            print("Error: el teléfono no puede estar vacío.")

    def set_direccion(self, direccion):
        if direccion.strip() != "":
            self._direccion = direccion
        else:
            print("Error: la dirección no puede estar vacía.")

    def set_barrio(self, barrio):
        if barrio.strip() != "":
            self._barrio = barrio
        else:
            print("Error: el barrio no puede estar vacío.")

    def mostrar_info(self):
        print("----- INFORMACIÓN DEL CLIENTE -----")
        print(f"Nombre: {self._nombre}")
        print(f"Teléfono: {self._telefono}")
        print(f"Dirección: {self._direccion}")
        print(f"Barrio: {self._barrio}")