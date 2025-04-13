# fichier analyse_sql.py

import sqlite3
import json

def analyse_ventes():
    conn = sqlite3.connect("/root/db/ventes.db")
    cursor = conn.cursor()

    # 1.Requete Chiffre d’affaires total
    cursor.execute("""
        SELECT SUM(v.quantite * p.prix) AS chiffre_affaires_total
        FROM ventes v
        JOIN produits p ON v.id_ref = p.id_ref
    """)
    ca_total = cursor.fetchone()[0]
    print(f"=> Chiffre d’affaires total : {ca_total} €")
    #  requete inserstion des données d'analyse dans la table analyses
    cursor.execute("""
        INSERT INTO analyses (type_analyse, resultat)
        VALUES (?, ?)
    """, ("Chiffre d’affaires total", str(ca_total)))

    # 2.Requete Ventes par produit
    cursor.execute("""
        SELECT p.nom, SUM(v.quantite) AS total_vendus, SUM(v.quantite * p.prix) AS chiffre_affaires
        FROM ventes v
        JOIN produits p ON v.id_ref = p.id_ref
        GROUP BY p.id_ref
    """)
    resultats_produits = cursor.fetchall()
    print("\n=> Ventes par produit :")
    for row in resultats_produits:
        print(row)
    #  requete inserstion des données d'analyse dans la table analyses
    cursor.execute("""
        INSERT INTO analyses (type_analyse, resultat)
        VALUES (?, ?)
    """, ("Ventes par produit", json.dumps(resultats_produits)))

    # 3.Requete Ventes par ville
    cursor.execute("""
        SELECT m.ville, SUM(v.quantite * p.prix) AS chiffre_affaires
        FROM ventes v
        JOIN magasins m ON v.id_magasin = m.id_magasin
        JOIN produits p ON v.id_ref = p.id_ref
        GROUP BY m.ville
    """)
    resultats_villes = cursor.fetchall()
    print("\n=> Ventes par ville :")
    for row in resultats_villes:
        print(row)
    

    #  requete inserstion des données d'analyse dans la table analyses
    cursor.execute("""
        INSERT INTO analyses (type_analyse, resultat)
        VALUES (?, ?)
    """, ("Ventes par ville", json.dumps(resultats_villes)))

    conn.commit()
    conn.close()

    print("\n💾 Résultats bien stockés dans la table 'analyses'. Projet biref Simplon fini!")
