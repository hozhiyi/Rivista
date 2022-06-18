import streamlit as st
import main

txt = main.send_txt()
st.write(txt)