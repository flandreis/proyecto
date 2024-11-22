
import streamlit as st
from streamlit_image_comparison import image_comparison
st.set_page_config(
    page_title="DASHBOARD PROTEINAS",
    page_icon="🧬",
    layout="centered")
menu = ["Proteínas", "TIPO I", "TIPO II", "TIPO III", "TIPO IV"]
opcion = st.sidebar.selectbox("ÍNDICE DE ESTRUCTURAS", menu)
if opcion == "Proteínas":
    st.title("Descripción")
    st.write("blablablaba")
    st.write("Colágeno estructura tipo I")
    image_comparison(
        img1="Col_T1.jpg",
        img2="colágeno_TIPO1.jpg",
        label1="Estructura molecular",
        label2="Estructura",
    )
elif opcion == "TIPO I":
    st.write("Has seleccionado Tipo I")
    st.write("Colágeno estructura tipo I")
    image_comparison(
        img1="Col_T1.jpg",
        img2="colágeno_TIPO1.jpg",
        label1="Estructura molecular",
        label2="Estructura",
    )
elif opcion == "TIPO II":
    st.write("Has seleccionado Tipo II")
    st.write("Colágeno estructura tipo II (agregar contenido aquí)")
elif opcion == "TIPO III":
    st.write("Has seleccionado TIPO III")
    st.title("ESTRUCTURAS TIPO III")
    st.write("bkbalblaba")
    st.write("Colágeno estructura tipo III")
    image_comparison(
        img1="estructuracolag3.jpg",
        img2="Colag.Tipo3.jpg",
        label1="Estructura molecular",
        label2="Estructura",
    )
elif opcion == "TIPO IV":
    st.write("Has seleccionado Tipo IV")
else:
    st.write("Selecciona una opción del menú.")

#streamlit run proyectofinal.py
