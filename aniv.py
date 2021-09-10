import datetime
import streamlit as st

st.title('Aniversário do meu Nerdzila')
st.markdown(" #Seráquetrintou?")



hoje = datetime.date.today()
#dia = hoje.split('-')
st.write(hoje)

nasci = st.date_input("Data do seu nascimento: ",datetime.date(1991, 9, 10))
nome = st.text_input ("Como as pessoas te chamam: ")
st.write(nasci)

#nasci = nasci.split("/")
btn = st.button('Calcular o aniversário')
if btn:
    if hoje.day == nasci.day and hoje.month == nasci.month:
        idade = int(hoje.year) - int(nasci.year)
        if idade == 30:
            if nome.split(' ')[0] =='Igor' or nome.split(' ')[0] == 'Girão' or nome == 'Igor Girão':
                st.write(f'Hoje é seu aniversário.\nTrintou.\n{nome},tá fazendo {idade} anos')
                #print(f'Hoje é seu aniversário.\nTrintou.\n{nome},tá fazendo {idade} anos')
            else:
                st.write('Hoje é até seu aniversário mas não é meu nerdzila.')
                #print('Hoje é até seu aniversário mas não é meu nerdzila.')
        else:
            st.write('Hoje é até seu aniversário porém não está fazendo trinta anos e nem é meu nerdzila')
            #print('Hoje é até seu aniversário porém não está fazendo trinta anos e nem é meu nerdzila')
    else:
        st.write(f"{nome}, hoje não é seu aniversário,querido(a).")
        print("Hoje não é seu aniversário,querido(a).")
