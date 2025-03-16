#!/bin/bash

set -e

echo "Esperando a que PostgreSQL inicie..."
until pg_isready -h localhost -U "$POSTGRES_USER"; do
  sleep 2
done

echo "Verificando si hay datos en auth_user..."
USER_COUNT=$(psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -t -c "SELECT COUNT(*) FROM auth_user;" | tr -d '[:space:]')

if [ "$USER_COUNT" -eq "0" ]; then
  echo "No hay datos en auth_user. Migrando desde SQLite..."
  
  # Instalar pgloader (debes hacer esto si no está preinstalado en la imagen de PostgreSQL)
  apt update -y && apt install pgloader -y

  # Ejecutar pgloader
  pgloader sqlite:///tmp/db.sqlite3 postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@localhost/$POSTGRES_DB

  echo "Migración completada."
else
  echo "Ya hay datos en auth_user. No se requiere migración."
fi

exec "$@"
