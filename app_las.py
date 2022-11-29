#Importando Pacotes 
import pickle
import streamlit as st
 
# Carregando a Máquina Preditiva
pickle_in = open('maquina_preditiva.pkl', 'rb') 
maquina_preditiva = pickle.load(pickle_in)

#Manter a sessão em cache 
@st.cache()
  
# Criando a função que irá fazer a predição usando os dados impostados pelo usuário do Sistema 
def prediction(sexo,empregado,emprestimo,renda,renda_conjuge, historico_credito):   

    # Pre-processando a entrada do Usuário    
    if sexo == "Masculino":
        sexo = 0
    else:
        sexo = 1
 
    if empregado == "Não":
        empregado = 0
    else:
        empregado = 1
 
    if historico_credito == "Débitos Pendentes":
        historico_credito = 0
    else:
        historico_credito = 1  
 
    emprestimo = emprestimo / 1000
 
    # Fazendo Predições
    prediction = maquina_preditiva.predict([[sexo, empregado,emprestimo,renda,renda_conjuge,historico_credito]])
     
    if prediction == 0:
        pred = 'Rejeitado'
    else:
        pred = 'Aprovado'
    return pred
      
  
# Essa função é para criação da webpage  
def main():  

    # Elementos da webpage
    # Nesse Ponto vc deve Personalizar o Sistema com sua Marca
    html_temp = """ 
    <div style ="background-color:blue;padding:13px"> 
    <h1 style ="color:white;text-align:center;">SAE</h1> 
    <h2 style ="color:white;text-align:center;">Projeto Uninove - Professdor Edson</h2> 
    </div> 
    """
      
    # Função do stramlit que faz o display da webpage
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # As linhas abaixo criam as caixas na qual o usuário vai entrar com dados da pessoa que quer o empréstimo para fazer a Predição
    sexo = st.selectbox('Sexo',("Masculino","Feminino"))
    empregado = st.selectbox('Empregado',("Sim","Não")) 
    emprestimo = st.number_input("Empréstimo requisitado:") 
    renda = st.number_input("Renda Mensal") 
    renda_conjuge = st.number_input("Valor Total da renda do conjuge")
    historico_credito = st.selectbox('Histórico de Créditos',("Sem Débitos","Débitos Pendentes"))
    result =""
      
    #Quando o Usuário clicar no botão "Verificar" a Máquina Preditiva faz seu trabalho
    if st.button("Verificar"): 
        result = prediction(sexo, empregado,emprestimo,renda,renda_conjuge, historico_credito) 
        st.success('O empréstimo foi {}'.format(result))
        print(emprestimo)
     
if __name__=='__main__': 
    main()
