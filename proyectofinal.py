
import streamlit as st
from streamlit_image_comparison import image_comparison
st.set_page_config(
    page_title="DASHBOARD PROTEINAS",
    page_icon="🧬",
    layout="centered")
menu["Proteínas", "TIPO I", "TIPO II", "TIPO III", "TIPO IV"]

opcion = st.sidebar.selectbox("ÍNDICE DE ESTRUCTURAS",menu)
st.sidebar.caption("descripcion breve ajaa")

if opcion == "Proteínas":
    st.title("Descripción")
    st.write("blablablaba")
st.markdown("### ESTRUCTURA TIPO I")
st.write("Colágeno estructura tipo I")
image_comparison(
  img1="Col_T1.jpg",
  img2="colágeno_TIPO1.jpg",
   label1="Estructura molecular",
    label2="Estructura",
)

else opcion == "TIPO III":
    st.title("ESTRUCTURAS TIPO III")
    st.write("bkbalblaba")
st.markdown("### ESTRUCTURA TIPO III")
st.write("Colágeno estructura tipo III")
image_comparison(
  img1="estructuracolag3.jpg",
  img2="Colag.Tipo3.jpg",
   label1="Estructura molecular  ",
    label2="Estructura",
)
#streamlit run proyectofinal.py
