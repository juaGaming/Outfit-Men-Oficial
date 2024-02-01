// Listar prendas
function Consultar() {
    fetch("http://127.0.0.1:8000/listarPrendas",{
        method: "GET",
        headers: {
            "consultar-Type": "OufitMen/json"
        }
    })
    .then(response => response.json())
    .then(datos => {
        console.log(datos);
        let tabla = document.querySelector('#tabla1-body');
        tabla.innerHTML = "";

        if (datos.length === 0) {
            tabla.innerHTML += `<tr> <td colspan="7"> no hay datos </td> </tr>`;
        } else {
            for (let dat of datos) {
                tabla.innerHTML += `
                <tr>
                <td>${dat.prod_Id}</td>
                <td>${dat.prod_Nombre}</td>
                <td>${dat.prod_Descripcion}</td>
                <td>${dat.prod_Precio}</td>
                <td>${dat.prod_Talla}</td>
                <td>${dat.prod_Color}</td>
                <td>${dat.prod_Imagen}</td>
                <td>
                <div class="btn-container">
                <button class="btnEliminar" onclick="EliminarPrendas(${dat.prod_Id})">Eliminar</button>
                <button class="btnActualizar" onclick="capturarYActualizarProducto(${dat.prod_Id})">Actualizar</button>
                </div>
                </td>
                </tr>`;


                            // Obtén todos los botones de "Actualizar"
                const updateButtons = document.querySelectorAll('.btnActualizar');
                
                // Agrega un evento de clic a cada botón de "Actualizar"
                updateButtons.forEach(button => {
                    button.addEventListener('click', function() {
                        const prod_Id = button.getAttribute('data-prod_Id');
                        abrirModalActualizar(prod_Id);
                    });
                });
            }
        }
    });
}




//Agregar Productos
function agregarProducto() {
    var prod_Nombre = document.getElementById("prod_Nombre").value;
    var prod_Descripcion = document.getElementById("prod_Descripcion").value;
    var prod_Precio = document.getElementById("prod_Precio").value;
    var prod_Talla = document.getElementById("prod_Talla").value;
    var prod_Color = document.getElementById("prod_Color").value;
    var prod_Imagen = document.getElementById("prod_Imagen").value;
  
  
    if (
      
        prod_Nombre === "" ||
        prod_Descripcion === "" ||
        prod_Precio === "" ||
        prod_Talla === "" ||
        prod_Color === "" ||
        prod_Imagen === "" 
    ) {
        Swal.fire({
            icon: "error",
            title: "Error",
            text: "Por favor, complete todos los campos."
        });
        return; // No envíes la solicitud si hay campos vacíos
    }
  
    var datos = {
        prod_Nombre: prod_Nombre,
        prod_Descripcion: prod_Descripcion,
        prod_Precio: prod_Precio,
        prod_Talla: prod_Talla,
        prod_Color: prod_Color,
        prod_Imagen: prod_Imagen
    };
  
    console.log(datos)
  
    var jsonData = JSON.stringify(datos);
  
    fetch("http://127.0.0.1:8000/InsertarPrendas/", {
        method: "POST",
        body: jsonData,
        headers: {
            "Content-Type": "AppOufitMen/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        Consultar();
        //equiposActivos();
        //mostrarCantidadEquipos();
        //equiposInactivos();
        Swal.fire({
            icon: "success",
            title: "Éxito",
            text: "Datos enviados exitosamente."
        });
    })
    .catch(error => {
        console.error(error);
        Swal.fire({
            icon: "error",
            title: "Error",
            text: "Serial ya existente"
        });
    });
  }
  
  document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("FormProductos").addEventListener("submit", function (event) {
        event.preventDefault();
        agregarProducto();
    });
  });
  





