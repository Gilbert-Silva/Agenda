import streamlit as st

def main():
    st.header("Clientes")

"""

import sys
sys.path.append("../models")
from models import Cliente, NCliente

def main():
    st.header("Clientes")
    st.text("Inserir um novo cliente")
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o email")
    fone = st.text_input("Informe o fone")
    if st.button("Inserir"):
        NCliente.Inserir(Cliente(nome, email, fone))
        st.success("Contato inserido com sucesso")
    if st.button("Listar"):
        for obj in NCliente.Listar(): st.text(obj)
        #op = st.selectbox("Clientes", NCliente.Listar())
"""