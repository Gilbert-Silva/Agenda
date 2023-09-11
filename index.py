import streamlit as st
from templates.clienteUI import ClienteUI
from templates.inicioUI import InicioUI
from templates.servicoUI import ServicoUI
from templates.agendaUI import AgendaUI

def sidebar():
  op = st.sidebar.selectbox("Menu", ["Início", "Clientes", "Serviços", "Agenda"])
  if op == "Início": st.session_state["page"] = "inicioUI"
  if op == "Clientes": st.session_state["page"] = "clienteUI"
  if op == "Serviços": st.session_state["page"] = "servicoUI"
  if op == "Agenda": st.session_state["page"] = "agendaUI"

def main():
  sidebar()
  if "page" not in st.session_state: st.session_state["page"] = "inicioUI"
  if st.session_state["page"] == "inicioUI": InicioUI.main()
  if st.session_state["page"] == "clienteUI": ClienteUI.main()
  if st.session_state["page"] == "servicoUI": ServicoUI.main()
  if st.session_state["page"] == "agendaUI": AgendaUI.main()

main()

