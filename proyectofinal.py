
import streamlit as st
from streamlit_image_comparison import image_comparison
st.set_page_config(
    page_title="DASHBOARD PROTEINAS",
    page_icon="🧬",
    layout="centered")
#menu["Proteínas", "TIPO I", "TIPO II", "TIPO III", "TIPO IV"]
#opcion = st.sidebar.selectbox("ÍNDICE DE ESTRUCTURAS",menu)
#st.sidebar.caption("descripcion breve ajaa")
import argparse

parser = argparse.ArgumentParser(description="Menú interactivo en terminal")
parser.add_argument("opcion", type=str, help="Selecciona una opción: Proteínas, TIPO I, TIPO II, TIPO III")

args = parser.parse_args()

if args.opcion == "Proteínas":
    print("Contenido sobre proteínas.")
elif args.opcion == "TIPO I":
    print("Descripción de la estructura TIPO I.")
elif args.opcion == "TIPO II":
    print("Descripción de la estructura TIPO II.")
else:
    print("Opción no válida.")


#streamlit run proyectofinal.py
