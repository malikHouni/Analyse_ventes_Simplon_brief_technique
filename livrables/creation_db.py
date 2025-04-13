import sqlite3


def create_db():
    # Connexion à la base SQLite (elle sera créée si elle n'existe pas)
    conn = sqlite3.connect("/root/db/ventes.db")  # chemin dans le volume partagé
    cursor = conn.cursor()

    # Création des tables

    # Produits
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produits (
        id_ref TEXT PRIMARY KEY,
        nom TEXT NOT NULL,
        prix REAL NOT NULL,
        stock INTEGER NOT NULL
    );
    """)

    # Magasins
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magasins (
        id_magasin INTEGER PRIMARY KEY,
        ville TEXT NOT NULL,
        nombre_salaries INTEGER
    );
    """)

    # Ventes
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ventes (
        id_vente INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        id_ref TEXT NOT NULL,
        quantite INTEGER NOT NULL,
        id_magasin INTEGER NOT NULL,
        FOREIGN KEY (id_ref) REFERENCES produits(id_ref),
        FOREIGN KEY (id_magasin) REFERENCES magasins(id_magasin)
    );
    """)

    # Analyses
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS analyses (
        id_analyse INTEGER PRIMARY KEY AUTOINCREMENT,
        type_analyse TEXT NOT NULL,
        resultat TEXT NOT NULL,
        date_analyse TEXT DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Sauvegarde et fermeture de la connexion
    conn.commit()
    conn.close()

    print("Base de données et tables créées avec succès!.")
