# Utilisation d'une image Python de base
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements-backend.txt .

# Installer les dépendances depuis requirements-backend.txt
RUN pip install --no-cache-dir -r /app/requirements-backend.txt

# Copier tout le contenu du répertoire courant dans le conteneur
COPY . .

# Exposer le port sur lequel l'application Flask sera exécutée
EXPOSE 5550

# Définir la commande par défaut pour démarrer l'application
CMD ["python", "app.py"]
