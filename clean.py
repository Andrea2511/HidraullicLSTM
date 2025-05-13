import pandas as pd

# Lee el archivo CSV
df = pd.read_csv("delta_logs.csv", skiprows=13)

# Renombra las columnas
df.columns = [
    "fecha", "flow",
    "flow_min", "flow_max", "flow_avg", "flow_sp",
    "p1_current", "p1_min", "p1_max", "p1_avg", "p1_sp",
    "p2_current", "p2_min", "p2_max", "p2_avg",
    "v1", "v2", "latch_position"
]

# Convierte la columna 'fecha' a datetime
df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')

# Elimina filas donde la fecha no se pudo convertir
df = df.dropna(subset=['fecha'])

# Convierte las demás columnas a numéricas
for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Elimina filas con valores faltantes
df = df.dropna()

# Guarda el archivo limpio para usarlo luego
df.to_csv("datos_limpios.csv", index=False)

# Verifica
print("Archivo limpio guardado como 'datos_limpios.csv'")
print(df.head())