from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)


# Configuration de la connexion
db_config = {
    'host': '172.19.0.4',
    'port': 3306,
    'user': 'root',
    'password': 'rootpass',
    'database': 'billetterie'
}

@app.route('/')
def home():
    return "🎉 Bienvenue sur l'API de billetterie !"

# 🔍 Liste des utilisateurs
@app.route('/utilisateurs', methods=['GET'])
def get_utilisateurs():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM utilisateur")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 🔍 Liste des événements
@app.route('/evenements', methods=['GET'])
def get_evenements():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM evenement")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ➕ Créer une réservation
@app.route('/reservation', methods=['POST'])
def creer_reservation():
    data = request.json
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        sql = """
            INSERT INTO reservation (id_evenement, id_utilisateur, nb_places, statut)
            VALUES (%s, %s, %s, %s)
        """
        values = (
            data['id_evenement'],
            data['id_utilisateur'],
            data['nb_places'],
            data.get('statut', 'en attente')
        )

        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Réservation enregistrée ✅'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
