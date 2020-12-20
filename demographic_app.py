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

    #r = requests.post(
        #"https://api.deepai.org/api/demographic-recognition",
        #files={
            #'image': uploaded_file,
        #},
        #headers={'api-key': 'ed22d0b2-4cc5-4223-9e48-302f8a86c7c5'}
    #)

    #response_data = r.json()
    #resultado = response_data['output']['faces'][0]
    ##st.text("Resultado: {}.".format(resultado))
    
    #age = resultado['age_range']
    #st.text("Su edad está en el rango: {}-{} años.".format(age[0],age[1])) 

    #gender = resultado['gender']
    #if gender=='Male':
        #st.text("Ud. es hombre.")
    #else:
	    #st.text("Ud. es mujer.")

    #demography = resultado['cultural_appearance']
    #st.text("Su apariencia demográfica es: {}.".format(demography))


    r2 = requests.post("https://api.deepai.org/api/facial-expression-recognition",
        files={
            'image': uploaded_file,
        },
        headers={'api-key': 'ed22d0b2-4cc5-4223-9e48-302f8a86c7c5'}
     )
    response_data2 = r2.json()
    #st.text("emocion: {}.".format(response_data2))
    #resultado2 = response_data2['output']
    resultado2 = response_data2['output']['expressions'][0]
    emocion = resultado['emotion']
    st.text("Su emoción es: {}.".format(emocion))

    #st.subheader("Hasta luego!")
        
