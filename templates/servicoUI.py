import streamlit as st
import views

class ServicoUI:
  def listar():
    clientes = views.cliente_listar()
    df = []
    for obj in clientes: df.append(obj.__dict__)
    st.dataframe(df, use_container_width=True)

  def inserir():
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o email")
    fone = st.text_input("Informe o fone")
    if st.button("Inserir"):
      views.cliente_inserir(nome, email, fone)
      st.success("Serviço inserido com sucesso")
      st.experimental_rerun()

  def atualizar():
    clientes = views.cliente_listar()
    op = st.selectbox("Atualização de Serviços", clientes)
    nome = st.text_input("Informe o novo nome")
    email = st.text_input("Informe o novo email")
    fone = st.text_input("Informe o novo fone")
    if st.button("Atualizar"):
      st.write(op._id)
      views.cliente_atualizar(nome, email, fone, op._id)
      st.success("Serviço atualizado com sucesso")
      st.experimental_rerun()

  def excluir():
    clientes = views.cliente_listar()
    op = st.selectbox("Exclusão de Serviços", clientes)
    if st.button("Excluir"):
      views.cliente_excluir(op._id)
      st.success("Serviço excluído com sucesso")
      st.experimental_rerun()

  def main():
    st.header("Cadastro de Serviços")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ServicoUI.listar()
    with tab2: ServicoUI.inserir()
    with tab3: ServicoUI.atualizar()
    with tab4: ServicoUI.excluir()

