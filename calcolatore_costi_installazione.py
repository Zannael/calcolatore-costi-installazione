import streamlit as st

st.set_page_config(page_title="Calcolatore Costi Installazione", layout="centered")

st.title("💻 Calcolatore Costi Installazione Software")

st.markdown("""
Seleziona il tipo di **macchina**, la **struttura del database**, 
il **numero di tabelle** e la **media di colonne per tabella** 
per calcolare i costi di installazione per ciascuna fase del processo.
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

# Sovrapprezzi per numero di tabelle
table_count_costs = {
    "1-10": 100,
    "11-50": 300,
    "51+": 1000
}

# Sovrapprezzi per numero medio di colonne per tabella
column_avg_costs = {
    "1-10": 0,
    "11-50": 250,
    "51+": 1000
}

# Selezione interattiva
machine_choice = st.selectbox("📦 Tipo di macchina:", list(machine_costs.keys()))
db_choice = st.selectbox("🧠 Struttura database:", list(db_costs.keys()))
table_count_choice = st.selectbox("📊 Numero di tabelle nel database:", list(table_count_costs.keys()))
column_avg_choice = st.selectbox("📐 Numero medio di colonne per tabella:", list(column_avg_costs.keys()))

st.markdown("---")

# Calcolo e visualizzazione
total_general = 0
extra_machine = machine_costs[machine_choice]
extra_db = db_costs[db_choice]
extra_tables = table_count_costs[table_count_choice]
extra_columns = column_avg_costs[column_avg_choice]

for phase, base in base_costs.items():
    total = base + extra_machine + extra_db + extra_tables + extra_columns
    total_general += total
    st.write(
        f"**{phase}**: €{base} + €{extra_machine} (macchina) + €{extra_db} (DB) + "
        f"€{extra_tables} (tabelle) + €{extra_columns} (colonne) = **€{total}**"
    )

st.markdown("---")
st.subheader(f"💰 Totale complessivo: **€{total_general}**")
