import streamlit as st
import views
import time

class ServicoUI:
  def listar():
    servicos = views.servico_listar()
    if len(servicos) == 0:
      st.write("Nenhum serviço cadastrado")
    else:  
      df = []
      for obj in servicos: df.append(obj.__dict__)
      st.dataframe(df, use_container_width=True)

  def inserir():
    descricao = st.text_input("Informe a descrição")
    valor = st.text_input("Informe o valor")
    duracao = st.text_input("Informe a duração (min)")
    if st.button("Inserir"):
      views.servico_inserir(descricao, float(valor), int(duracao))
      st.success("Serviço inserido com sucesso")
      time.sleep(2)
      st.experimental_rerun()

  def atualizar():
    servicos = views.servico_listar()
    if len(servicos) == 0:
      st.write("Nenhum serviço cadastrado")
    else:  
      op = st.selectbox("Atualização de servicos", servicos)
      descricao = st.text_input("Informe a nova descrição", op._descricao)
      valor = st.text_input("Informe o novo valor", op._valor)
      duracao = st.text_input("Informe a nova duração (min)", op._duracao)
      if st.button("Atualizar"):
        views.servico_atualizar(descricao, float(valor), int(duracao))
        st.success("Serviço atualizado com sucesso")
        time.sleep(2)
        st.experimental_rerun()

  def excluir():
    servicos = views.servico_listar()
    if len(servicos) == 0:
      st.write("Nenhum serviço cadastrado")
    else:  
      op = st.selectbox("Exclusão de servicos", servicos)
      if st.button("Excluir"):
        views.servico_excluir(op._id)
        st.success("Serviço excluído com sucesso")
        time.sleep(2)
        st.experimental_rerun()
  
  def main():
    st.header("Cadastro de serviços")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ServicoUI.listar()
    with tab2: ServicoUI.inserir()
    with tab3: ServicoUI.atualizar()
    with tab4: ServicoUI.excluir()
