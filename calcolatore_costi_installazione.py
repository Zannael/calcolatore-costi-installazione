
import streamlit as st

st.set_page_config(page_title="Calcolatore Costi Installazione", layout="centered")

st.title("💻 Calcolatore Costi Installazione Software")

st.markdown("""
Seleziona il tipo di **macchina** e la **struttura del database** per calcolare i costi di installazione 
per ciascuna fase del processo.
""")

# Costi base
base_costs = {
    "Analisi pre-installazione": 300,
    "Setup prerequisiti": 350,
    "Deploy applicativo": 300,
    "Testing e validazione": 300
}

# Sovrapprezzi
machine_costs = {
    "Remota (Docker)": 100,
    "Locale": 200
}

db_costs = {
    "Già noto": 0,
    "Liv. 3 (strutturato)": 100,
    "Liv. 2 (mediamente ok)": 200,
    "Liv. 1 (caotico)": 300
}

# Selezione interattiva
machine_choice = st.selectbox("📦 Tipo di macchina:", list(machine_costs.keys()))
db_choice = st.selectbox("🧠 Struttura database:", list(db_costs.keys()))

st.markdown("---")

# Calcolo e visualizzazione
total_general = 0
for phase, base in base_costs.items():
    extra_machine = machine_costs[machine_choice]
    extra_db = db_costs[db_choice]
    total = base + extra_machine + extra_db
    total_general += total
    st.write(f"**{phase}**: €{base} + €{extra_machine} (macchina) + €{extra_db} (DB) = **€{total}**")

st.markdown("---")
st.subheader(f"💰 Totale complessivo: **€{total_general}**")
