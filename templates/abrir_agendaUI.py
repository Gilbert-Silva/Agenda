import streamlit as st
import views
import time
import datetime

class AbrirAgendaUI:

  def abrir_agenda():
    data = st.text_input("Informe a data no formato *dd/mm/aaaa*")
    hinicio = st.text_input("Informe o horário inicial no formato *HH\:MM*")
    hfim = st.text_input("Informe o horário final no formato *HH\:MM*")
    intervalo = st.text_input("Informe o intervalo entre os horários (min)")

    if st.button("Inserir Horários"):
      #data = datetime.datetime.strptime(datastr, "%d/%m/%Y %H:%M")
      views.agenda_abrir_agenda(data, hinicio, hfim, int(intervalo))
      st.success("horário(s) inserido(s) com sucesso")
      time.sleep(2)
      st.experimental_rerun()

  def main():
    st.header("Abrir Agenda do Dia")
    AbrirAgendaUI.abrir_agenda()
 