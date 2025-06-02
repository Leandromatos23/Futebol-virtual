import streamlit as st

st.set_page_config(page_title="Futebol Virtual", layout="centered")

st.title("Análise de Futebol Virtual")

st.markdown("Escolha o número mínimo de gols para filtrar jogos:")

# Slider interativo
over_goals = st.slider("Gols mínimos (over)", 0, 10, 2)

# Dados simulados
jogos = [
    {"time1": "Time A", "time2": "Time B", "gols": 3},
    {"time1": "Time C", "time2": "Time D", "gols": 1},
    {"time1": "Time E", "time2": "Time F", "gols": 5},
    {"time1": "Time G", "time2": "Time H", "gols": 2},
]

# Filtro
jogos_filtrados = [j for j in jogos if j["gols"] > over_goals]

st.subheader("Jogos filtrados:")

if jogos_filtrados:
    for jogo in jogos_filtrados:
        st.write(f"**{jogo['time1']} x {jogo['time2']}** – Gols: {jogo['gols']}")
else:
    st.write("Nenhum jogo com essa quantidade de gols.")
