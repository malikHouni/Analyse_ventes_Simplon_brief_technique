
import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

# Connexion à la base
DB_PATH = "../etape3/data/ventes.db"

@st.cache_data
def load_data():
    conn = sqlite3.connect(DB_PATH)
    ventes = pd.read_sql_query("""
        SELECT v.date, p.nom AS produit, v.quantite, p.prix, m.ville
        FROM ventes v
        JOIN produits p ON v.id_ref = p.id_ref
        JOIN magasins m ON v.id_magasin = m.id_magasin
    """, conn)
    conn.close()
    return ventes

st.set_page_config(page_title="Analyse des ventes PME", layout="centered")

st.title("📊 Analyse des ventes - PME _ Par Malik HOUNI")
st.markdown("Mini app d’analyse des ventes pour le brief technique de Simplon. Les données ont été extraites depuis la base SQLite intégrée dans l’environnement Docker.")

data = load_data()

st.header("1. Chiffre d'affaires total")
data["chiffre_affaires"] = data["quantite"] * data["prix"]
st.metric(label="Total", value=f"{data['chiffre_affaires'].sum():,.2f} €")

st.header("2. Ventes par produit")
ca_par_produit = data.groupby("produit").agg(
    quantite_totale=("quantite", "sum"),
    chiffre_affaires=("chiffre_affaires", "sum")
).reset_index()

st.dataframe(ca_par_produit)

fig1 = px.bar(ca_par_produit, x="produit", y="chiffre_affaires",
              title="Chiffre d'affaires par produit", labels={"chiffre_affaires": "CA (€)"})
st.plotly_chart(fig1)

st.header("3. Ventes par ville")
ca_par_ville = data.groupby("ville").agg(
    chiffre_affaires=("chiffre_affaires", "sum")
).reset_index()

fig2 = px.bar(ca_par_ville, x="ville", y="chiffre_affaires",
              title="Chiffre d'affaires par ville", labels={"chiffre_affaires": "CA (€)"})
st.plotly_chart(fig2)

st.header("📥 Données brutes")
if st.checkbox("Afficher les données complètes"):
    st.dataframe(data)
