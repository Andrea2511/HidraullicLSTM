import pandas as pd
import numpy as np

# Cargar el dataset limpio
df = pd.read_csv('datos_limpios.csv')

# Elige solo la columna que quieres predecir (por ejemplo, caudal)
# Puedes cambiar 'flow_avg' por cualquier otra variable que te interese
serie = df['flow_avg'].values  # -> array de solo una columna numérica

# Normalizar si lo deseas (opcional)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
serie = scaler.fit_transform(serie.reshape(-1, 1)).flatten()  # 1D para LSTM

# Parámetro: tamaño de la ventana
ventana = 96

# Crear X e y
X, y = [], []
for i in range(len(serie) - ventana):
    X.append(serie[i:i+ventana])
    y.append(serie[i+ventana])  # la siguiente

X = np.array(X)
y = np.array(y)

# Dar forma para LSTM: [samples, timesteps, features]
X = X.reshape((X.shape[0], X.shape[1], 1))  # 1 característica por paso

# Guardar los archivos
np.save('X_lstm.npy', X)
np.save('y_lstm.npy', y)

print("X shape:", X.shape)  # Debe ser (n_ejemplos, 96, 1)
print("y shape:", y.shape)  # Debe ser (n_ejemplos,)
