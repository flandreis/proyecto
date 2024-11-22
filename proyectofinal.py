
import streamlit as st
from streamlit_image_comparison import image_comparison
st.set_page_config(
    page_title="DASHBOARD PROTEINAS",
    page_icon="🧬",
    layout="centered")
menu = ["Proteínas", "Colágeno", "Estructura primaria", "TIPO II", "TIPO III", "TIPO IV"]
opcion = st.sidebar.selectbox("ÍNDICE DE ESTRUCTURAS", menu)
if opcion == "Proteínas":
    st.title("Descripción")
    st.write("Las proteínas son biomoléculas esenciales para la vida, formadas por cadenas de aminoácidos unidos mediante enlaces peptídicos. Desempeñan funciones clave en casi todos los procesos biológicos, como la catálisis de reacciones (enzimas), transporte de moléculas (hemoglobina), soporte estructural (colágeno), defensa (anticuerpos) y regulación de procesos celulares (hormonas y receptores).")
    st.write("Las proteínas tienen diferentes niveles de organización estructural que determinan su función")

elif opcion == "Colágeno":
    st.tile("COLÁGENO")
    st.write("")


elif opcion == "Estructura primaria":
    st.title("Colágeno tipo I")   
    st.write("Has seleccionado estructura de tipo I")
    st.write("Es la secuencia lineal de aminoácidos en una cadena polipeptídica, determinada por el código genético, define el orden en que los aminoácidos están dispuestos y dicta cómo se pliega la proteína en niveles superiores.")
    
    image_comparison(
        img1="Col_T1.jpg",
        img2="colágeno_TIPO1.jpg",
        label1="Estructura molecular",
        label2="Estructura",
    )
elif opcion == "TIPO II":
    st.write("Has seleccionado Tipo II")
    st.write("Colágeno estructura tipo II")


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
