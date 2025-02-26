# app.py
from flask import Flask, request, jsonify, render_template

from kafka.producer import send_to_kafka


## initialisation de l'application Flask
app = Flask(__name__)


# Route pour afficher le formulaire HTML
@app.route('/')
def index():
    return render_template('index.html')



# Endpoint pour recevoir la découverte
@app.route('/discovery', methods=['POST'])
def add_discovery():
    # Récupérer les données JSON envoyées par le formulaire
    data = request.get_json()

    # Vérification des données
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    print(f"Received discovery data: {data}")

    # Envoi des données vers Kafka
    send_to_kafka(data)

    # Exemple d'une réponse JSON après traitement
    return jsonify({'message': 'Discovery sent successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5550)
