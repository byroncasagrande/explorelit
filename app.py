import streamlit as st
with st.sidebar:        
    nombres = st.text_input("Nombres y apellidos",key=str)
    edad = st.number_input("Edad", min_value=0, max_value=100)    
    agree = st.checkbox("Acepto Terminos y Condiciones")
    if agree:
        st.write("Aceptado!")
    genre = st.radio(
    "Seleccione genero",
    ["Hombre", "Mujer"],
    captions=[
        "",
        "",
    ],
)
    if genre == "Hombre":
        st.write("Selecciono Hombre.")
    else:
        st.write("Selecciono Mujer.")    
    if st.button("Enviar informacion",icon=":material/thumb_up:"):
        st.write("Gracias por enviar la informacion ",nombres)
    else:
        st.write("Goodbye")    
st.title("Mi Primera Aplicación en Streamlit")
st.title("Byron Collazo")