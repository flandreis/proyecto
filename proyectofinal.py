
import streamlit as st
from streamlit_image_comparison import image_comparison
st.set_page_config(
    page_title="DASHBOARD PROTEINAS",
    page_icon="🧬",
    layout="centered")
menu = ["Proteínas", "Colágeno", "Estructura primaria", "Estructura secundaria", "Estructura terciaria", "Estructura cuarternaria"]
opcion = st.sidebar.selectbox("ÍNDICE DE ESTRUCTURAS", menu)
if opcion == "Proteínas":
    st.title("Descripción")
    st.write("Las proteínas son biomoléculas esenciales para la vida, formadas por cadenas de aminoácidos unidos mediante enlaces peptídicos. Desempeñan funciones clave en casi todos los procesos biológicos, como la catálisis de reacciones (enzimas), transporte de moléculas (hemoglobina), soporte estructural (colágeno), defensa (anticuerpos) y regulación de procesos celulares (hormonas y receptores).")
    st.write("Las proteínas tienen diferentes niveles de organización estructural que determinan su función")
    st.title("Tipos de representacion biomolecular")
    st.head("Representación stick o molecular detallada")
    st.write("Es un modelo detallado que representa cada átomo y enlace químico en la molécula donde los átomos se muestran como esferas o puntos, mientras que los enlaces químicos son líneas que los conectan.") 
    st.write("Tomamos como referencia esta representacion ya que es útil para estudiar interacciones moleculares como enlaces de hidrógeno y la conformación local de la proteína. También porque muestra los átomos por distintos colores")
   
    st.head("Representación de superficie molecular")
    st.write("Es una representación de la superficie externa de la molécula, construida en base al volumen ocupado por los átomos. Simula cómo se miraría la molécula desde el exterior, incluyendo sus cavidades, canales o zonas de contacto.")

elif opcion == "Colágeno":
    st.title("COLÁGENO, LA PROTEÍNA ESTRUCTURAL CLAVE", )
    st.write("El colágeno es la proteína más abundante en los mamíferos y desempeña un papel fundamental en la estructura y soporte de tejidos conectivos, como la piel, los huesos, los tendones, los cartílagos y los vasos sanguíneos. Es una proteína fibrosa que proporciona fuerza, flexibilidad y resistencia a los tejidos.")


elif opcion == "Estructura primaria":
    st.title("ESTRUCTURA PRIMARIA")   
    st.write("Has seleccionado estructura de tipo I. **cursiva**")
    st.write("Es la secuencia lineal de aminoácidos en una cadena polipeptídica, determinada por el código genético, define el orden en que los aminoácidos están dispuestos y dicta cómo se pliega la proteína en niveles superiores.")
    st.write("A continuación se podrá visualizar la estructura molecular del colágeno.")   
    image_comparison(
        img1="Col_T1.jpg",
        img2="colágeno_TIPO1.jpg",
        label1="representación molecular",
        label2="superficie molecular",
    )
    st.write("Colágeno tipo I es el más abundante ya que se encuentra en la piel, huesos, tendones, ligamentos y córnea. Su función brinda fuerza tensil y resistencia.")
    
elif opcion == "Estructura secundaria":
    st.title("ESTRUCTURA SECUNDARIA") 
    st.write("Has seleccionado estructura de tipo II")
    st.write("Es la organización local de segmentos de la cadena polipeptídica en patrones repetitivos estabilizados por enlaces de hidrógeno. Proporciona estabilidad y contribuye al plegamiento global.")
    st.write("Hélice alfa (α): Una estructura helicoidal en espiral. Lámina beta (β): Segmentos extendidos que forman una hoja plegada.")
    image_comparison(
        img1="col2mjpg",
        img2="col2.jpg",
        label1="representación molecular",
        label2="superficie molecular",
    )


elif opcion == "TEstructura terciaria":
    st.title("ESTRUCTURAS TIPO III")
    st.write("Has seleccionado estructura de tipo III")
    st.write("Es el plegamiento tridimensional completo de una cadena polipeptídica, estabilizado por interacciones entre los grupos R (radicales) de los aminoácidos.")
    
   
    image_comparison(
        img1="estructuracolag3.jpg",
        img2="Colag.Tipo3.jpg",
        label1="Estructura molecular",
        label2="Estructura",
    )
elif opcion == "Estructura cuarternaria":
    st.write("Has seleccionado Tipo IV")
else:
    st.write("Selecciona una opción del menú.")

#streamlit run proyectofinal.py
