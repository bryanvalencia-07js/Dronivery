document.addEventListener("DOMContentLoaded", () => {
    const formConductor = document.getElementById("formConductor");
    const formUsuario = document.getElementById("formUsuario");
    const ciudadUsuario = document.getElementById("ciudadUsuario");
    const barrioUsuario = document.getElementById("barrioUsuario");


    // ==========================
    // REGISTRO DE CONDUCTOR
    // ==========================
    if (formConductor) {
        formConductor.addEventListener("submit", async (event) => {
            event.preventDefault();

            const datosDron = {
                nombre_conductor: document.getElementById("nombreConductor").value,
                telefono_conductor: document.getElementById("telefonoConductor").value,
                ciudad_conductor: document.getElementById("ciudadConductor").value,
                codigo: document.getElementById("codigoDron").value,
                modelo: document.getElementById("modeloDron").value,
                bateria: document.getElementById("bateriaDron").value,
                capacidad_kg: document.getElementById("capacidadDron").value,
                distancia_maxima_km: document.getElementById("distanciaDron").value
            };

            console.log(datosDron);

            console.log(datosDron);

            const mensaje = document.getElementById("mensajeConductor");

            try {
                const respuesta = await fetch("/api/registrar-dron", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(datosDron)
                });

                const resultado = await respuesta.json();

                if (respuesta.ok) {
                    mensaje.textContent = resultado.mensaje;
                    mensaje.className = "mensaje exito";
                    formConductor.reset();
                } else {
                    mensaje.textContent = resultado.mensaje;
                    mensaje.className = "mensaje error";
                }

            } catch (error) {
                mensaje.textContent = "Error al conectar con el servidor.";
                mensaje.className = "mensaje error";
            }
        });
    }

    // ==========================
    // CARGAR BARRIOS POR CIUDAD
    // ==========================
    if (ciudadUsuario && barrioUsuario) {
        let ubicaciones = {};

        async function cargarUbicaciones() {
            try {
                const respuesta = await fetch("/api/ubicaciones");
                const resultado = await respuesta.json();

                if (resultado.estado === "ok") {
                    ubicaciones = resultado.barrios;
                }

            } catch (error) {
                console.log("Error al cargar ubicaciones:", error);
            }
        }

        function cargarBarriosPorCiudad(ciudad) {
            barrioUsuario.innerHTML = "";

            if (!ciudad || !ubicaciones[ciudad]) {
                barrioUsuario.innerHTML = `
                    <option value="">Primero seleccione una ciudad</option>
                `;
                return;
            }

            barrioUsuario.innerHTML = `
                <option value="">Seleccione un barrio</option>
            `;

            ubicaciones[ciudad].forEach((barrio) => {
                const opcion = document.createElement("option");
                opcion.value = barrio.nombre;
                opcion.textContent = barrio.nombre;
                opcion.dataset.distancia = barrio.distancia_km;
                opcion.dataset.id = barrio.id;

                barrioUsuario.appendChild(opcion);
            });
        }

        ciudadUsuario.addEventListener("change", () => {
            const ciudadSeleccionada = ciudadUsuario.value;
            cargarBarriosPorCiudad(ciudadSeleccionada);
        });

        cargarUbicaciones();
    }

    // ==========================
    // CREAR PEDIDO DE USUARIO
    // ==========================
    if (formUsuario) {
        formUsuario.addEventListener("submit", async (event) => {
            event.preventDefault();

            const productoSelect = document.getElementById("productoUsuario");
            const productoSeleccionado = productoSelect.options[productoSelect.selectedIndex];

            const datosPedido = {
                nombre_usuario: document.getElementById("nombreUsuario").value,
                telefono_usuario: document.getElementById("telefonoUsuario").value,
                direccion_usuario: document.getElementById("direccionUsuario").value,
                ciudad_usuario: document.getElementById("ciudadUsuario").value,
                barrio_usuario: document.getElementById("barrioUsuario").value,
                nombre_producto: productoSeleccionado.value,
                precio_producto: productoSeleccionado.dataset.precio,
                peso_producto: productoSeleccionado.dataset.peso,
                cantidad: document.getElementById("cantidadUsuario").value
            };

            const mensaje = document.getElementById("mensajeUsuario");

            try {
                const respuesta = await fetch("/api/crear-pedido", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(datosPedido)
                });

                const resultado = await respuesta.json();

                if (resultado.estado === "ok") {
                    mensaje.textContent = `${resultado.mensaje} Dron asignado: ${resultado.dron.codigo}`;
                    mensaje.className = "mensaje exito";
                    formUsuario.reset();
                } else if (resultado.estado === "sin_dron") {
                    mensaje.textContent = resultado.mensaje;
                    mensaje.className = "mensaje error";
                } else {
                    mensaje.textContent = "No se pudo crear el pedido.";
                    mensaje.className = "mensaje error";
                }

            } catch (error) {
                mensaje.textContent = "Error al conectar con el servidor.";
                mensaje.className = "mensaje error";
            }
        });
    }
});