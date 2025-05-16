import requests
import csv

# URL del endpoint
url = "http://localhost:5000/predict"

# Vector base
base_vector = [
    22.8,
    24.4,
    24.2,
    23.3,
    25.0,
    25.0,
    24.7,
    22.8,
    21.9,
    24.2,
    24.4,
    22.5,
    22.8,
    21.9,
    23.1,
    21.7,
    23.1,
    22.2,
    23.1,
    23.1,
    24.7,
    28.3,
    27.2,
    46.9,
    46.9,
    50.0,
    56.4,
    58.9,
    67.5,
    68.3,
    71.4,
    74.7,
    71.4,
    73.1,
    78.1,
    71.9,
    79.7,
    80.6,
    83.9,
    81.9,
    75.0,
    76.1,
    77.9,
    76.1,
    76.4,
    70.8,
    83.6,
    81.7,
    75.6,
    77.2,
    82.5,
    75.6,
    73.6,
    73.6,
    75.0,
    64.4,
    67.2,
    66.9,
    62.8,
    62.2,
    61.7,
    56.7,
    56.4,
    54.2,
    53.9,
    53.6,
    51.7,
    55.3,
    53.1,
    52.2,
    50.8,
    49.7,
    47.8,
    49.2,
    46.7,
    46.7,
    58.6,
    45.8,
    43.6,
    41.4,
    37.5,
    35.0,
    34.7,
    32.8,
    31.4,
    30.6,
    29.2,
    26.7,
    26.9,
    24.2,
    80.6,
    83.9,
    81.9,
    75.0,
    76.1,
    78.9,
]

# Ruta del archivo CSV con los nuevos datos (debes guardarlos en un archivo, por ejemplo 'datos.csv')
archivo_csv = "datos_limpios.csv"

# Leer el archivo CSV y enviar las peticiones
with open(archivo_csv, newline="") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Saltar encabezado si lo tiene

    for row in reader:
        # Ignorar la primera columna (timestamp)
        valores = list(map(float, row[1:]))

        # Asegurarte de que solo haya 96 valores
        valores = valores[:96]  # cortar si hay más
        if len(valores) < 96:
            valores += [0] * (96 - len(valores))  # rellenar con ceros si hay menos

        payload = {"input_vector": valores}

        try:
            response = requests.post(url, json=payload)
            print(f"Status: {response.status_code}, Response: {response.text}")
        except Exception as e:
            print(f"Error enviando datos: {e}")
