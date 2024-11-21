
import streamlit as st
from streamlit_image_comparison import image_comparison
st.set_page_config("TIPO DE ESTRUCTURAS EN LAS PROTEÍNAS")
st.header(" TIPO DE ESTRUCTURAS EN LAS PROTEÍNAS")

st.write("")
"TIPOS DE ESTRUCTURAS Y SUS DIFERENCIAS"
st.write("")

st.markdown("### ESTRUCTURA TIPO 1")
image_comparison(
  img1="Col_T1.jpg",
  img2="colágeno_TIPO1.jpg",
   label1="Estructura  ",
    label2="Estructura molecular",
)
#streamlit run proyectofinal.py