import streamlit as st
from templates.clienteUI import ClienteUI
from templates.inicioUI import InicioUI
from templates.servicoUI import ServicoUI

def sidebar():
  op = st.sidebar.selectbox("Menu", ["Início", "Clientes", "Serviços"])
  if op == "Início": st.session_state["page"] = "inicioUI"
  if op == "Clientes": st.session_state["page"] = "clienteUI"
  if op == "Serviços": st.session_state["page"] = "servicoUI"

def main():
  sidebar()
  if "page" not in st.session_state: st.session_state["page"] = "inicioUI"
  if st.session_state["page"] == "inicioUI": InicioUI.main()
  if st.session_state["page"] == "clienteUI": ClienteUI.main()
  if st.session_state["page"] == "servicoUI": ServicoUI.main()

main()

