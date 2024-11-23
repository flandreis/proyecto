# st.markdown("## Esto es un encabezado de nivel 2")
#st.markdown("### Subtítulo con `monoespaciado`")


import streamlit as st
from streamlit_image_comparison import image_comparison
from skimage import io, filters, img_as_ubyte
from PIL import Image
def load_css(file_name): 
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
st.set_page_config(
    page_title="DASHBOARD PROTEINAS",
    page_icon="🧬",
    layout="centered"
 )   
load_css("style.css")
menu = ["Proteínas", "Estructura primaria", "Estructura secundaria", "Estructura terciaria", "Estructura cuarternaria", "Colágeno", "Enzimas"]
st.sidebar.header("ÍNDICE")
opcion = st.sidebar.selectbox("ÍNDICE DE ESTRUCTURAS", menu)
st.sidebar.markdown("---")
if opcion == "Proteínas":

    st.title("¿Qué son las proteínas?🫧")
    st.write("Las proteínas, macromoléculas formadas a partir de cadenas lineales de aminoácidos, son la base de todo tejido vivo, ya que representan el 80% del protoplasma celular deshidratado y el 50% del peso en seco de toda asociación tisular en el cuerpo:brain:. Los genes, encerrados en el núcleo en forma de cromosomas, codifican mediante secuencias de ácidos nucleicos la síntesis de proteínas específicas. Gracias a los mecanismos de transcripción y traducción, el código genético :dna: se convierte en los elementos funcionales que dan forma a nuestro cuerpo. Desempeñan funciones clave en casi todos los procesos biológicos, como la catálisis de reacciones (enzimas), transporte de moléculas (hemoglobina:drop_of_blood:), soporte estructural (colágeno:worm:), defensa (anticuerpos:anatomical_heart:) y regulación de procesos celulares (hormonas y receptores).")
    st.write(" *Las proteínas tienen diferentes niveles de organización estructural que determinan su función* ")
    st.image("COLAGENO3.png", width=300)
    st.title("Tipos de representacion biomolecular")
    st.markdown("## Representación *stick* o molecular detallada")
    st.image("Chimerem.png", width=150)

    
    st.write("Es un modelo detallado que representa cada átomo y enlace químico en la molécula donde los átomos se muestran como esferas o puntos, mientras que los enlaces químicos son líneas que los conectan.")
    st.write("Tomamos como referencia esta representacion ya que es útil para estudiar interacciones moleculares como enlaces de hidrógeno y la conformación local de la proteína. También porque muestra los átomos por distintos colores")
   
    st.markdown("## Representación de superficie molecular")
    st.write("Es una representación de la superficie externa de la molécula, construida en base al volumen ocupado por los átomos. Simula cómo se miraría la molécula desde el exterior, incluyendo sus cavidades, canales o zonas de contacto.")
    st.image("mmm.png", width=150)

elif opcion == "Estructura primaria":
    st.title("ESTRUCTURA PRIMARIA")   
    st.write("Has seleccionado estructura de tipo I.")
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
    st.write("Es la organización local de segmentos de la cadena polipeptídica en patrones repetitivos estabilizados por enlaces de hidrógeno. Su función es proporciona estabilidad y contribuye al plegamiento global.⌬")
    st.write("Hélice alfa (α): Una estructura helicoidal en espiral. Lámina beta (β): Segmentos extendidos que forman una hoja plegada.")

    image_comparison( 
        img1="col2m.jpg", 
        img2="col2.jpg", 
        label1="representación molecular", 
        label2="superficie molecular", 
    )
    st.write("El cartílago tipo II se encuentra en cartílago, humor vítreo del ojo, y tiene como función proporcionar elasticidad y resistencia al cartílago.")
    
elif opcion == "Estructura terciaria":
    st.title("ESTRUCTURA TERCIARIA")
    st.write("Has seleccionado estructura de tipo III")
    st.write("Es el plegamiento tridimensional completo de una cadena polipeptídica, estabilizado por interacciones entre los grupos R (radicales) de los aminoácidos. Con interacciones clave: Puentes disulfuro, interacciones hidrofóbicas, enlaces iónicos y de hidrógeno. Aquí se define la forma específica de la proteína y su función biológica.")
    
    image_comparison(
        img1="estructuracolag3.jpg",
        img2="Colag.Tipo3.jpg",
        label1="representación molecular", 
        label2="superficie molecular", 
    )
    st.write("Se encuentra en los vasos sanguíneos, piel, músculos y órganos, y su función principal es el soporte estructural en tejidos elásticos.")
    st.write("Tres cadenas polipeptídicas (cadenas alfa) se enrollan formando una triple hélice (superhélice) estabilizada por enlaces de hidrógeno y enlaces covalentes cruzados.")

elif opcion == "Estructura cuarternaria":
    st.title("ESTRUCTURA CUATERNARIA")
    st.write("Has seleccionado Tipo IV")
    st.write("Es la organización de múltiples cadenas polipeptídicas (subunidades) en una única proteína funcional.")

    image_comparison(
        img1="COL4M.jpg",
        img2="col4.jpg",
        label1="representación molecular", 
        label2="superficie molecular", 
    )
    st.write("Se encuentra principalmente en la membrana basal (estructura que separa el epitelio del tejido conectivo) con  la función de filtración selectiva y soporte a las células epiteliales.")
    st.write("En los tejidos, las moléculas de colágeno se ensamblan en fibras que proporcionan resistencia mecánica.")

elif opcion == "Colágeno":
    st.title("COLÁGENO, LA PROTEÍNA ESTRUCTURAL CLAVE:microbe:", )
    st.markdown("# ¿Qué es el colágeno? ")
    st.write("El colágeno es la proteína fibrosa más abundante en la matriz extracelular y en el tejido conectivo. Es uno de los componentes principales de la piel y los huesos y, por tanto, cubre aproximadamente el 25% de la masa proteica del organismo humano. También se encuentra en tendones, ligamentos y cartílagos. Dependiendo del grado de mineralización, el colágeno puede ser rígido, maleable o encontrarse en un amplio espectro entre ambos términos.")
    st.markdown("# Tipos de colágeno:bone:")
    st.write("Según el tipo de cadenas que presentan, su disposición, su localización y la interrelación con otros elementos, se pueden detectar varios tipos de colágeno, esta proteína está formada por distintos tipos de cadenas y, según su disposición (fibras, redes, redes hexagonales, asociados a fibras o transmembrana), se pueden contar varios tipos de colágeno, con funcionalidades distintas.")
    st.image("co.jpg", width=500)

elif opcion == "Enzimas":
    st.title("¿Qué son las enzimas?")
    st.markdown("# AMILASA")
    st.write("que es amilasa")
    image_comparison(
        img1="amimol.jpg",
        img2="amisup.jpg",
        label1="representación molecular", 
        label2="superficie molecular", 
    )
    st.write("que es amilasa")
    st.markdown("---")
    st.markdown("# LACTASA")
    image_comparison(
        img1="lacmol.jpg",
        img2="lacsup.jpg",
        label1="representación molecular", 
        label2="superficie molecular", 
    )

else:
    st.write("Selecciona una opción del menú.")
#streamlit run proyectofinal.py
