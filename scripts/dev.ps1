$ErrorActionPreference = "Stop"

Write-Host "🚀 Iniciando contenedor postgres..."
docker start elama_postgres

Write-Host "🐍 Iniciando el servidor de Django en modo desarrollo..."
try {
    .\.venv\Scripts\python.exe manage.py runserver 0.0.0.0:8000
} catch {
    Write-Host "❌ Error al ejecutar el servidor de Django." -ForegroundColor Red
    exit 1
}

Write-Host "✅ Servidor en ejecución en http://0.0.0.0:8000"