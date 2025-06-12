import streamlit as st
import pandas as pd

st.set_page_config(page_title="Calcolatore Costi Installazione", layout="centered")

st.title("💻 Calcolatore Costi Installazione Software")

st.markdown("""
Seleziona i parametri per visualizzare la matrice dei costi totali di installazione.  
La cella corrispondente alla tua selezione verrà evidenziata.
""")

# Costi base
base_costs = {
    "Analisi pre-installazione": 300,
    "Setup prerequisiti": 350,
    "Deploy applicativo": 300,
    "Testing e validazione": 300
}

# Sovrapprezzi
machine_costs = {"Remota (Docker)": 100, "Locale": 200}
db_costs = {
    "Già noto": 0,
    "Liv. 3 (strutturato)": 100,
    "Liv. 2 (mediamente ok)": 200,
    "Liv. 1 (caotico)": 300
}
table_count_costs = {"1-10": 100, "11-50": 300, "51+": 1000}
column_avg_costs = {"1-10": 0, "11-50": 250, "51+": 1000}

# Genera tutte le matrici con costi totali
def genera_matrici():
    matrici = {}
    for macchina in machine_costs:
        for colonne in column_avg_costs:
            dati = []
            for db in db_costs:
                riga = []
                for tabelle in table_count_costs:
                    extra = (
                        machine_costs[macchina]
                        + db_costs[db]
                        + table_count_costs[tabelle]
                        + column_avg_costs[colonne]
                    )
                    totale_fase = sum(base_costs.values()) + extra * len(base_costs)
                    riga.append(totale_fase)
                dati.append(riga)
            df = pd.DataFrame(
                dati,
                index=list(db_costs.keys()),
                columns=list(table_count_costs.keys())
            )
            chiave = f"{macchina}_{colonne}"
            matrici[chiave] = df
    return matrici

# Generazione matrici
matrici_costi = genera_matrici()

# Selezione dell'utente (tutte e 4 le dimensioni)
macchina_sel = st.selectbox("📦 Tipo di macchina:", list(machine_costs.keys()))
db_sel = st.selectbox("🧠 Struttura database:", list(db_costs.keys()))
tabelle_sel = st.selectbox("📊 Numero di tabelle:", list(table_count_costs.keys()))
colonne_sel = st.selectbox("📐 Numero medio di colonne per tabella:", list(column_avg_costs.keys()))

# Seleziona la matrice corrispondente
chiave_matrice = f"{macchina_sel}_{colonne_sel}"
matrice = matrici_costi[chiave_matrice]

def highlight_pos(df):
    # crea una DataFrame di stringhe vuote, stessa forma di df
    mask = pd.DataFrame("", index=df.index, columns=df.columns)
    # evidenzia UNICAMENTE la cella selezionata
    mask.loc[db_sel, tabelle_sel] = "background-color: yellow; font-weight: bold"
    return mask

styled_matrice = matrice.style.apply(highlight_pos, axis=None)


st.markdown("---")
st.subheader(f"📊 Matrice costi per: **{macchina_sel} + {colonne_sel} colonne**")
st.dataframe(styled_matrice.format("€{:,.0f}"))

st.markdown(f"""
📍 Hai selezionato:  
- **Struttura DB**: {db_sel}  
- **Numero Tabelle**: {tabelle_sel}  
- 💰 **Costo Totale**: **€{matrice.loc[db_sel, tabelle_sel]:,.0f}**

🧠 **Righe** = Struttura DB  
📈 **Colonne** = Numero tabelle  
📦 **Celle** = Costo totale installazione
""")
