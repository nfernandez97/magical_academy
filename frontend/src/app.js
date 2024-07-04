import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [solicitudes, setSolicitudes] = useState([]);
  const [asignaciones, setAsignaciones] = useState([]);
  const [form, setForm] = useState({
    nombre: '',
    apellido: '',
    identificacion: '',
    edad: '',
    afinidad_magica: 'Oscuridad',
  });
  const [selectedSolicitud, setSelectedSolicitud] = useState(null);
  const [newStatus, setNewStatus] = useState('aprobado');

  useEffect(() => {
    fetchSolicitudes();
    fetchAsignaciones();
  }, []);

  const fetchSolicitudes = async () => {
    const response = await axios.get('/api/solicitudes');
    setSolicitudes(response.data);
  };

  const fetchAsignaciones = async () => {
    const response = await axios.get('/api/asignaciones');
    setAsignaciones(response.data);
  };

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await axios.post('/api/solicitud', form);
    fetchSolicitudes();
  };

  const fetchSolicitudById = async (id) => {
    const response = await axios.get(`/api/solicitud/${id}`);
    setSelectedSolicitud(response.data);
  };

  const updateSolicitudById = async (id) => {
    await axios.put(`/api/solicitud/${id}`, selectedSolicitud);
    fetchSolicitudes();
  };

  const deleteSolicitudById = async (id) => {
    await axios.delete(`/api/solicitud/${id}`);
    fetchSolicitudes();
    fetchAsignaciones();
  };

  const updateSolicitudStatus = async (id) => {
    await axios.patch(`/api/solicitud/${id}/estatus?estatus=aprobado`);
    fetchSolicitudes();
    fetchAsignaciones();
  };

  return (
    <div>
      <h1>Solicitudes de Estudiantes</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" name="nombre" placeholder="Nombre" value={form.nombre} onChange={handleChange} />
        <input type="text" name="apellido" placeholder="Apellido" value={form.apellido} onChange={handleChange} />
        <input type="text" name="identificacion" placeholder="Identificación" value={form.identificacion} onChange={handleChange} />
        <input type="number" name="edad" placeholder="Edad" value={form.edad} onChange={handleChange} />
        <select name="afinidad_magica" value={form.afinidad_magica} onChange={handleChange}>
          <option value="Oscuridad">Oscuridad</option>
          <option value="Luz">Luz</option>
          <option value="Fuego">Fuego</option>
          <option value="Agua">Agua</option>
          <option value="Viento">Viento</option>
          <option value="Tierra">Tierra</option>
        </select>
        <button type="submit">Enviar Solicitud</button>
      </form>
      <h2>Lista de Solicitudes</h2>
      <ul>
        {solicitudes.map((solicitud) => (
          <li key={solicitud.id}>
            ID: {solicitud.id} {solicitud.nombre} {solicitud.apellido} ({solicitud.estatus})
            <button onClick={() => fetchSolicitudById(solicitud.id)}>Ver</button>
            <button onClick={() => deleteSolicitudById(solicitud.id)}>Eliminar</button>
            <button onClick={() => updateSolicitudStatus(solicitud.id)}>Aprobar</button>
          </li>
        ))}
      </ul>
      {selectedSolicitud && (
        <div>
          <h2>Solicitud Detalle</h2>
          <input type="text" name="nombre" value={selectedSolicitud.nombre} onChange={(e) => setSelectedSolicitud({ ...selectedSolicitud, nombre: e.target.value })} />
          <input type="text" name="apellido" value={selectedSolicitud.apellido} onChange={(e) => setSelectedSolicitud({ ...selectedSolicitud, apellido: e.target.value })} />
          <input type="text" name="identificacion" value={selectedSolicitud.identificacion} onChange={(e) => setSelectedSolicitud({ ...selectedSolicitud, identificacion: e.target.value })} />
          <input type="number" name="edad" value={selectedSolicitud.edad} onChange={(e) => setSelectedSolicitud({ ...selectedSolicitud, edad: e.target.value })} />
          <select name="afinidad_magica" value={selectedSolicitud.afinidad_magica} onChange={(e) => setSelectedSolicitud({ ...selectedSolicitud, afinidad_magica: e.target.value })}>
            <option value="Oscuridad">Oscuridad</option>
            <option value="Luz">Luz</option>
            <option value="Fuego">Fuego</option>
            <option value="Agua">Agua</option>
            <option value="Viento">Viento</option>
            <option value="Tierra">Tierra</option>
          </select>
          <div style={{ marginTop: '10px' }}>
            <button onClick={() => updateSolicitudById(selectedSolicitud.id)}>Update</button>
            <span style={{ margin: '0 5px' }}></span>
            <button onClick={() => setSelectedSolicitud(null)}>Close</button>
          </div>
        </div>
      )}

      <h1>Asignaciones de Grimorios</h1>
      <ul>
        {asignaciones.map((asignacion) => (
          <li key={asignacion.id}>
            Solicitud ID: {asignacion.solicitud_id} - Grimorio: {asignacion.grimorio}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
