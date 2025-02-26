# Utiliser une image de base Python 3
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements-spark.txt dans le conteneur
COPY requirements-spark.txt requirements-spark.txt

# Installer les dépendances depuis requirements-spark.txt
RUN pip install --no-cache-dir -r requirements-spark.txt

# Copier tout le contenu du répertoire courant dans le conteneur
COPY . .

# # Commande pour démarrer le script
# CMD ["python", "app.py"]
