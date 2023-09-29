import streamlit as st
import sqlite3

# Crear una conexión a la base de datos SQLite
conn = sqlite3.connect('clientes.db')
c = conn.cursor()

# Crear la tabla de clientes si no existe
c.execute('''CREATE TABLE IF NOT EXISTS clientes
             (nombre TEXT, email TEXT, telefono TEXT)''')

# Crear el formulario de cliente
st.header('Formulario de Cliente')
nombre = st.text_input('Nombre')
email = st.text_input('Email')
telefono = st.text_input('Teléfono')

# Guardar los datos del cliente en la base de datos al hacer clic en el botón "Guardar"
if st.button('Guardar'):
    c.execute("INSERT INTO clientes VALUES (?, ?, ?)", (nombre, email, telefono))
    conn.commit()
    st.success('¡Cliente guardado exitosamente!')

# Mostrar la lista de clientes guardados en la base de datos
st.header('Lista de Clientes')
clientes = c.execute("SELECT rowid, * FROM clientes")
for cliente in clientes:
    st.write(cliente[0], cliente[1], cliente[2], cliente[3])

# Crear el formulario para editar o eliminar un cliente
st.header('Editar o Eliminar Cliente')
cliente_id = st.number_input('ID del Cliente', min_value=1)
editar = st.checkbox('Editar')
eliminar = st.checkbox('Eliminar')

if editar:
    nuevo_nombre = st.text_input('Nuevo Nombre', value=cliente[1])
    nuevo_email = st.text_input('Nuevo Email', value=cliente[2])
    nuevo_telefono = st.text_input('Nuevo Teléfono', value=cliente[3])
    if st.button('Actualizar'):
        c.execute("UPDATE clientes SET nombre=?, email=?, telefono=? WHERE rowid=?", (nuevo_nombre, nuevo_email, nuevo_telefono, cliente_id))
        conn.commit()
        st.success('¡Cliente actualizado exitosamente!')

if eliminar:
    confirmacion = st.checkbox(f'¿Estás seguro que deseas eliminar el cliente con ID {cliente_id}?')
    if confirmacion:
        c.execute("DELETE FROM clientes WHERE rowid=?", (cliente_id,))
        conn.commit()
        st.success(f'¡Cliente con ID {cliente_id} eliminado exitosamente!')

# Cerrar la conexión a la base de datos al finalizar
conn.close()
