import streamlit as st

# Simulação de dados simplificada (exemplo)
jogos = [
    {"time1": "Time A", "time2": "Time B", "placar_ht": (0, 1), "placar_ft": (2, 1)},
    {"time1": "Time C", "time2": "Time D", "placar_ht": (1, 0), "placar_ft": (3, 2)},
    {"time1": "Time E", "time2": "Time F", "placar_ht": (0, 2), "placar_ft": (0, 3)},
    {"time1": "Time G", "time2": "Time H", "placar_ht": (0, 1), "placar_ft": (4, 2)},
]

def viradinha(jogo):
    ht1, ht2 = jogo["placar_ht"]
    ft1, ft2 = jogo["placar_ft"]
    return (ht1 < ht2) and (ft1 > ft2)

st.title("Análise de Futebol Virtual - Versão Parcial")

# Filtros
st.sidebar.header("Filtros")

filtro_over_25 = st.sidebar.checkbox("Mostrar jogos Over 2.5", value=True)
filtro_over_35 = st.sidebar.checkbox("Mostrar jogos Over 3.5", value=False)
filtro_viradinha = st.sidebar.checkbox("Mostrar viradinhas (time que perdeu 1º tempo e virou)", value=True)

def gols_totais(jogo):
    ft1, ft2 = jogo["placar_ft"]
    return ft1 + ft2

# Filtrar jogos
jogos_filtrados = []
for jogo in jogos:
    gols = gols_totais(jogo)
    cond_over_25 = gols > 2.5 if filtro_over_25 else True
    cond_over_35 = gols > 3.5 if filtro_over_35 else True
    cond_viradinha = viradinha(jogo) if filtro_viradinha else True

    if cond_over_25 and cond_over_35 and cond_viradinha:
        jogos_filtrados.append(jogo)

# Mostrar resultados
st.subheader(f"Jogos filtrados ({len(jogos_filtrados)})")

for jogo in jogos_filtrados:
    st.write(f"{jogo['time1']} {jogo['placar_ht'][0]}x{jogo['placar_ht'][1]} {jogo['time2']} (1º Tempo)")
    st.write(f"{jogo['time1']} {jogo['placar_ft'][0]}x{jogo['placar_ft'][1]} {jogo['time2']} (Resultado Final)")
    st.write("---")
