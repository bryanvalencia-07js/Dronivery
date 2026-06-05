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