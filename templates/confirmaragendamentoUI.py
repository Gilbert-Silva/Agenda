import streamlit as st
import pandas as pd
from views import View

class ConfirmarAgendamentoUI:
  def main():
    st.header("Confirmar Agendamento")
    ConfirmarAgendamentoUI.listar()    
  
  def listar():
    agendas = View.agenda_listar_nao_confirmados()
    if len(agendas) == 0:
      st.write("Nenhuma agenda disponível")
    else:  
      #df = []
      #for obj in agendas: df.append(obj.__dict__)
      #st.dataframe(df, use_container_width=True)
      dic = []
      for obj in agendas: dic.append(obj.to_json())
      df = pd.DataFrame(dic)
      with st.form("form_confirm_agendamento"):
        edited_df = st.data_editor(df, key="df")
        submitted = st.form_submit_button("Confirmar")
      if submitted:
        #st.write(st.session_state["df"]["edited_rows"])
        for key in st.session_state["df"]["edited_rows"]:
          #st.write(key)
          #st.write(edited_df.iloc[key])
          st.write(edited_df.iloc[key]["id"])
          st.write(edited_df.iloc[key]["confirmado"])
          id = edited_df.iloc[key]["id"]
          conf = edited_df.iloc[key]["confirmado"]
          View.agenda_confirmar_agendamento(id, conf)







