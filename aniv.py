import datetime
import streamlit as st

st.title('Aniversário do meu Nerdzila')
st.markdown(" #Seráquetrintou?")



hoje = datetime.date.today().strftime('%d-%m-%Y')
#dia = hoje.split('-')
st.write(hoje)
st.write(hoje.day,hoje.month,hoje.year)
nasci = st.date_input("Data do seu nascimento: ", min_value = datetime.date(1990, 1, 1))
nome = st.text_input ("Como as pessoas te chamam: ")
st.write(nasci)
st.write(nasci.day,nasci.month,nasci.year)
#nasci = nasci.split("/")
btn = st.button('Calcular o aniversário')
if btn:
    if dia.day == nasci.day and dia.month == nasci.month:
        idade = int(dia.year) - int(nasci.year)
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
