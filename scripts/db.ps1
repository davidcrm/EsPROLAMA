# Habilitar salida de errores
$ErrorActionPreference = "Stop"

Write-Host "📂 Copiando init-database.sh al contenedor..."
docker compose cp .\scripts\init-database.sh db:/init-database.sh

Write-Host "📂 Copiando db.sqlite3 al contenedor..."
docker compose cp db.sqlite3 db:/tmp/db.sqlite3

Write-Host "🔒 Asignando permisos de ejecución al script..."
docker compose exec db chmod +x /init-database.sh

Write-Host "🛢️ Aplicando migraciones de Django"
docker compose exec web bash -c "python manage.py migrate"

Write-Host "🚀 Ejecutando script dentro del contenedor..."
docker compose exec db bash /init-database.sh

Write-Host "✅ Proceso completado."
