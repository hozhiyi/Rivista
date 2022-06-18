#Diary page
import streamlit as st

date = st.date_input("Date")

txt = st.text_area("Write about your day!")


st.download_button(label="Save diary", data=txt, file_name='diary')
st.button("Analyse this text")

#chunfangnihaoshuai