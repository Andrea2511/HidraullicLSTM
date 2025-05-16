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

## Librerias usadas 

- Pandas
Es una librería de Python para manipulación y análisis de datos estructurados, especialmente en forma de tablas (similares a Excel o bases de datos).

![Image](https://github.com/user-attachments/assets/9603c7ca-44fa-43e5-a1c8-aa8d818f2d96)

![Image](https://github.com/user-attachments/assets/7a53e1f7-4df2-45c6-88eb-ce8f797ee045)
  
- Matplotlib
Es una librería de Python que permite crear gráficos en 2D como gráficos de líneas, gráficos de barras, gráficos de pastel, entre otros.

![Image](https://github.com/user-attachments/assets/06fa2d24-c064-4600-879c-6a63dec769b0)

---

## Instalación y uso del modelo de IA

### Requisitos previos

Antes de ejecutar el modelo, asegúrate de tener **Python 3.8 o superior** instalado en tu sistema. También necesitarás de tu IDE favorito y `pip` para instalar las dependencias.


### 🚀 Instrucciones de instalación y ejecución

1. **Descomprime el archivo del proyecto (`server.zip`)** en tu directorio de trabajo.

2. **Instala las dependencias del proyecto**:

```bash
pip install -r requirements.txt
```

Alternativamente, si tienes problemas con el archivo requirements.txt, puedes usar:

```bash
pip install ./requirements.txt
```

3. **Ejecuta la apliación**

```bash
python app.py
```

## Simulación del Funcionamiento

Para simular el comportamiento del sistema, realizamos pruebas utilizando un vector de entrada como el siguiente:

![Image](https://github.com/user-attachments/assets/16632aeb-7dc3-41a0-a82a-1a5998cbdf5d)

En esa misma imagen podemos observar la predicción que arroja la IA. 

El sistema IoT real funciona de forma similar: envía los datos actuales y recibe la predicción. Si la presión actual se desvía significativamente del valor estimado, se activa una alerta de posible anomalía.

## Observando resultados


