#!/bin/bash

set -e

echo "🚀 Iniciando contenedor postgres..."
docker start elama_postgres

echo "🐍 Iniciando el servidor de Django en modo desarrollo..."
if ! ./.venv/bin/python manage.py runserver 0.0.0.0:8000; then
    echo -e "\e[31m❌ Error al ejecutar el servidor de Django.\e[0m"
    exit 1
fi

echo -e "\e[32m✅ Servidor en ejecución en http://0.0.0.0:8000\e[0m"
