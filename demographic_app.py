#!/usr/bin/env python3
import streamlit as st
import json
import requests

# ***********************************
# MAIN
# ***********************************
st.set_option('deprecation.showfileUploaderEncoding', False)

st.title("Características faciales")
#st.header("Hola! soy el dibujante de createch y haré una caricatura de tu foto :smile:")
#st.markdown("Hola! soy **creaRec**, el primer reconocedor de createch :smile:")

st.subheader("Suba una imagen tipo selfie y le diré lo que veo a partir de su cara:")

uploaded_file = st.file_uploader("", type="jpg")
if uploaded_file is not None:

    st.image(uploaded_file, caption='Imagen analizada', use_column_width=True)

    
    ### DEMOGRAPHIC
    r = requests.post(
        "https://api.deepai.org/api/demographic-recognition",
        files={
            'image': uploaded_file,
        },
        headers={'api-key': 'ed22d0b2-4cc5-4223-9e48-302f8a86c7c5'}
    )


    response_data = r.json()
    resultado = response_data['output']['faces'][0]
    #st.text("Resultado: {}.".format(resultado))
    
    age = resultado['age_range']
    st.text("Su edad está en el rango: {}-{} años.".format(age[0],age[1])) 

    gender = resultado['gender']
    gconf = resultado['gender_confidence']
    if gender=='Male':
        st.text("Ud. es hombre (certeza: {}).".format(gconf)
    else:
	    st.text("Ud. es mujer (certeza: {}).".format(gconf)

    demography = resultado['cultural_appearance']
    if demography=='Latino':
        st.text("Su apariencia demográfica es latina.")
    elif demography=='White':
        st.text("Su apariencia demográfica es caucásica.")
    elif demography=='Asian':
        st.text("Su apariencia demográfica es asiática.")
    elif demography=='Black':
        st.text("Su apariencia demográfica es africana subsahariana.")
    else:
        st.text("Su apariencia demográfica es: {}.".format(demography))

    ### EXPRESSION
    #r2 = requests.post("https://api.deepai.org/api/facial-expression-recognition",
        #files={
            #'image': uploaded_file,
        #},
        #headers={'api-key': 'ed22d0b2-4cc5-4223-9e48-302f8a86c7c5'}
     #)
    #response_data2 = r2.json()
    #resultado2 = response_data2['output']['expressions'][0]
    #emocion = resultado2['emotion']
    ##st.text("Su emoción es: {}.".format(emocion))
    #if emocion=='anger':
        #st.text("Su expresión facial denota enojo.")
    #elif emocion=='disgust':
        #st.text("Su expresión facial denota disgusto.")
    #elif emocion=='fear':
        #st.text("Su expresión facial denota miedo.")
    #elif emocion=='happy':
        #st.text("Su expresión facial denota alegría.")
    #elif emocion=='sad':
        #st.text("Su expresión facial denota tristeza.")
    #elif emocion=='surprise':
        #st.text("Su expresión facial denota sorpresa.")
    #elif emocion=='neutral':
        #st.text("Su expresión facial es neutral.")
    #else:
        #st.text("Su emoción es: {}.".format(emocion))


    st.subheader("Hasta luego!")
        
