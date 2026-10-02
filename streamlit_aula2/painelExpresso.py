import streamlit as st
 
st.title("🚌 Expresso Mobilidade")
st.header("Painel do Operador")
 
nome = st.text_input("Digite seu nome:")
if nome:
    st.write("Olá,", nome, "👋 Bom turno!")
 
st.subheader("Consultar uma linha")
linha = st.selectbox("Escolha uma linha:", ["510", "520", "550"])
st.write("Linha selecionada:", linha)
 
horarios = {
    "510": "06:00 | 06:30 | 07:00",
    "520": "06:15 | 06:45 | 07:15",
    "550": "06:10 | 06:40 | 07:10",
}
st.write("Próximos horários:", horarios[linha])
 
st.subheader("Relatório de passageiros")
linhas = st.multiselect("Escolha as linhas:", ["510", "520", "550", "620"])
st.write(linhas)
 
if st.button("Calcular"):
    st.write("Calculando...")
    if len(linhas) == 0:
        st.write("Escolha pelo menos uma linha!")
    else:
        total = len(linhas) * 3
        st.write("Linhas calculadas:", len(linhas))
        st.write("Ônibus necessários:", total, "🚌")
        st.write("Pronto! ✅")
 