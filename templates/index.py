import streamlit as st
import clientepage, servicopage

op = st.sidebar.selectbox("Menu", ["Clientes", "Serviços"])
if op == "Clientes": clientepage.main()
if op == "Serviços": servicopage.main()

