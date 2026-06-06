import json
import os
import re

from flask import Flask, send_from_directory, jsonify, request

app = Flask(__name__)
app.json.sort_keys = False

RUTA_DATOS = "data/datos.json"

RUTA_BARRIOS = "data/barrios.js"

MUNICIPIOS_PERMITIDOS = {
    66001: "PEREIRA",
    66170: "DOSQUEBRADAS",
    66682: "SANTA ROSA DE CABAL"
}

def cargar_datos():
    if not os.path.exists(RUTA_DATOS):
        return {
            "drones": [],
            "productos": [],
            "pedidos": [],
            "contador_pedidos": 1
        }

    with open(RUTA_DATOS, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_datos(datos):
    with open(RUTA_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def limpiar_nombre_barrio(nombre):
    reemplazos = {
        "?": "í",
        "`": "",
        "#": "Ñ"
    }

    for viejo, nuevo in reemplazos.items():
        nombre = nombre.replace(viejo, nuevo)

    return nombre.strip()


def calcular_distancia_estimada(posicion, municipio):
    if municipio == "PEREIRA":
        distancia_base = 1.5
    elif municipio == "DOSQUEBRADAS":
        distancia_base = 2.0
    else:
        distancia_base = 4.0

    distancia = distancia_base + (posicion % 10) * 0.4
    return round(distancia, 1)


def cargar_ubicaciones_desde_js():
    with open(RUTA_BARRIOS, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    patron_barrios = r'\{\s*id:\s*(\d+),\s*nombre:\s*"([^"]+)",\s*idMunicipio:\s*(\d+)\s*\}'

    ubicaciones = {
        "PEREIRA": [],
        "DOSQUEBRADAS": [],
        "SANTA ROSA DE CABAL": []
    }

    contador_por_municipio = {
        "PEREIRA": 0,
        "DOSQUEBRADAS": 0,
        "SANTA ROSA DE CABAL": 0
    }

    coincidencias = re.findall(patron_barrios, contenido)

    for id_barrio, nombre_barrio, id_municipio in coincidencias:
        id_municipio = int(id_municipio)

        if id_municipio in MUNICIPIOS_PERMITIDOS:
            nombre_municipio = MUNICIPIOS_PERMITIDOS[id_municipio]
            contador_por_municipio[nombre_municipio] += 1

            posicion = contador_por_municipio[nombre_municipio]

            ubicaciones[nombre_municipio].append({
                "id": int(id_barrio),
                "nombre": limpiar_nombre_barrio(nombre_barrio),
                "distancia_km": calcular_distancia_estimada(posicion, nombre_municipio)
            })

    return ubicaciones

@app.route("/")
def inicio():
    return send_from_directory("frontend", "index.html")


@app.route("/conductor")
def conductor():
    return send_from_directory("frontend", "conductor.html")


@app.route("/usuario")
def usuario():
    return send_from_directory("frontend", "usuario.html")


@app.route("/frontend/<path:archivo>")
def archivos_frontend(archivo):
    return send_from_directory("frontend", archivo)


@app.route("/api/estado")
def estado_api():
    return jsonify({
        "mensaje": "Backend de Dronivery funcionando correctamente",
        "estado": "ok"
    })


@app.route("/api/drones", methods=["GET"])
def obtener_drones():
    datos = cargar_datos()
    return jsonify(datos["drones"])


@app.route("/api/registrar-dron", methods=["POST"])
def registrar_dron():
    datos_recibidos = request.get_json()

    nombre_conductor = datos_recibidos.get("nombre_conductor")
    telefono_conductor = datos_recibidos.get("telefono_conductor")
    ciudad_conductor = datos_recibidos.get("ciudad_conductor")
    codigo = datos_recibidos.get("codigo")
    modelo = datos_recibidos.get("modelo")
    bateria = int(datos_recibidos.get("bateria"))
    capacidad_kg = float(datos_recibidos.get("capacidad_kg"))
    distancia_maxima_km = float(datos_recibidos.get("distancia_maxima_km"))

    datos = cargar_datos()

    for dron in datos["drones"]:
        if dron["codigo"] == codigo:
            return jsonify({
                "estado": "error",
                "mensaje": "Ya existe un dron registrado con ese código."
            }), 400

    nuevo_dron = {
        "conductor": {
            "nombre": nombre_conductor,
            "telefono": telefono_conductor,
            "ciudad": ciudad_conductor
        },
        "codigo": codigo,
        "modelo": modelo,
        "bateria": bateria,
        "capacidad_kg": capacidad_kg,
        "distancia_maxima_km": distancia_maxima_km,
        "estado": "Disponible"
    }

    datos["drones"].append(nuevo_dron)
    guardar_datos(datos)

    return jsonify({
        "estado": "ok",
        "mensaje": "Dron registrado correctamente.",
        "dron": nuevo_dron
    })

@app.route("/api/ubicaciones", methods=["GET"])
def obtener_ubicaciones():
    ubicaciones = cargar_ubicaciones_desde_js()

    resumen = {}

    for municipio, barrios in ubicaciones.items():
        resumen[municipio] = len(barrios)

    return jsonify({
        "estado": "ok",
        "municipios": list(ubicaciones.keys()),
        "barrios": ubicaciones,
        "resumen": resumen
    })

@app.route("/api/crear-pedido", methods=["POST"])
def crear_pedido():
    datos_recibidos = request.get_json()

    nombre_usuario = datos_recibidos.get("nombre_usuario")
    telefono_usuario = datos_recibidos.get("telefono_usuario")
    direccion_usuario = datos_recibidos.get("direccion_usuario")
    barrio_usuario = datos_recibidos.get("barrio_usuario")
    ciudad_usuario = datos_recibidos.get("ciudad_usuario")

    nombre_producto = datos_recibidos.get("nombre_producto")
    cantidad = int(datos_recibidos.get("cantidad"))

    productos_disponibles = {
        "Hamburguesa clásica": {
            "precio": 18000,
            "peso_kg": 0.8
        },
        "Pizza personal": {
            "precio": 22000,
            "peso_kg": 1.0
        },
        "Perro caliente": {
            "precio": 14000,
            "peso_kg": 0.6
        },
        "Combo alitas": {
            "precio": 26000,
            "peso_kg": 1.2
        },
        "Salchipapa especial": {
            "precio": 20000,
            "peso_kg": 1.1
        },
        "Arroz chino personal": {
            "precio": 25000,
            "peso_kg": 1.3
        },
        "Combo hamburguesa doble": {
            "precio": 32000,
            "peso_kg": 1.5
        },
        "Burrito mixto": {
            "precio": 24000,
            "peso_kg": 1.0
        },
        "Sushi roll personal": {
            "precio": 28000,
            "peso_kg": 0.9
        }
    }

    producto_encontrado = productos_disponibles.get(nombre_producto)

    if producto_encontrado is None:
        return jsonify({
            "estado": "error",
            "mensaje": "El producto seleccionado no existe en el catálogo."
        }), 400

    precio_producto = producto_encontrado["precio"]
    peso_producto = producto_encontrado["peso_kg"]

    peso_total = peso_producto * cantidad
    total = precio_producto * cantidad

    datos = cargar_datos()

    dron_asignado = None

    for dron in datos["drones"]:
        conductor = dron.get("conductor", {})
        ciudad_conductor = conductor.get("ciudad")

        if(
            dron.get("estado") == "Disponible"
            and ciudad_conductor == ciudad_usuario
            and dron.get("bateria", 0) >= 30
            and dron.get("capacidad_kg", 0) >= peso_total
        ):
            dron_asignado = dron
            dron["estado"] = "Ocupado"
            break

        numero_pedido = datos["contador_pedidos"]

        nuevo_pedido = {
            "numero": numero_pedido,
            "usuario": {
                "nombre": nombre_usuario,
                "telefono": telefono_usuario,
                "direccion": direccion_usuario,
                "barrio": barrio_usuario,
                "ciudad": ciudad_usuario
            },
            "producto": {
                "nombre": nombre_producto,
                "peso_kg": peso_producto,
                "precio": precio_producto,
            },
            "cantidad": cantidad,
            "peso_total": peso_total,
            total: total,
            "estado": "Dron asignado" if dron_asignado is not None else "Pendiente por dron",
            "dron_asignado": dron_asignado["codigo"] if dron_asignado is not None else None
        }

        datos["pedidos"].append(nuevo_pedido)
        datos["contador_pedidos"] += 1

        guardar_datos(datos)

        if dron_asignado is not None:
            return jsonify({
                "estado": "ok",
                "mensaje": "Pedido creado correctamente. Se asignó un dron disponible.",
                "pedido": nuevo_pedido,
                "dron": dron_asignado
            })
        
        return jsonify({
            "estado": "sin_dron",
            "mensaje": "Pedido creado, pero no hay drones disponibles en esta ciudad.",
            "pedido": nuevo_pedido
        })


if __name__ == "__main__":
    app.run(debug=True)