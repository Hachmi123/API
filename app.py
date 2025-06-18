from flask import Flask, request, jsonify
from flask_cors import CORS  # ← ajout

app = Flask(__name__)
CORS(app)  # ← autorise les requêtes cross-origin (depuis Flutter Web)

# Variable globale pour stocker les constantes vitales
current_vitals = {
    "heartRate": 0,
    "spo2": 0,
    "temperature": 0
}

@app.route('/api/vitals', methods=['POST', 'GET'])
def handle_vitals():
    global current_vitals

    if request.method == 'POST':
        data = request.json
        print("Données reçues :", data)
        current_vitals = data
        return jsonify({"status": "received"}), 200

    elif request.method == 'GET':
        return jsonify(current_vitals), 200

if __name__ == '__main__':
    # ← écoute toutes les IPs locales, ce qui est utile pour Flutter Web
    app.run(host='0.0.0.0', port=5000)
