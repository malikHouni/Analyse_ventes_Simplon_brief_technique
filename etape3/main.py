from creation_db import create_db
from import_data_url import import_data
from analyse_sql import analyse_ventes


'''
programme principale permettant d'executer les autre script de creation de db, d'import des données et d'analyse(et insertion des resultats dans la bd)
'''
if __name__ == "__main__":
    create_db()
    import_data()
    analyse_ventes()
