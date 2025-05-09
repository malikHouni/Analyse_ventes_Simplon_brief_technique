# Analyse_ventes_Simplon_brief_technique
Projet d'analyse de ventes pour le brief technique de Simplon.co

![image](https://github.com/user-attachments/assets/48622d08-e2e3-42cb-9eab-3fba32ddf04e)



Ce projet consiste à construire un environnement complet d’analyse de données pour une PME, à l’aide de Docker, Python, SQLite, et en bonus une visualtion avec Streamlit.

---

## 🧱 Architecture

Le projet repose sur deux services Docker principaux :

- `script_runner` : exécution des scripts Python (import, création base, analyse SQL)
- `sqlite_simplon_db` : service avec SQLite (base de données persistée)

Les services partagent un volume `./data` où la base `ventes.db` est stockée.

---

## 🔄 Fonctionnement automatique

L’ensemble des opérations se fait automatiquement via `main.py` avec:
- Création de la base
- Import des données (depuis des URLs Google Sheets en CSV données)
- Lancement des analyses SQL
- Stockage des résultats dans une table `analyses` dans la bd

---

## 🧠 Analyses effectuées

- Chiffre d'affaires total
- Ventes par produit (quantité et CA)
- Ventes par ville
- Résultats stockés dans la table `analyses`
---
## 📊 Visualisation, Dashboard Interactive avec Google Looker Studio

Un Dashboard permet de visualiser les données de façon interactive : [visit dashboard](https://lookerstudio.google.com/reporting/9c19ab2e-12a7-4d3e-8e1f-ccb79281aab0) 
- CA total (metric)
- Graphique de ventes par produit
- Graphique de ventes par ville
- Carte de la France avec les ventes par Villes
- peut facilement être partagé et entretenu pour les analystes

---

## 🌍 Application Streamlit

Une application Streamlit permet de visualiser les données de façon interactive :
- CA total (metric)
- Graphique par produit
- Graphique par ville
- Affichage des données brutes
- peut facilement être augmenté et hébergé

### Lancer l’app streamlit localement (bonus):

Apres avoir activé le conteneur et que la bd existe:
```bash
cd ./bonus_appli_streamlit_visualisation/
streamlit run app_streamlit.py
```

### Base requise :
Le fichier `ventes.db` doit être présent dans un dossier `data/` à la racine.

---

## 📁 Contenu du projet

- `Dockerfile` : image Python + scripts
- `docker-compose.yml` : orchestre les services
- `main.py` : point d’entrée du traitement
- `creation_db.py`, `import_data.py`, `analyse_sql.py` : modules
- `app_streamlit.py` : app Streamlit
- `data/ventes.db` : base SQLite (générée)


---

## ✅ Résultat

Le projet respecte l’ensemble des objectifs, est modulaire, automatisé, et prêt à être présenté ou enrichi avec de nouvelles données en temps réel.


