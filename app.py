from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Define custom metrics and losses that might be in the model
# This addresses the serialization issue with 'mse'
import keras.metrics as metrics
import keras.losses as losses

# Cargar el modelo al iniciar la aplicación
model = load_model(
    "modelo_lstm.h5", custom_objects={"mse": tf.keras.losses.MeanSquaredError}
)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        input_vector = data.get("input_vector")

        if not input_vector or len(input_vector) != 96:
            return jsonify(
                {
                    "error": "El vector de entrada debe tener 96 valores, se encontraron {}".format(
                        len(input_vector)
                    )
                }
            ), 400

        # Preparar el input para el modelo
        input_array = np.array(input_vector).reshape((1, 96, 1))
        prediction = model.predict(input_array)

        # Convert numpy float32 to Python native float
        prediction_value = float(prediction[0][0])

        return jsonify({"prediction": prediction_value})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
