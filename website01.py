import streamlit as st
import pandas as pd
import hashlib
from PIL import Image

from io import BytesIO
import requests

#ANALISE DE DADOS
import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError


image = Image.open('Monitoria.png')
st.image(image, caption='Web site em desenvolvimento')
st.markdown(":computer:")	
st.title("AMBIENTE DE MONITORIA")
SUB_TITULO = '<p style="font-family:tahoma; color:Green; font-size: 15px;">Desenvolvido pela aluna Isabela Ferreira Paranaíba</p>'
st.markdown(SUB_TITULO, unsafe_allow_html=True)

mystyle = '''
    <style>
        p {
            text-align: justify;
        }
    </style>
    '''
st.markdown(mystyle, unsafe_allow_html=True)
# Generate tree equal columns
#col1, col2, col3 = st.columns((1, 1, 1))
col1, col2 = st.columns((1,1))
with col1:
    st.info(
       """
    ### ***Atenção, calouro!***
    Este material tem o intuito de **auxiliar** os alunos que estão tendo o primeiro contato com linguagem de programação.
    Em comparação com a matéria explanada nas aulas, este terá uma escrita mais informal e de fácil compreenção, com o **MEU** ponto de vista do conteúdo.
    """    
    )
with col2:
    st.info(
    """
    ### ***Vale Lembrar que:***
    O objetivo deste site não é substituir as aulas ministradas pelo professor Massaki Igarashi, tão pouco a monitoria presencial.
    Espero que tenhamos um semestre agradável e de muito aprendizado! Até logo 
    :heart:
    """
    )

st.markdown("""
#### ***Como base para desenvolver esse mateiral, eu usei a programação do site em desenvolvimento do professor Massaki Igarashi.*** """)
st.warning("Site: [link](https://massakiigarashi2-streamlitwebapp-website-5g8yl6.streamlitapp.com/).")
    
#task1 = 
streamlit.sidebar.selectbox("Selecione a opção desejada 👇: ",
                    ["Horários de monitoria", 
                     "Marcar presença",
                     "Dicas",
                     "Software low-code",
                     "Meus códigos",
                     "Contato" 
                    ])                                
if task1 == "Horários de monitoria": 
    #st.set_page_config(page_title="Horários", page_icon=":alarm_clock:")

    st.markdown( 
     """
        DIA | HORÁRIO | LOCAL
    :---------: | :------: | :-------:
    Quarta - feira | 14h00 às 17h00 | Lab 06 (4º Andar)
    Sexta - feira | 14h00 às 17h00 | Lab 06 (4º Andar)    
    """
    )
if task1 == "Marcar presença":
    
   st.markdown (""" 
    ### *Quando você participar da monitoria:* ### 
    Preencha por favor: [link](https://forms.gle/R1PQwwXVqQTHXCmTA).""")

if task1 == "Dicas": 
    
    SUB_TITULO1_1 = '<p style="font-family:tahoma; color:Green; font-size: 26px;"> Dica 01 - Pratique </p>'
    st.markdown(SUB_TITULO1_1, unsafe_allow_html=True)

    cols02 = st.columns(1)
    cols02[0].write(' Por experiência própria: a prática provoca melhorias gritantes. As aulas passam muito rápido e com os colegas em turma, a distração é inevitável. A primeira dica que eu tenho então é: tente praticar pelo menos uma vez por semana, além das aulas de laboratório,  e você verá que o conteúdo fica um pouco menos complicado. ')

    SUB_TITULO1_2 = '<p style="font-family:tahoma; color:Green; font-size: 26px;"> Dica 02 - Entenda o código </p>'
    st.markdown(SUB_TITULO1_2, unsafe_allow_html=True)
    
    cols03 = st.columns(1)
    cols03[0].write('As vezes o programa está muito difícil e o código não está "saindo", então podemos copiar de algum colega, ou da internet. Não tem problema copiar de alguém, mas tente entender o porquê e como o programa funciona. Isso nos leva a próxima dica: ')
    
    SUB_TITULO1_3 = '<p style="font-family:tahoma; color:Green; font-size: 26px;">  Dica 03 - Não tenha medo </p>'
    st.markdown(SUB_TITULO1_3, unsafe_allow_html=True)

    cols04 = st.columns(1)
    cols04[0].write('No início, a programação parece um bicho com 7 cabeças, muitas letras e símblos, que parecem não fazer sentido, mas quando você começa a praticar e a entender o que cada linha faz, fica muito mais fácil. O Massaki sempre me falava: "O computador não vai explodir se você errar o código", e realmente, isso não aconteceu nas inumeras vezes que eu errei. Então, pegue um programa na internet, e treine com ele, apagando ou adicionando mais linhas, assim você se familiariza com as bibliotecas e funções. ')

if task1 == "Software low-code":
   SUB_TITULO1_1 = '<p style="font-family:tahoma; color:Green; font-size: 20px;">Meu contato com o low-code: </p>'  
    
if task1 == "Meus códigos":
    st.markdown ("""
    Tenho conta em alguns compliladores, você pode entrar lá e se inspirar nos códigos disponíveis:
    - Replit: [link](https://replit.com/@IsabelaFerreir8).
    - GitHub: [link](https://github.com/Isafp).
    - OnlineGDB: [link](https://www.onlinegdb.com/myfiles).                                           
                                            """)
   
    

if task1 == "Contato": 
    
    SUB_TITULO1_1 = '<p style="font-family:tahoma; color:Green; font-size: 20px;">Canais para tirar as dúvidas: </p>'
    st.markdown(SUB_TITULO1_1, unsafe_allow_html=True)
    cols05 = st.info(
            """
            O método que eu considero mais efetivo é de forma presencial, no laboratório, mas também será possível enviar suas dúvidas via: 
             - Grupo Teams: [link](https://teams.microsoft.com/l/channel/19%3a7xkQWvR0fCtUeibcBpxp0qY9Oukrf74CspgaJ2RAuHs1%40thread.tacv2/Geral?groupId=bce15ed0-5eb4-4b99-ba83-4575cc95481a&tenantId=51da9440-4e5e-47b3-8e5c-4817f6f43c04) .
             - E-mail: isafparanaiba@gmail.com .
            """
            )
    SUB_TITULO1_2 = '<p style="font-family:tahoma; color:Red; font-size: 20px;"> Atenção!: </p>'
    st.markdown(SUB_TITULO1_2, unsafe_allow_html=True)
    
    cols05 = st.columns(1)
    cols05[0].write('📌 Só irei responder durante o horário da monitoria, então tenha paciência que responderei o quanto antes. ')
