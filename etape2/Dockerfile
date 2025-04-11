# Fichier Dockerfile

# Image de base officielle Python pour utiliser ce language de programmation
FROM python:3.11-slim

# Définir le répertoire de notre travail à réaliser
WORKDIR /app

# Copier le script dans le conteneur construit
COPY hello.py .

# b. Commande pour lancer le script quand le conteneur démarre
CMD ["python", "hello.py"]
