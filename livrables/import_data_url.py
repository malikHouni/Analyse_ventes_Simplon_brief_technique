# import_data.py

import sqlite3
import csv
import os
import requests





def import_data():
    # Connexion à la base
    db_path = "/root/db/ventes.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    base_dir = "/app"  

    # --- Import PRODUITS ---
    # Fetch the content from the URL
    response = requests.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vSawI56WBC64foMT9pKCiY594fBZk9Lyj8_bxfgmq-8ck_jw1Z49qDeMatCWqBxehEVoM6U1zdYx73V/pub?gid=0&single=true&output=csv")

    # Check if the request was successful
    if response.status_code == 200:
        # Read the CSV data from the response content
        reader = csv.DictReader(response.content.decode('utf-8').splitlines())
        for row in reader:
            cursor.execute("""
                INSERT OR IGNORE INTO produits (id_ref, nom, prix, stock)
                VALUES (?, ?, ?, ?)
            """, (row["ID Référence produit"], row["Nom"], float(row["Prix"]), int(row["Stock"])))
    else:
        print(f"Failed to retrieve data from the URL: {response.status_code}")










    # --- Import MAGASINS ---
    # Fetch the content from the URL
    response = requests.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vSawI56WBC64foMT9pKCiY594fBZk9Lyj8_bxfgmq-8ck_jw1Z49qDeMatCWqBxehEVoM6U1zdYx73V/pub?gid=714623615&single=true&output=csv")
    # Check if the request was successful
    if response.status_code == 200:
        # Read the CSV data from the response content
        reader = csv.DictReader(response.content.decode('utf-8').splitlines())
        for row in reader:
            cursor.execute("""
                INSERT OR IGNORE INTO magasins (id_magasin, ville, nombre_salaries)
                VALUES (?, ?, ?)
            """, (int(row["ID Magasin"]), row["Ville"], int(row["Nombre de salariés"])))
    else:
        print(f"Failed to retrieve data from the URL: {response.status_code}")









            

    # --- Import VENTES avec vérification de duplication ---
    # Fetch the content from the URL
    response = requests.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vSawI56WBC64foMT9pKCiY594fBZk9Lyj8_bxfgmq-8ck_jw1Z49qDeMatCWqBxehEVoM6U1zdYx73V/pub?gid=760830694&single=true&output=csv")

    # Check if the request was successful
    if response.status_code == 200:
        # Read the CSV data from the response content
        reader = csv.DictReader(response.content.decode('utf-8').splitlines())
        
        for row in reader:
            # Vérifier si la ligne existe déjà (sur les 3 champs)
            cursor.execute("""
                SELECT COUNT(*) FROM ventes
                WHERE date = ? AND id_ref = ? AND id_magasin = ?
            """, (row["Date"], row["ID Référence produit"], int(row["ID Magasin"])))
            
            exists = cursor.fetchone()[0]
            
            if exists == 0:
                cursor.execute("""
                    INSERT INTO ventes (date, id_ref, quantite, id_magasin)
                    VALUES (?, ?, ?, ?)
                """, (row["Date"], row["ID Référence produit"], int(row["Quantité"]), int(row["ID Magasin"])))
    else:
        print(f"Failed to retrieve data from the URL: {response.status_code}")







    # Commit & Close
    conn.commit()
    conn.close()

    print("Import des données avec urls, terminé avec succès.")
