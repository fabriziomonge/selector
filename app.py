#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import altair as alt
import streamlit as st

from PIL import Image

try:
    image = Image.open('logo.png')
except:
    image = Image.open(r'C:\Users\user\Downloads\App_sim\logo.png')

st.sidebar.image(image, use_column_width=True)

st.sidebar.markdown('''### Seleziona i parametri del tuo grafico ''')



try:

    tabella = tabella
    
except:
    
    tabella = pd.read_excel('http://www.sphereresearch.net/Sim/tabella_completa.xlsx')
    
    
tabella = tabella.set_index('Unnamed: 0',1)

# Qua inserisci il filtro

st.title('Selettore Fondi Quantitativo')

asset_sel = ['ALL']+list(tabella['Asset Class'].unique())

Filtro = st.multiselect('Asset selezionata', asset_sel, default=['ALL'])
# valore= 'Breve Medio Periodo'

Filtro = list(Filtro)


tabella_show = pd.DataFrame(columns=tabella.columns)
if Filtro == ['ALL']:
    tabella_show = tabella_show.append(tabella)
else:
    
    for i in Filtro:
        tabella1 = tabella.loc[tabella['Asset Class'] == i]
        tabella_show = tabella_show.append(tabella1)




# display(tabella.columns)

#Qua inserisci i selettori

indice = ['Rendimento% a 3 mesi','Rendimento% a 6 mesi', 'Rendimento% a 12 mesi', 'Rendimento% a 3 anni', 'Rendimento% a 5 anni', 'Volatilità% a 6 mesi', 'Volatilità% a 12 mesi', 'Volatilità% a 3 anni', 'Volatilità% a 5 anni','Max Drawdown']
indice2 = ['Asset Class', 'Categoria', 'Rischio', 'Orizzonte', 'Classificazione', 'Listino']

assex = st.sidebar.selectbox('scegli asse x',indice, index=5)

assey = st.sidebar.selectbox('scegli asse y',indice, index=1)

marker = st.sidebar.selectbox('scegli marker',indice2)

# assex = 'DD'
# assey = 'roc6'
# marker = 'Orizzonte'


dim = st.slider('Dimensione Bolle',min_value=1, max_value=5, value=1)
dim=dim*100
fig1 = alt.Chart(tabella_show).mark_circle(size=dim).encode(x=assex, y=assey, color=marker,tooltip=['Asset Class', 'Categoria','Società di Gestione', 'Nome prodotto', 'ISIN', 'analisi dal:']).properties(height=500, width=700).interactive()


fig1


# In[1]:


tabella_show


# In[ ]:




