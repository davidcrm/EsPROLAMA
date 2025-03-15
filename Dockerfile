FROM python:3.12.0-slim AS build

# Instalación de paquetes utilitarios
RUN apt update && apt install -y build-essential libpq-dev gcc wget curl nano net-tools

WORKDIR /app

# Copiar archivos de la aplicación
COPY . /app

# Instalar dependencias de la aplicación
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Limpieza de archivos y directorios innecesarios
RUN rm -rf /app/.venv 2> /dev/null \
    && rm -rf /app/.git 2> /dev/null \
    && rm /app/README.md 2> /dev/null \
    && rm /app/Dockerfile 2> /dev/null \
    && rm /app/requirements.txt 2> /dev/null \
    && rm /app/docker-compose.yml 2> /dev/null

# Exponer el puerto 8000
EXPOSE 8000

# Dar valor a las variables de entorno
ENV DB_NAME=esprolama
ENV DB_USER=elama
ENV DB_PASSWORD=uhu.2024
ENV DB_HOST=db
ENV DB_PORT=5432

# Iniciar la aplicación de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
