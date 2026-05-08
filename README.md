# Dronivery

## Sistema básico de gestión de pedidos de comida con entrega simulada por drones

Dronivery es un proyecto desarrollado en Python para la materia de Programación III.

El sistema simula una empresa de comida a domicilio que utiliza drones para realizar entregas.

El programa permite registrar drones, productos de comida, crear pedidos, seleccionar barrios en cobertura, calcular automáticamente la distancia de entrega y asignar un dron disponible según su batería, capacidad de carga y distancia máxima permitida.

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
├── data/
│   └── datos.json
│
├── models/
│   ├── __init__.py
│   ├── Cliente.py
│   ├── Dron.py
│   ├── Pedido.py
│   └── Producto.py
│
├── sistema/
│   ├── __init__.py
│   └── SistemaDronivery.py
│
├── main.py
└── README.md