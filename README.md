import streamlit as st
import pandas as pd

st.set_page_config(page_title="Futebol Virtual", layout="centered", page_icon="⚽")

st.title("⚽ Análise de Futebol Virtual")
st.markdown("Bem-vindo! Aqui você pode filtrar partidas por critérios como Over 2.5, viradas e placares exatos.")

# Upload de arquivo CSV com dados simulados
uploaded_file = st.file_uploader("Envie um arquivo .csv com os resultados", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Exibir dados
    st.subheader("📊 Dados carregados")
    st.dataframe(df)

    # Filtro: Over 2.5 gols
    st.subheader("🔎 Filtro: Over 2.5 gols")
    over_25 = df[df['total_gols'] > 2.5]
    st.write(f"Partidas com mais de 2.5 gols: {len(over_25)}")
    st.dataframe(over_25)

    # Filtro: Viradas (perdeu o 1º tempo, venceu o jogo)
    st.subheader("🔄 Filtro: Viradas")
    viradas = df[(df['1T_time_casa'] < df['1T_time_fora']) & (df['FT_time_casa'] > df['FT_time_fora'])]
    st.write(f"Viradas encontradas: {len(viradas)}")
    st.dataframe(viradas)

else:
    st.info("Envie um arquivo CSV com dados de partidas para começar.")
