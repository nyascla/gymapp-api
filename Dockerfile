FROM python:3.10-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el backend a la imagen
COPY ./ ./

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8000 para FastAPI
EXPOSE 8001

# Comando para iniciar la aplicación FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
