import streamlit as st
import pandas as pd

# Load the dataframe
df = pd.read_excel("ANTROPOMETRICI OFFICIAL.xlsx")

def section1():
    st.title("🧑‍💼 Player Profiling")
    
    # Filtro iniziali del giocatore
    player_input = st.text_input("Search by player initials", "")
    
    # Filtro dei giocatori che corrispondono alle iniziali
    filtered_players = df[df['PLAYER'].str.contains(player_input, case=False, na=False)]
    
    if filtered_players.empty:
        st.write("No players found.")
    else:
        # Se ci sono giocatori filtrati, li mostriamo in una selectbox
        player_name = st.selectbox("Select Player", filtered_players['PLAYER'].unique())
        
        # Filtriamo i dati per il giocatore selezionato
        player_data = filtered_players[filtered_players['PLAYER'] == player_name]
        
        # Visualizziamo i dati per quel giocatore
        st.dataframe(player_data)

        # Visualizzazione completa dei dati numerici
        numeric_columns = player_data.select_dtypes(include=['float64', 'int64']).columns

        if not numeric_columns.empty:
            # Grafico a barre con tutte le colonne numeriche per il giocatore
            st.bar_chart(player_data[numeric_columns].iloc[0])
        else:
            st.write("No numeric data available for chart.")
