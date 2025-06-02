app.py import streamlit as st

# Configurar o tema escuro
st.set_page_config(page_title="Futebol Virtual", page_icon="⚽", layout="centered")

# Estilo CSS para modo escuro básico
dark_style = """
<style>
    body {
        background-color: #121212;
        color: #eeeeee;
    }
    .stButton>button {
        background-color: #1e88e5;
        color: white;
    }
    .stTextInput>div>input {
        background-color: #333333;
        color: white;
    }
</style>
"""
st.markdown(dark_style, unsafe_allow_html=True)

st.title("Futebol Virtual - Análise Over 2.5")

# Exemplo simples de filtro
st.sidebar.header("Filtros")
time_selecionado = st.sidebar.selectbox("Selecione o time:", ["Todos", "Time A", "Time B", "Time C"])
over_2_5 = st.sidebar.checkbox("Mostrar só jogos Over 2.5", value=True)

st.write(f"Time selecionado: {time_selecionado}")
st.write(f"Filtro Over 2.5 ativado? {'Sim' if over_2_5 else 'Não'}")

# Aqui você colocaria a lógica para coletar e mostrar os dados reais

st.write("Aqui aparecerão os dados e análises do futebol virtual.")

