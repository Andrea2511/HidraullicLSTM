# Etapa de construcción
FROM python:3.9-slim as builder

WORKDIR /app

# Copiar y instalar dependencias
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Etapa final
FROM python:3.9-slim

WORKDIR /app

# Copiar dependencias desde la etapa de construcción
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copiar la aplicación
COPY --from=builder /app /app

EXPOSE 5000

ENV FLASK_ENV=production

CMD ["python", "app.py"]
