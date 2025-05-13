import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense

# Carga los datos limpios
df = pd.read_csv("datos_limpios.csv")

# Asignamos los nombres de las columnas
df.columns = [
    "fecha", "flow",
    "flow_min", "flow_max", "flow_avg", "flow_sp",
    "p1_current", "p1_min", "p1_max", "p1_avg", "p1_sp",
    "p2_current", "p2_min", "p2_max", "p2_avg",
    "v1", "v2", "latch_position"
]

# Seleccionamos las columnas relevantes para el análisis (caudal y presiones)
input_data = df[["flow", "p1_current", "p2_current"]]  # Usamos flow y las dos presiones como entrada

# Escalamos los datos entre 0 y 1
scaler = MinMaxScaler()
input_scaled = scaler.fit_transform(input_data)

# Definimos las variables de entrada
input_dim = input_scaled.shape[1]

# Creamos el autoencoder
input_layer = Input(shape=(input_dim,))
encoded = Dense(10, activation='relu')(input_layer)
encoded = Dense(5, activation='relu')(encoded)
decoded = Dense(10, activation='relu')(encoded)
output_layer = Dense(input_dim, activation='sigmoid')(decoded)

# Capa para la predicción de la presión ideal (en este caso, p1_current)
pressure_input = Dense(1, activation='linear', name='pressure_output')(encoded)  # Salida para la presión ideal

# Creamos el modelo
autoencoder = Model(inputs=input_layer, outputs=[output_layer, pressure_input])
autoencoder.compile(optimizer='adam', loss=['mse', 'mse'], loss_weights=[0.8, 0.2])  # Hacemos énfasis en la reconstrucción

# Entrenamos el modelo
history = autoencoder.fit(
    input_scaled, [input_scaled, df['p1_current']],  # Usamos los datos de p1_current como la etiqueta para la predicción
    epochs=50,
    batch_size=32,
    validation_split=0.1,
    shuffle=True,
    verbose=1
)

# Predecimos la presión ideal para el conjunto de datos
reconstructions, predicted_pressure = autoencoder.predict(input_scaled)

# Extraemos la predicción de la presión ideal
df['predicted_pressure'] = predicted_pressure

# Guardamos los resultados
df.to_csv("resultados_con_presion_ideal.csv", index=False)

# Visualizamos los resultados
plt.figure(figsize=(10, 6))
plt.plot(df['predicted_pressure'], label='Presión Predicha')
plt.plot(df['p1_current'], label='Presión Real', alpha=0.7)
plt.legend()
plt.title("Presión Real vs. Presión Predicha")
plt.xlabel("Índice")
plt.ylabel("Presión")
plt.show()

# Opcional: Visualizar el error de reconstrucción
reconstructions_error = np.mean(np.power(input_scaled - reconstructions, 2), axis=1)
threshold = np.percentile(reconstructions_error, 95)  # El 5% más alto se considera anómalo

# Visualizamos el error de reconstrucción
plt.figure(figsize=(10, 6))
plt.plot(reconstructions_error, label='Error de reconstrucción')
plt.axhline(y=threshold, color='r', linestyle='--', label='Umbral')
plt.legend()
plt.title("Error de Reconstrucción y Umbral de Anomalías")
plt.xlabel("Índice")
plt.ylabel("Error")
plt.show()