//Eliminar prendas
function EliminarPrendas(prod_Id) {
    const url = `http://127.0.0.1:8000/EliminarPrendas/${prod_Id}`;

    Swal.fire({
        title: "¿Estás seguro?",
        text: "Esta Acción Eliminará El Producto",
        icon: "error",
        showCancelButton: true,
        confirmButtonText: "Eliminar",
        cancelButtonText: "Cancelar"
    }).then((result) => {
        if (result.isConfirmed) {
            fetch(url, {
                method: "DELETE",
                headers: {
                    "consultar-Type": "AppOufitMen/json"
                }
            })
            .then(response => response.json())
            .then(data => {
                Consultar();
                Swal.fire("Éxito", "Dispositivo eliminado exitosamente.", "success");
            })
            .catch(error => {
                console.error("Error al eliminar el Dispositivo:", error);
                Swal.fire("Error", "Error al eliminar el equipo.", "error");
            });
        }
    });
}




document.addEventListener("DOMContentLoaded", () => {
    const buscarBtn = document.getElementById("BuscarArticulo");
    buscarBtn.addEventListener("click", () => {
        const ProductoidInput = document.getElementById("prod_Id");
        const Productoid = ProductoidInput.value;

        if (Productoid) {
            const url = `http://127.0.0.1:8000/BuscarProducto/${Productoid}/`;

            fetch(url, {
                method: "GET",
                headers: {
                    "Content-Type": "application/json"
                }
            })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error("Error al buscar el Producto por el Id");
                }
            })
            .then(prenda => {
                if (prenda.hasOwnProperty('prod_Id')) {
                    const tablaBody = document.getElementById("tabla1-body");
                    tablaBody.innerHTML = "";

                    const newRow = document.createElement("tr");
                    newRow.innerHTML = `
                        <td>${prenda.prod_Id}</td>
                        <td>${prenda.prod_Nombre}</td>
                        <td>${prenda.prod_Descripcion}</td>
                        <td>${prenda.prod_Precio}</td>
                        <td>${prenda.prod_Talla}</td>
                        <td>${prenda.prod_Color}</td>
                        <td>${prenda.prod_Imagen}</td>
                        <td>
                            <div class="btn-container">
                                <button class="btnEliminar" onclick="EliminarPrendas(${prenda.prod_Id})">Eliminar</button>
                                <button class="btnActualizar" data-prod_Id="${prenda.prod_Id}">Actualizar</button>
                            </div>
                        </td>
                    `;

                    tablaBody.appendChild(newRow);
                    
                    // Agregar evento de clic al botón de "Actualizar"
                    const updateButton = newRow.querySelector('.btnActualizar');
                    updateButton.addEventListener('click', function() {
                        const prod_Id = this.getAttribute('data-prod_Id');
                        abrirModalActualizar(prod_Id);
                    });

                } else {
                    Swal.fire({
                        title: "Dispositivo No Encontrado",
                        icon: "error", 
                        confirmButtonText: "Aceptar"
                    });
                    Consultar();
                }
            })
            .catch(error => {
                console.error("Error al buscar el equipo por Serial:", error);
                alert("Error al buscar el equipo por Serial");
            });
        } else {
            console.error("Debe ingresar un serial de un equipo válido");
        }
    });
});















function capturarYActualizarProducto(prod_Id) {
    fetch(`http://127.0.0.1:8000/BuscarProducto/${prod_Id}`, {
        method: "GET",
        headers: {
            "consultar-Type": "AppOufitMen/json"
        }
    })

    .then(response => response.json())
    .then(data => {
        // Populate the form fields with the retrieved data
        document.getElementById('prod_Id_Act').value = data.prod_Id;
        document.getElementById('prod_Nombre_Act').value = data.prod_Nombre;
        document.getElementById('prod_Descripcion_Act').value = data.prod_Descripcion;
        document.getElementById('prod_Precio_Act').value = data.prod_Precio;
        document.getElementById('prod_Talla_Act').value = data.prod_Talla;
        document.getElementById('prod_Color_Act').value = data.prod_Color;
        document.getElementById('prod_Imagen_Act').value = data.prod_Imagen;

        // Show the update form
        document.getElementById('ActualizarProducto').style.display = 'block';
        
        // Update the form submission event listener
        document.getElementById("ActualizarProducto").addEventListener("submit", function (event) {
            event.preventDefault();
            ActualizarProducto(prod_Id);
        });
    });
}

