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

r = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vTjhdfDYTI3HNP0wpxBAp_YePhfyBj9GlLAmFgW2zUsTQiWJwkY_iUvVuhiT9AD2X81uJQalB89rYlw/pub?gid=2112212887&single=true&output=csv')
DB = r.content
df = pd.read_csv(BytesIO(DB), index_col=0)
df.columns = ['Curso', 'Nome', 'CPF', 'Endereco', 'Telefone', 'e-mail']
curso = df['Curso']
nome = df['Nome']
#mail = df['email'][[0]
#st.write(df)
#st.write(df['email'])

image = Image.open('sun.png')
image1 = Image.open('BibliografiaBASICA.jpg')
image2 = Image.open('BibliografiaComplementar1.jpg')
st.image(image, caption='Web site em desenvolvimento')
st.markdown(":computer:")	
st.title("AMBIENTE DE MONITORIA")
SUB_TITULO = '<p style="font-family:tahoma; color:Green; font-size: 20px;">Desenvolvido pela aluna Isabela Ferreira Paranaíba</p>'
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
#### ***Para desenvolver esse mateiral eu usei a programação do site em desenvlvimento do professor Massaki Igarashi.*** """)
st.warning("Site: [link](https://massakiigarashi2-streamlitwebapp-website-5g8yl6.streamlitapp.com/).")
    
task1 = st.selectbox("Selecione a opção desejada 👇: ",
                    ["Horários de monitoria", 
                     "Dicas",                                
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


if task1 == "Dicas": 
    
    SUB_TITULO1_1 = '<p style="font-family:tahoma; color:Green; font-size: 26px;"> 01 - ... </p>'
    st.markdown(SUB_TITULO1_1, unsafe_allow_html=True)

    cols02 = st.columns(1)
    cols02[0].write(' ')

    SUB_TITULO1_2 = '<p style="font-family:tahoma; color:Green; font-size: 26px;"> 02 - ... </p>'
    st.markdown(SUB_TITULO1_2, unsafe_allow_html=True)
    
    cols03 = st.columns(1)
    cols03[0].write(' ')
    
    SUB_TITULO1_3 = '<p style="font-family:tahoma; color:Green; font-size: 26px;"> 03 - ... </p>'
    st.markdown(SUB_TITULO1_3, unsafe_allow_html=True)

    cols04 = st.columns(1)
    cols04[0].write(' ')
    
if task1 == "Contato": 
    
    SUB_TITULO1_1 = '<p style="font-family:tahoma; color:Grenn; font-size: 20px;">Canais para contato: </p>'
    st.markdown(SUB_TITULO1_1, unsafe_allow_html=True)
    cols05 = st.columns(1)
    cols05[0].write(' Temos um grupo no Teams onde as dúvidas podem ser enviadas a qualquer hora do dia: [link](https://emojipedia.org/backhand-index-pointing-down/  (link improvisado).')
