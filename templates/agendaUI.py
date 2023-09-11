import streamlit as st
import views
import time
import datetime

class AgendaUI:
  def listar():
    agendas = views.agenda_listar()
    if len(agendas) == 0:
      st.write("Nenhuma agenda disponível")
    else:  
      df = []
      for obj in agendas: df.append(obj.__dict__)
      st.dataframe(df, use_container_width=True)

  def inserir():
    data = st.text_input("Informe a data dd/mm/aaaa")
    hinicio = st.text_input("Informe o horário inicial hh:mm")
    hfim = st.text_input("Informe o horário final hh:mm")
    intervalo = st.text_input("Informe o intervalo entre os horários (min)")

    if st.button("Inserir"):
      #data = datetime.datetime.strptime(datastr, "%d/%m/%Y %H:%M")
      views.agenda_inserir(data, hinicio, hfim, int(intervalo))
      st.success("horário(s) inserido(s) com sucesso")
      time.sleep(2)
      st.experimental_rerun()

  def atualizar():
    agendas = views.agenda_listar()
    if len(agendas) == 0:
      st.write("Nenhuma agenda disponível")
    else:  
      op = st.selectbox("Atualização de horários", agendas)
      datastr = st.text_input("Informe a nova data dd/mm/aaaa HH:MM: ")
      if st.button("Atualizar"):
        data = datetime.datetime.strptime(datastr, "%d/%m/%Y %H:%M")
        views.agenda_atualizar(op._id, data, op._confirmado, 0, 0)
        st.success("horário atualizado com sucesso")
        time.sleep(2)
        st.experimental_rerun()

  def excluir():
    agendas = views.agenda_listar()
    if len(agendas) == 0:
      st.write("Nenhuma agenda disponível")
    else:  
      op = st.selectbox("Exclusão de horários", agendas)
      if st.button("Excluir"):
        views.agenda_excluir(op._id)
        st.success("horário excluído com sucesso")
        time.sleep(2)
        st.experimental_rerun()
  
  def main():
    st.header("Cadastro de horários")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: AgendaUI.listar()
    with tab2: AgendaUI.inserir()
    with tab3: AgendaUI.atualizar()
    with tab4: AgendaUI.excluir()
