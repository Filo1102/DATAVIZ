import streamlit as st

def main_menu():
    st.title("📋 Main Menu")
    st.write("Choose a section below:")

    # Creiamo due colonne che occupano tutta la larghezza disponibile
    col1, col2 = st.columns([1, 1])  # Entrambe le colonne occupano metà della larghezza

    # Colonna per i pulsanti
    with col1:
        # Pulsanti per la selezione della sezione
        if st.button("🧑‍💼 Player Profiling"):
            st.session_state.page = "section1"
            st.rerun()

        if st.button("📚 History & Trend"):
            st.session_state.page = "section2"
            st.rerun()

        if st.button("🔬 Research"):
            st.session_state.page = "section3"
            st.rerun()

        if st.button("🏆 Player Career"):
            st.session_state.page = "section4"
            st.rerun()

    # Colonna per l'immagine
    with col2:
        # Inserisci l'immagine con una larghezza che occupi tutta la colonna
        st.image("/workspaces/DATAVIZ/images/DRAFT2.jpg", use_container_width=True)  # Usa tutta la larghezza della colonna

    # Ridurre lo spazio tra i due contenuti con il CSS (se necessario)
    st.markdown("""
        <style>
            .stColumn {
                padding-top: 0px;
                padding-bottom: 0px;
            }
        </style>
    """, unsafe_allow_html=True)
