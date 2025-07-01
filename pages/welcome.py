import streamlit as st

def welcome_page():
    st.markdown("""
        <div style='display: flex; flex-direction: column; justify-content: center; align-items: center; height: 80vh; padding: 2rem;'>
            <div class="title-custom">NEXT GEN<br>DRAFT</div>
            <div class="subtitle-effect">
                Where talent meets destiny and every pick could shape the future of the game
            </div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Start"):
        st.session_state.page = "menu"
        st.rerun()
