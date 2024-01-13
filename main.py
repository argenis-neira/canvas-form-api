from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
  return "root"

@app.route('/save', methods=['POST'])
def save_data():
  data = request.get_json()
  with open("database.txt", 'a') as archivo:
    archivo.write(json.dumps(data) + "\n")
  return "OK"

@app.route('/get_data', methods=['GET'])
def get_data():
  data = []
  with open("database.txt", "r") as archivo:
    for linea in archivo:
      data.append(json.loads(linea))
  return jsonify({"array": data})

if __name__ == '__main__':
  app.run(debug=True)