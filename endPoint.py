import json
import numpy as np
import boto3
import os
import tensorflow as tf
from tensorflow.keras.models import load_model

# Cargar el modelo una sola vez
MODEL_PATH = '/opt/modelo_lstm.h5'  # /opt es donde van los archivos de una capa en Lambda
model = load_model(MODEL_PATH)

def lambda_handler(event, context):
    try:
        # Leer los datos del cuerpo del JSON (esperamos un vector de 95 o 96 números)
        body = json.loads(event['body'])
        entrada = body['entrada']  # Lista de floats
        
        if len(entrada) != 96:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'La entrada debe contener exactamente 96 elementos'})
            }

        # Convertir a formato LSTM: [1, 96, 1]
        datos = np.array(entrada).reshape((1, 96, 1))

        # Predecir
        pred = model.predict(datos)
        pred = pred[0][0]

        return {
            'statusCode': 200,
            'body': json.dumps({'prediccion': float(pred)})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
