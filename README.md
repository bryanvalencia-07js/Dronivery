# Dronivery

## Plataforma web de domicilios con asignación automática de drones

Dronivery Web es una aplicación desarrollada con Python, Flask, HTML, CSS y JavaScript que simula una plataforma de domicilios tipo Rappi, donde los conductores registran drones y los usuarios realizan pedidos que son asignados automáticamente a un dron disponible.

## Conceptos aplicados de Programación III

Clases
Objetos
Métodos
Atributos protegidos
Encapsulamiento
Getters y setters
Listas de objetos
Modularidad
Manejo de archivos JSON
Base de datos pequeña en json

## Cómo ejecutar el proyecto localmente

Este proyecto utiliza Python con Flask para el backend, y HTML, CSS y JavaScript para el frontend.

GitHub Pages no ejecuta aplicaciones con backend en Python, por eso el proyecto debe ejecutarse de manera local usando Flask.

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

Luego entrar a la carpeta del proyecto:

```bash
cd Dronivery
```

### 2. Crear un entorno virtual

En Linux o macOS:

```bash
python3 -m venv .venv
```

En Windows:

```bash
python -m venv .venv
```

### 3. Activar el entorno virtual

En Linux o macOS:

```bash
source .venv/bin/activate
```

En Windows:

```bash
.venv\Scripts\activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar el servidor Flask

En Linux o macOS:

```bash
python3 app.py
```

En Windows:

```bash
python app.py
```

### 6. Abrir la aplicación en el navegador

Después de ejecutar el servidor, abrir esta dirección:

```text
http://127.0.0.1:5000
```

Desde ahí se puede acceder a la pantalla principal de Dronivery, donde existen dos roles:

* Usuario: permite crear pedidos.
* Conductor: permite registrar drones disponibles.

### 7. Detener el servidor

Para detener Flask, presionar en la terminal:

```bash
Ctrl + C
```

### 8. Salir del entorno virtual

```bash
deactivate
```

## Nota

El sistema guarda la información en el archivo:

```text
data/datos.json
```

Allí se almacenan los drones registrados, pedidos realizados y demás datos necesarios para simular el funcionamiento de la plataforma.

## Estructura del proyecto

Dronivery/
│
├── backend/
│   ├── app.py
│   ├── data/
│   │   └── datos.json
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── Dron.py
│   │   ├── Producto.py
│   │   ├── Pedido.py
│   │   ├── Usuario.py
│   │   └── Conductor.py
│   │
│   └── services/
│       ├── __init__.py
│       └── SistemaDronivery.py
│
├── frontend/
│   ├── index.html
│   ├── conductor.html
│   ├── usuario.html
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── app.js
│
├── README.md
└── .gitignore