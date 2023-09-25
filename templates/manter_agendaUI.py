import streamlit as st
import views
import time
import datetime

class ManterAgendaUI:
  def listar():
    agendas = views.agenda_listar()
    if len(agendas) == 0:
      st.write("Nenhuma agenda disponível")
    else:  
      df = []
      for obj in agendas: df.append(obj.__dict__)
      st.dataframe(df, use_container_width=True)

  def inserir():
    datastr = st.text_input("Informe a data no formato *dd/mm/aaaa HH\:MM*")
    clientes = views.cliente_listar()
    cliente = st.selectbox("Selecione o cliente", clientes)
    servicos = views.servico_listar()
    servico = st.selectbox("Selecione o serviço", servicos)
  
    if st.button("Inserir"):
      data = datetime.datetime.strptime(datastr, "%d/%m/%Y %H:%M")
      views.agenda_inserir(data, True, cliente._id, servico._id)
      st.success("horário inserido com sucesso")
      time.sleep(2)
      st.experimental_rerun()

  def atualizar():
    agendas = views.agenda_listar()
    if len(agendas) == 0:
      st.write("Nenhuma agenda disponível")
    else:  
      op = st.selectbox("Atualização de horários", agendas)
      datastr = st.text_input("Informe a nova data no formato *dd/mm/aaaa HH\:MM*")
      if st.button("Atualizar"):
        data = datetime.datetime.strptime(datastr, "%d/%m/%Y %H:%M")
        views.agenda_atualizar(op._id, data, op._confirmado, op._id_cliente, op._id_servico)
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
    st.header("Cadastro de Horários")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterAgendaUI.listar()
    with tab2: ManterAgendaUI.inserir()
    with tab3: ManterAgendaUI.atualizar()
    with tab4: ManterAgendaUI.excluir()
