param (
    [switch]$NoDocker
)

# Habilitar salida de errores
$ErrorActionPreference = "Stop"

if (-not $NoDocker) {
    Write-Host "🚀 Iniciando contenedores en modo detach..."
    docker compose up -d

    # Verificar si hubo un error en la ejecución de docker-compose up
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Error al iniciar los contenedores." -ForegroundColor Red
        exit 1
    }

    Write-Host "🛑 Deteniendo el servicio 'web'..."
    docker compose stop web

    if ($LASTEXITCODE -ne 0) {
        Write-Host "⚠️ Advertencia: No se pudo detener el servicio 'web'." -ForegroundColor Yellow
    }
}

Write-Host "🐍 Iniciando el servidor de Django en modo desarrollo..."
try {
    .\.venv\Scripts\python.exe manage.py runserver 127.0.0.1:8000
} catch {
    Write-Host "❌ Error al ejecutar el servidor de Django." -ForegroundColor Red
    exit 1
}

Write-Host "✅ Servidor en ejecución en http://127.0.0.1:8000"
