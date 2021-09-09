import datetime
import streamlit as st

st.title('Aniversário do meu Nerdzila')
st.markdown(" #Seráquetrintou?")



hoje = datetime.date.today().strftime('%d-%m-%Y') 
dia = hoje.split('-')

nasci = st.date_input("Data do seu nascimento(dd-mm-aaaa): ")
nome = st.text_input ("Como as pessoas te chamam: ")
nasci = nasci.split("-")
if dia[0] == nasci[0] and dia[1] == nasci[1]:
    idade = int(dia[2]) - int(nasci[2])
    if idade == 30:
        if nome.split(' ')[0] =='Igor' or nome.split(' ')[0] == 'Girão' or nome == 'Igor Girão':
            print(f'Hoje é seu aniversário.\nTrintou.\n{nome},tá fazendo {idade} anos')
        else:
            print('Hoje é até seu aniversário mas não é meu nerdzila.')
    else:
        print('Hoje é até seu aniversário porém não está fazendo trinta anos e nem é meu nerdzila')
else:
    print("Hoje não é seu aniversário,querido(a).")
