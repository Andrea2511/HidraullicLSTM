import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import EarlyStopping

# Cargar los datos estructurados
X = np.load("X_lstm.npy")
y = np.load("y_lstm.npy")

# Dividir en entrenamiento y prueba
split = int(len(X) * 0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Construir el modelo LSTM
model = Sequential()
model.add(LSTM(units=64, activation='tanh', input_shape=(X.shape[1], X.shape[2])))
model.add(Dense(1))  # salida: un valor (el paso 97)

model.compile(optimizer='adam', loss='mse')
model.summary()

# Entrenar con early stopping
es = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

history = model.fit(
    X_train, y_train,
    validation_data=(X_test, y_test),
    epochs=100,
    batch_size=32,
    callbacks=[es],
    verbose=1
)

# Guardar modelo entrenado
model.save("modelo_lstm.h5")

# Evaluar
loss = model.evaluate(X_test, y_test)
print("MSE en test:", loss)

# Predecir y visualizar
y_pred = model.predict(X_test)

plt.figure(figsize=(10, 5))
plt.plot(y_test, label="Real")
plt.plot(y_pred, label="Predicción", linestyle="--")
plt.title("Predicción del paso 97 usando 96 anteriores")
plt.legend()
plt.show()
