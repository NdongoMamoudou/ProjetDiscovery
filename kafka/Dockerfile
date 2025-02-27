# # Utiliser Python avec Java (nécessaire pour Kafka)
# FROM openjdk:11-slim

# # Installer Python et Pip
# RUN apt update && apt install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*

# # Définir le répertoire de travail
# WORKDIR /app

# # Copier le fichier requirements-kafka.txt
# COPY requirements-kafka.txt /app/requirements-kafka.txt

# # Installer les dépendances Python
# RUN pip3 install --no-cache-dir -r /app/requirements-kafka.txt

# # Copier tout le contenu du répertoire courant
# COPY . .

# # Commande par défaut (modifié pour pouvoir choisir entre producer et consumer)
# ENTRYPOINT ["python3"]
# CMD ["producer.py"]



# Utilise l'image Python 3.9 en version slim
FROM python:3.9-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier des dépendances et l'installe
COPY requirements-kafka.txt requirements-kafka.txt

RUN pip install --no-cache-dir -r requirements-kafka.txt

# Copie l'ensemble de votre code dans le conteneur
COPY . .


# Définit la commande de lancement de votre application
CMD ["python", "app.py"]
