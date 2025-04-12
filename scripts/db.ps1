$ErrorActionPreference = "Stop"

$containerName = "elama_postgres"
$containerExists = docker ps -a --format "{{.Names}}" | Where-Object { $_ -eq $containerName }

if (-not $containerExists) {
    Write-Host "⚠️ El contenedor '$containerName' no existe. Creándolo..."
    docker run -d --name $containerName -p 5432:5432 -e POSTGRES_USER=elama -e POSTGRES_PASSWORD=uhu.2024 -e POSTGRES_DB=esprolama postgres:16
} else {
    $isRunning = docker ps --format "{{.Names}}" | Where-Object { $_ -eq $containerName }

    if (-not $isRunning) {
        Write-Host "▶️ El contenedor '$containerName' existe pero no está corriendo. Iniciándolo..."
        docker start $containerName
    } else {
        Write-Host "✅ El contenedor '$containerName' ya está corriendo."
    }
}

Write-Host "🔄 Actualizando apt e instalando pgloader en el contenedor $containerName..."
docker exec $containerName bash -c "apt update -y && apt install pgloader -y"

Write-Host "🔄 Ejecutando migraciones..."
python manage.py migrate

Write-Host "🔄 Copiando db.sqlite3 al contenedor $containerName..."
docker cp db.sqlite3 ${containerName}:/tmp/db.sqlite3

Write-Host "🔄 Ejecutando pgloader para migrar datos desde SQLite a PostgreSQL..."
docker exec $containerName bash -c "pgloader sqlite:///tmp/db.sqlite3 postgresql://elama:uhu.2024@localhost/esprolama"

Write-Host "✅ Proceso completado."
