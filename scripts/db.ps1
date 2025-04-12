$ErrorActionPreference = "Stop"

$containerName = "elama_postgres"
$pgUser = "elama"
$pgPass = "uhu.2024"
$pgDb   = "esprolama"

# Verifica si el contenedor ya existe
$containerExists = docker ps -a --format "{{.Names}}" | Where-Object { $_ -eq $containerName }

if (-not $containerExists) {
    Write-Host "⚠️ El contenedor '$containerName' no existe. Creándolo..."
    docker run -d --name $containerName `
        -p 5432:5432 `
        -e POSTGRES_USER=$pgUser `
        -e POSTGRES_PASSWORD=$pgPass `
        -e POSTGRES_DB=$pgDb `
        postgres:16
} else {
    $isRunning = docker ps --format "{{.Names}}" | Where-Object { $_ -eq $containerName }

    if (-not $isRunning) {
        Write-Host "▶️ El contenedor '$containerName' existe pero no está corriendo. Iniciándolo..."
        docker start $containerName
    } else {
        Write-Host "✅ El contenedor '$containerName' ya está corriendo."
    }
}

# Esperar a que PostgreSQL esté listo (opcional, pero útil)
Start-Sleep -Seconds 5

Write-Host "🔄 Actualizando apt e instalando pgloader en el contenedor $containerName..."
docker exec $containerName bash -c "apt update -y && apt install -y pgloader"

Write-Host "🔄 Ejecutando migraciones Django (si aplica)..."
python manage.py migrate

Write-Host "🔄 Copiando db.sqlite3 al contenedor $containerName..."
docker cp db.sqlite3 ${containerName}:/tmp/db.sqlite3

Write-Host "🔄 Ejecutando pgloader para migrar datos desde SQLite a PostgreSQL..."
$pgloaderCmd = "pgloader sqlite:///tmp/db.sqlite3 postgresql://${pgUser}:`"$pgPass`"@localhost/$pgDb"
docker exec $containerName bash -c $pgloaderCmd

Write-Host "✅ Proceso completado."
