
import streamlit as st
from streamlit_image_comparison import image_comparison
st.set_page_config(
    page_title="DASHBOARD PROTEINAS",
    page_icon="🧬",
    layout="centered")

st.sidebar.title("ÍNDICE DE ESTRUCTURAS")
st.sidebar.caption("descripcion breve ajaa")

with st.sidebar.expander("Estructuras tipo 1"):
    st.caption("balbask")


st.markdown("### ESTRUCTURA TIPO I")
st.write("Colágeno estructura tipo I")
image_comparison(
  img1="Col_T1.jpg",
  img2="colágeno_TIPO1.jpg",
   label1="Estructura molecular",
    label2="Estructura",
)
st.markdown("### ESTRUCTURA TIPO III")
st.write("Colágeno estructura tipo III")
image_comparison(
  img1="estructuracolag3.jpg",
  img2="Colag.Tipo3.jpg",
   label1="Estructura molecular  ",
    label2="Estructura",
)
#streamlit run proyectofinal.py
