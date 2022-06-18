import streamlit as st
#contact us page

with st.container():
    st.title("Need help?")
    st.write("---")
    st.header("Contact information:")
    col1, col2, col3 = st.columns(3)

with col1:
    st.header("Dr. Norharlina Bahar")
    st.write("https://princecourt.com/?doctor=dr-norharlina-bahar")

with col2:
    st.header("Manjung New Hope")
    st.write("""Hotline numbers: 
                01133773093 / 056922612""")

with col3:
    st.header("Befrienders ")
    st.write(
             """Website: https://www.befrienders.org.my/
                
                Hotline numbers: 
                KL: 03-7956 8145 (24 hours)
                Ipoh: 05-547 7933 (4pm to 11pm)
                Penang: 04-281 5161 (3pm to midnight)
                

                E-Mail: sam@befrienders.org.my"""
                )
    