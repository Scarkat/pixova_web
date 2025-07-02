const API_BASE_URL = 'http://localhost:8000/api/servicios/';

document.addEventListener('DOMContentLoaded', () => {
    cargarServicios();
});

function cargarServicios() {
    fetch(API_BASE_URL)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            renderServicios(data.results);
        })
        .catch(error => {
            console.error('Error al cargar servicios:', error);
        });
}

function renderServicios(servicios) {
    const tbody = document.querySelector('#servicios-table tbody');
    tbody.innerHTML = '';
    servicios.forEach(servicio => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${servicio.title}</td>
            <td>${servicio.description}</td>
            <td><img src="${servicio.image_url || ''}" alt="Imagen" style="max-width:60px;max-height:40px;"></td>
            <td>
                <button class="action-btn" title="Editar"><span>✏️</span></button>
                <button class="action-btn" title="Eliminar"><span>🗑️</span></button>
            </td>
        `;
        tbody.appendChild(tr);
    });
} 