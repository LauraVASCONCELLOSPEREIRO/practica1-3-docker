# Imagen base de Python ligera
FROM python:3.12-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiamos primero las dependencias
COPY requirements.txt /app/requirements.txt

# Instalamos dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código
COPY . /app

# Comando de arranque: ejecuta tu main.py
CMD ["python", "main.py"]
