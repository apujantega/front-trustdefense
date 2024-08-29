import streamlit as st
from sqlalchemy import create_engine
import pandas as pd

# Configuración de la conexión a la base de datos MySQL
DATABASE_URI = 'mysql+pymysql://username:password@localhost/trustdefense'
engine = create_engine(DATABASE_URI)

# Función para autenticar usuarios (esqueleto básico)
def autenticar_usuario(username, password):
    # Aquí iría la lógica de autenticación, como consultar una tabla de usuarios en la base de datos
    # Por ahora, se aceptan todos los usuarios para simplificar
    return username == "admin" and password == "password"

# Login del usuario
def login():
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if autenticar_usuario(username, password):
            st.sidebar.success("Login correcto")
            st.session_state['logged_in'] = True
        else:
            st.sidebar.error("Usuario o contraseña incorrecta")

# Vista principal
def vista_principal():
    st.title("Dashboard de TrustDefense")
    
    st.subheader("Vista de Marcas")
    query = "SELECT * FROM brand"
    df = pd.read_sql(query, engine)
    st.dataframe(df)

    st.subheader("Vista de Negocios")
    query = "SELECT * FROM business"
    df = pd.read_sql(query, engine)
    st.dataframe(df)

# Esqueleto de la aplicación
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    login()
else:
    vista_principal()
