#!/bin/bash

set -e

containerName="elama_postgres"
pgUser="elama"
pgPass="uhu.2024"
pgDb="esprolama"

# Verifica si el contenedor ya existe
if ! docker ps -a --format "{{.Names}}" | grep -q "^${containerName}$"; then
    echo "⚠️  El contenedor '$containerName' no existe. Creándolo..."
    docker run -d --name "$containerName" \
        -p 5432:5432 \
        -e POSTGRES_USER="$pgUser" \
        -e POSTGRES_PASSWORD="$pgPass" \
        -e POSTGRES_DB="$pgDb" \
        postgres:16
else
    if ! docker ps --format "{{.Names}}" | grep -q "^${containerName}$"; then
        echo "▶️  El contenedor '$containerName' existe pero no está corriendo. Iniciándolo..."
        docker start "$containerName"
    else
        echo "✅ El contenedor '$containerName' ya está corriendo."
    fi
fi

echo "⏳ Esperando a que el contenedor esté listo..."
sleep 5

echo "🔄 Actualizando apt e instalando pgloader en el contenedor $containerName..."
docker exec "$containerName" bash -c "apt update -y && apt install -y pgloader"

echo "🔄 Ejecutando migraciones Django (si aplica)..."
python3 manage.py migrate

echo "🔄 Copiando db.sqlite3 al contenedor $containerName..."
docker cp db.sqlite3 "${containerName}:/tmp/db.sqlite3"

echo "🔄 Ejecutando pgloader para migrar datos desde SQLite a PostgreSQL..."
pgloaderCmd="pgloader sqlite:///tmp/db.sqlite3 postgresql://${pgUser}:${pgPass}@localhost/${pgDb}"
docker exec "$containerName" bash -c "$pgloaderCmd"

echo "✅ Proceso completado."
