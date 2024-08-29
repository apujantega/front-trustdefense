import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Aplicación de ejemplo con Streamlit")

# Introducción de datos por el usuario
st.header("Introducir datos")
nombre = st.text_input("Nombre")
edad = st.slider("Edad", 0, 100, 25)
altura = st.number_input("Altura en cm", 100, 250, 170)

# Mostrar los datos introducidos
st.subheader("Datos introducidos")
st.write(f"Nombre: {nombre}")
st.write(f"Edad: {edad}")
st.write(f"Altura: {altura} cm")

# Generar un gráfico simple
st.header("Gráfico de Ejemplo")
datos = {'Categoría': ['Edad', 'Altura'],
         'Valores': [edad, altura]}
df = pd.DataFrame(datos)

fig, ax = plt.subplots()
ax.bar(df['Categoría'], df['Valores'], color=['blue', 'green'])
ax.set_ylabel('Valores')

st.pyplot(fig)

# Pie de página
st.write("Esta es una aplicación sencilla creada con Streamlit.")