//Actualizar prendas
function ActualizarProducto (prod_Id) {
    var datos = {
        prod_Id: document.getElementById("prod_Id_Act").value,
        prod_Nombre: document.getElementById("prod_Nombre_Act").value,
        prod_Descripcion: document.getElementById("prod_Descripcion_Act").value,
        prod_Precio: document.getElementById("prod_Precio_Act").value,
        prod_Talla: document.getElementById("prod_Talla_Act").value,
        prod_Color: document.getElementById("prod_Color_Act").value,
        prod_Imagen: document.getElementById("prod_Imagen_Act").value
    };

    var jsonData = JSON.stringify(datos);

    fetch("http://127.0.0.1:8000/ActualizarProducto/" + prod_Id, {
        method: "POST", 
        body: jsonData,
        headers: {
            "Content-Type": "application/json" 
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        Consultar();
        Swal.fire({
            icon: "success",
            title: "Éxito",
            text: "Datos enviados exitosamente.",
        });

    })
    .catch(error => {
        console.error(error);
        Swal.fire({
            icon: "error",
            title: "Error",
            text: "Error al enviar los datos."
        });
    });
}



document.addEventListener("DOMContentLoaded", function () {
    // Replace 'equipoId' with the actual ID of the equipment you want to capture and update
    capturarYActualizarProducto(prod_Id);
}); 











// funcionamiento para abrir un modal

document.addEventListener('DOMContentLoaded', function() {
    // Obtén una referencia al botón de abrir modal y al modal de actualización
    const openUpdateModalBtn = document.querySelector('.btnInsertar');
    const updateModal = document.getElementById('myModal2');
  
    // Agrega un evento de escucha al botón para abrir el modal de actualización
    openUpdateModalBtn.addEventListener('click', function() {
      updateModal.style.display = 'block'; // Muestra el modal de actualización
    });
  
    // Busca el botón de cierre en el modal de actualización y agrega un evento de escucha para cerrar el modal
    const closeUpdateModalBtn = updateModal.querySelector('.close2');
    closeUpdateModalBtn.addEventListener('click', function() {
      updateModal.style.display = 'none'; // Cierra el modal de actualización
    });
  
    // Agrega eventos de escucha para cambiar el color del cursor al pasar cerca de la "x"
    closeUpdateModalBtn.addEventListener('mouseenter', function() {
      closeUpdateModalBtn.style.color = 'red'; // Cambia el color al pasar cerca del cursor
    });
  
    closeUpdateModalBtn.addEventListener('mouseleave', function() {
      closeUpdateModalBtn.style.color = '#aaa'; // Restaura el color original
    });
  });

  
//funcion para que el boton pueda abrir el modal desde JS
function abrirModalActualizar() {
    const updateModal = document.getElementById('myModal');
    updateModal.style.display = 'block'; // Muestra el modal de actualización
    
    const closeUpdateModalBtn = updateModal.querySelector('.close');
    closeUpdateModalBtn.addEventListener('click', function() {
        updateModal.style.display = 'none'; // Cierra el modal de actualización
    });

    closeUpdateModalBtn.addEventListener('mouseenter', function() {
        closeUpdateModalBtn.style.color = 'red'; // Cambia el color al pasar cerca del cursor
    });

    closeUpdateModalBtn.addEventListener('mouseleave', function() {
        closeUpdateModalBtn.style.color = '#aaa'; // Restaura el color original
    });

    
    // Aquí puedes realizar acciones adicionales según tus necesidades, como cargar los datos del equipo en el modal.
}