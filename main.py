import streamlit as st
from pages.welcome import welcome_page
from pages.menu import main_menu
from pages.player_profiling import section1
from pages.history_and_trend import section2
from pages.research import section3
from pages.player_career import section4

# Page setup: Rimuove il menu laterale predefinito di Streamlit
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# Aggiungi uno script JavaScript per nascondere completamente la sidebar
hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .css-1d391kg {display: none;}  /* Rimuove l'icona del menu laterale */
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Set initial state
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

# Page map and reverse
page_labels = {
    "welcome": "🏠 Welcome",
    "menu": "📋 Main Menu",
    "section1": "🧑‍💼 Player Profiling",
    "section2": "📚 History & Trend",
    "section3": "🔬 Research",
    "section4": "🏆 Player Career"
}
page_reverse_map = {v: k for k, v in page_labels.items()}

# Sidebar navigation: Menu personalizzato
with st.sidebar:
    st.title("Navigation")
    selected_label = st.selectbox(
        "Go to:", list(page_labels.values()),
        index=list(page_labels.keys()).index(st.session_state.page)
    )
    selected_page = page_reverse_map[selected_label]
    if selected_page != st.session_state.page:
        st.session_state.page = selected_page
        st.rerun()

# Global style for custom look and feel
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@800&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary-color: #f45208;
            --secondary-color: #2f6974;
            --text-color: white;
        }
        .title-custom {
            font-family: 'Orbitron', sans-serif;
            font-weight: 800;
            font-size: 5rem;
            color: var(--primary-color);
            -webkit-text-stroke: 3px var(--text-color);
            text-shadow: 5px 5px 10px rgba(0,0,0,0.3);
            text-align: center;
            margin-bottom: 2rem;
        }
        .subtitle-effect {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.8rem;
            color: white;
            text-align: center;
            animation: fadeIn 2s ease-in-out;
            transition: transform 0.3s ease;
            margin-bottom: 3rem;
        }
        .subtitle-effect:hover {
            transform: scale(1.08);
            color: #f45208;
            text-shadow: 0 0 10px rgba(244,82,8,0.7);
        }
        .back-arrow {
            position: absolute;
            top: 20px;
            right: 30px;
            font-size: 18px;
            color: white;
            font-weight: bold;
            text-decoration: none;
            background-color: transparent;
            border: 2px solid white;
            padding: 6px 12px;
            border-radius: 8px;
            transition: all 0.3s ease;
        }
        .back-arrow:hover {
            background-color: white;
            color: #2f6974;
            text-decoration: none;
        }
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(10px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        .stApp {
            background-color: #2f6974;
        }
    </style>
""", unsafe_allow_html=True)

# Router: Carica la sezione giusta in base alla pagina selezionata
pages = {
    "welcome": welcome_page,
    "menu": main_menu,
    "section1": section1,
    "section2": section2,
    "section3": section3,
    "section4": section4
}

# Esegui la funzione della pagina attualmente selezionata
pages[st.session_state.page]()
