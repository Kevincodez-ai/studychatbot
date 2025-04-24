import streamlit as st


def get_temp(key):
    app1 = st.slider("THINKING LEVEL  🧠" , 0.0 , 1.0 , 0.1 , key = key)
    
    return app1