# Habilitar salida de errores
$ErrorActionPreference = "Stop"

Write-Host "🔄 Actualizando apt e instalando pgloader en el contenedor db..."
docker compose exec db bash -c "apt update -y && apt install pgloader -y"

Write-Host "🔄 Ejecutando migraciones en el contenedor web..."
docker compose exec web bash -c "python manage.py migrate"

Write-Host "🔄 Copiando db.sqlite3 al contenedor db..."
docker compose cp db.sqlite3 db:/tmp/db.sqlite3

Write-Host "🔄 Ejecutando pgloader para migrar datos desde SQLite a PostgreSQL..."
docker compose exec db bash -c "pgloader sqlite:///tmp/db.sqlite3 postgresql://elama:uhu.2024@localhost/esprolama"

Write-Host "✅ Proceso completado."
