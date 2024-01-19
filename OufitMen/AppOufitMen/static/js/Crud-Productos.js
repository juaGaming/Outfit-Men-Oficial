//visualizar todos los productos

function Consultar() {
  fetch("http://127.0.0.1:8000/ListarProductos",{
      method: "GET",
      headers: {
          "consultar-Type": "AppOufitMen/json"
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
              <td>${dat.prod_Imagen ? `<img src="${dat.prod_Imagen}" alt="Imagen del producto">` : 'Sin imagen'}</td>
              <td>
                  <div class="btn-container">
                      <button class="btnEliminar" onclick="eliminarProducto(${dat.prod_Id})">Eliminar</button>
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
      //Consultar();
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