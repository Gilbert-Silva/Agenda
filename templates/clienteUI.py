import streamlit as st
import views
import time

class ClienteUI:
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
      st.success("Contato inserido com sucesso")
      time.sleep(2)
      st.experimental_rerun()

  def atualizar():
    clientes = views.cliente_listar()
    op = st.selectbox("Atualização de Clientes", clientes)
    nome = st.text_input("Informe o novo nome", op._nome)
    email = st.text_input("Informe o novo email", op._email)
    fone = st.text_input("Informe o novo fone", op._fone)
    if st.button("Atualizar"):
      views.cliente_atualizar(nome, email, fone, op._id)
      st.success("Contato atualizado com sucesso")
      time.sleep(2)
      st.experimental_rerun()

  def excluir():
    clientes = views.cliente_listar()
    op = st.selectbox("Exclusão de Clientes", clientes)
    if st.button("Excluir"):
      views.cliente_excluir(op._id)
      st.success("Contato excluído com sucesso")
      time.sleep(2)
      st.experimental_rerun()
  
  def main():
    st.header("Cadastro de Clientes")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ClienteUI.listar()
    with tab2: ClienteUI.inserir()
    with tab3: ClienteUI.atualizar()
    with tab4: ClienteUI.excluir()
