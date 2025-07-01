import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.ticker import MaxNLocator

def section2():
    st.title("📚 History & Trend")
    st.write("Explore historical draft trends e vedi tutti i pick con un layout ad alto contrasto.")

    try:
        df = pd.read_csv("/workspaces/DATAVIZ/draft_history_fin.csv")
        years = df["Year"].unique().astype(int)
        year = st.selectbox("Select a year", sorted(years))
        filtered = (
            df[df["Year"] == year]
            .drop(columns=["Unnamed: 0", "Round.1"], errors="ignore")
            .sort_values("Overall Pick")
        )

        # … qui vanno la tabella e il bar chart come prima …

        st.subheader(f"All {year} Draft Picks")
        logo_folder = Path("/workspaces/DATAVIZ/images/logos")

        def find_logo(abbrev):
            for ext in [".png", ".jpg", ".jpeg"]:
                p = logo_folder / f"{abbrev}{ext}"
                if p.exists():
                    return p
            return None

        for _, r in filtered.iterrows():
            col1, col2, col3 = st.columns([1, 4, 2])

            # 1) Numero di pick (box nero opzionale)
            col1.markdown(f"""
                <div style="
                    background-color: #222;
                    padding: 10px;
                    border-radius: 8px;
                    text-align: center;
                ">
                  <span style="font-size:24px; color:#fff; font-weight:bold;">
                    {r['Overall Pick']}
                  </span>
                </div>
            """, unsafe_allow_html=True)

            # 2) Nome e round senza sfondo, testo chiaro per contrasto
            col2.markdown(f"""
                <div style="padding: 8px 12px;">
                  <div style="font-size:18px; font-weight:bold; color:#fafafa;">
                    {r['Player']}
                  </div>
                  <div style="font-size:14px; color:#e0e0e0;">
                    {int(r['Round Number'])}° Round, Pick {int(r['Round Pick'])}
                  </div>
                </div>
            """, unsafe_allow_html=True)

            # 3) Logo centrato, senza sfondo
            logo_path = find_logo(r["Team Abbreviation"])
            if logo_path:
                col3.markdown('<div style="text-align:center;">', unsafe_allow_html=True)
                col3.image(str(logo_path), width=80)
                col3.markdown('</div>', unsafe_allow_html=True)
            else:
                # fallback sigla
                col3.markdown(f"""
                    <div style="
                        text-align: center;
                        font-size:16px;
                        color:#fafafa;
                        padding-top:12px;
                    ">
                      {r['Team Abbreviation']}
                    </div>
                """, unsafe_allow_html=True)

            st.markdown("""<hr style="border-color:#2b6b6f; margin:12px 0;">""",
                        unsafe_allow_html=True)

    except Exception as e:
        st.error(f"An error occurred: {e}")
