# Imagen base con Python 3.12 slim para construir dependencias
FROM python:3.12.0-slim AS builder

# Actualizamos paquetes y añadimos herramientas necesarias para compilar dependencias nativas y librerías PostgreSQL
RUN apt update -y && apt install -y build-essential libpq-dev gcc

# Definimos el directorio de trabajo donde se copiará el código
WORKDIR /app

# Copiamos el contenido del proyecto al directorio de trabajo en la imagen builder
COPY . .

# -------------------------------------------------------

# Imagen base final, también Python 3.12 slim, para producción
FROM python:3.12.0-slim AS final

# Instalamos PostgreSQL, utilidades relacionadas y herramientas de red y edición (nano, curl, net-tools)
RUN apt update -y && \
    apt install -y postgresql postgresql-contrib libpq-dev curl nano net-tools pgloader

# Cambiamos a usuario postgres para configurar base de datos
USER postgres

# Arrancamos PostgreSQL, esperamos 5 segundos para asegurar inicio, y creamos un usuario y base de datos para la app
RUN /etc/init.d/postgresql start && sleep 5 && \
    psql --command "CREATE USER elama WITH PASSWORD 'uhu.2024';" && \
    psql --command "CREATE DATABASE esprolama OWNER elama;"

# Volvemos a usuario root para continuar con configuraciones y copias
USER root

# Establecemos directorio de trabajo para la aplicación
WORKDIR /app

# Copiamos el código desde la etapa builder para evitar instalar dependencias innecesarias en la imagen final
COPY --from=builder /app /app

# Actualizamos pip e instalamos las dependencias Python sin cache para reducir tamaño
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Iniciamos el servicio de PostgreSQL, migramos la base de datos Django,
# migramos datos de SQLite a PostgreSQL con pgloader,
# y eliminamos archivos temporales para limpieza
RUN service postgresql start && \
    sleep 1 && \
    python /app/manage.py migrate && \
    pgloader sqlite:///app/db.sqlite3 postgresql://elama:uhu.2024@localhost/esprolama && \
    rm -rf /app/db.sqlite3 /app/.dockerignore /app/requirements.txt 2> /dev/null

# Exponemos el puerto 8000 para la aplicación Django
EXPOSE 8000

# Variables de entorno para conexión a base de datos
ENV DB_NAME=esprolama
ENV DB_USER=elama
ENV DB_PASSWORD=uhu.2024
ENV DB_HOST=localhost
ENV DB_PORT=5432

# Comando para arrancar PostgreSQL y luego ejecutar el servidor de desarrollo Django en 0.0.0.0:8000
CMD /bin/sh -c "service postgresql start && python manage.py runserver 0.0.0.0:8000"
