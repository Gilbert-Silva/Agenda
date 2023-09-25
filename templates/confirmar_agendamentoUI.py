import streamlit as st
import views
import time
import datetime

class ConfirmarAgendamentoUI:
  def listar():
    agendas = views.agenda_listar_nao_confirmados()
    if len(agendas) == 0:
      st.write("Nenhuma agenda disponível")
    else:  
      df = []
      for obj in agendas: df.append(obj.__dict__)
      st.dataframe(df, use_container_width=True)

  def main():
    st.header("Confirmar Agendamento")
    ConfirmarAgendamentoUI.listar()    