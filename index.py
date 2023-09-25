import streamlit as st
from templates.inicioUI import InicioUI
from templates.manter_clienteUI import ManterClienteUI
from templates.manter_servicoUI import ManterServicoUI
from templates.manter_agendaUI import ManterAgendaUI
from templates.abrir_agendaUI import AbrirAgendaUI
from templates.confirmar_agendamentoUI import ConfirmarAgendamentoUI

def sidebar():
  op = st.sidebar.selectbox("Menu", ["Início", "Manter Clientes", "Manter Serviços", 
                                     "Manter Agenda", "Abrir Agenda do Dia",
                                     "Confirmar Agendamento"])
  if op == "Início": st.session_state["page"] = "inicioUI"
  if op == "Manter Clientes": st.session_state["page"] = "manter_clienteUI"
  if op == "Manter Serviços": st.session_state["page"] = "manter_servicoUI"
  if op == "Manter Agenda": st.session_state["page"] = "manter_agendaUI"
  if op == "Abrir Agenda do Dia": st.session_state["page"] = "abrir_agendaUI"
  if op == "Confirmar Agendamento": st.session_state["page"] = "confirmar_agendamentoUI"


def main():
  sidebar()
  if "page" not in st.session_state: st.session_state["page"] = "inicioUI"
  if st.session_state["page"] == "inicioUI": InicioUI.main()
  if st.session_state["page"] == "manter_clienteUI": ManterClienteUI.main()
  if st.session_state["page"] == "manter_servicoUI": ManterServicoUI.main()
  if st.session_state["page"] == "manter_agendaUI": ManterAgendaUI.main()
  if st.session_state["page"] == "abrir_agendaUI": AbrirAgendaUI.main()
  if st.session_state["page"] == "confirmar_agendamentoUI": ConfirmarAgendamentoUI.main()

main()

