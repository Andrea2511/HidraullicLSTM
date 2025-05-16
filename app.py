import random
from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# Conectar a MongoDB
client = MongoClient(
    "mongodb+srv://root:root@cluster0.l8qjw.mongodb.net/AREP-tstm?retryWrites=true&w=majority"
)
db = client["AREP-tstm"]
collection = db["data"]

# Cargar el modelo al iniciar la aplicación
model = load_model(
    "modelo_lstm.h5", custom_objects={"mse": tf.keras.losses.MeanSquaredError()}
)

# Vector de localidades de Bogotá
localidades = [
    "Chapinero",
    "Usaquén",
    "Suba",
    "Engativá",
    "Fontibón",
    "Kennedy",
    "Bosa",
]


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        input_vector = data.get("input_vector")

        if not input_vector or len(input_vector) != 96:
            return jsonify(
                {
                    "error": f"El vector de entrada debe tener 96 valores, se encontraron {len(input_vector)}"
                }
            ), 400

        # Preparar el input para el modelo
        input_array = np.array(input_vector).reshape((1, 96, 1))
        prediction = model.predict(input_array)
        prediction_value = float(prediction[0][0])

        # Seleccionar localidad aleatoria
        localidad = random.choice(localidades)

        # Guardar en MongoDB
        collection.insert_one(
            {
                "timestamp": datetime.utcnow(),
                "input_vector": input_vector,
                "prediction": prediction_value,
                "localidad": localidad,
            }
        )

        return jsonify({"prediction": prediction_value, "localidad": localidad})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
