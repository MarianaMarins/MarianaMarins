import datetime
import streamlit as st

st.title('Aniversário do meu Nerdzila')
st.header(" #Seráquetrintou?")



hoje = datetime.date.today()
#dia = hoje.split('-')


nasci = st.date_input("Data do seu nascimento: ",min_value = datetime.date(1991, 1, 1))
nome = st.text_input ("Como as pessoas te chamam: ")


#nasci = nasci.split("/")
btn = st.button('Calcular o aniversário')
if btn:
    if hoje.day == nasci.day and hoje.month == nasci.month:
        idade = int(hoje.year) - int(nasci.year)
        if idade == 30:
            if nome.split(' ')[0] =='Igor' or nome.split(' ')[0] == 'Girão' or nome == 'Igor Girão' or nome.split(' ')[0] == 'Girao' or nome.split(' ')[0] == 'igor':
                st.write(f'Meu nerdzila lindo.')
                st.write(f'FELIZ ANIVERSÁRIO.')
                st.write(f'Torço por você e pelas suas conquistas. Tudo de bom hoje e sempre.')
                st.write('Trintou.')
                st.write(f'{nome},tá fazendo {idade} anos')
                st.write('TE AMO <3')
                st.sidebar.markdown("![Alt Text](https://i.picasion.com/pic91/b90637250ed68cf7a91ca586ccbb9dce.gif)")
                #st.markdown("![Alt Text](https://i.picasion.com/pic91/b90637250ed68cf7a91ca586ccbb9dce.gif)")
                #print(f'Hoje é seu aniversário.\nTrintou.\n{nome},tá fazendo {idade} anos')
            else:
                st.write('Hoje é até seu aniversário mas não é meu nerdzila.')
                #print('Hoje é até seu aniversário mas não é meu nerdzila.')
        else:
            st.write('Hoje é até seu aniversário porém não está fazendo trinta anos e nem é meu nerdzila')
            #print('Hoje é até seu aniversário porém não está fazendo trinta anos e nem é meu nerdzila')
    else:
        st.write(f"{nome}, hoje não é seu aniversário,querido(a).")
        st.sidebar.markdown("![Alt Text]("https://giphy.com/embed/xROSM4Ifcrq79f7REf")
        print("Hoje não é seu aniversário,querido(a).")
