# HidraullicLSTM

# Sistema de Predicción de Presión con LSTM

Este proyecto implementa un modelo de inteligencia artificial basado en redes neuronales **LSTM (Long Short-Term Memory)**, diseñado para predecir la frecuencia de calibración de presión en una red de tuberías. Su principal objetivo es **detectar posibles fugas** o anomalías mediante el análisis de datos históricos de presión.

---

## ¿Cómo funciona?

El modelo recibe **96 valores consecutivos de presión** (en formato JSON) y predice el siguiente valor esperado. Esta predicción se interpreta como la frecuencia recomendada para **calibrar la presión** del sistema.

Si el valor real de la presión **no concuerda** con el valor predicho, se considera que **puede existir una fuga o anomalía** en el sistema de tuberías.

---

## Entrenamiento del Modelo

- El modelo fue entrenado con datos de presión.
- Recibe una **ventana de 96 datos** y predice el dato número 97.
- Los datos fueron **normalizados antes del entrenamiento** y **desnormalizados** al momento de evaluar los resultados.

---

## Simulación del Funcionamiento

Para simular el comportamiento del sistema, realizamos pruebas utilizando un vector de entrada como el siguiente:

![Image](https://github.com/user-attachments/assets/16632aeb-7dc3-41a0-a82a-1a5998cbdf5d)
