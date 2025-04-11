# Verifica si Docker está instalado
$dockerInstalled = Get-Command docker -ErrorAction SilentlyContinue
if (-not $dockerInstalled) {
    Write-Host "Docker no está instalado. Por favor, instala Docker primero." -ForegroundColor Red
    exit 1
}

# Definir nombre para la imagen y el contenedor
$appName = "esprolama"
$imageVersion = "latest"
$imageName = "$appName:$imageVersion"
$containerName = "$appName"
$postgresVolume = "${appName}_postgres_data"

# Construir la imagen Docker
Write-Host "Construyendo la imagen Docker..."
docker build -t $imageName ..

if ($?) {
    Write-Host "Imagen construida exitosamente." -ForegroundColor Green
} else {
    Write-Host "Hubo un error al construir la imagen." -ForegroundColor Red
    exit 1
}

# Verificar si el volumen de PostgreSQL ya existe, si no, crearlo
$volumeExists = docker volume ls --quiet --filter name=$postgresVolume
if (-not $volumeExists) {
    Write-Host "Creando volumen de PostgreSQL..."
    docker volume create $postgresVolume

    if ($?) {
        Write-Host "Volumen creado exitosamente." -ForegroundColor Green
    } else {
        Write-Host "Hubo un error al crear el volumen." -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "El volumen '$postgresVolume' ya existe." -ForegroundColor Yellow
}

# Ejecutar el contenedor Docker con el volumen mapeado
Write-Host "Ejecutando el contenedor Docker..."
docker run -d --name $containerName -v $postgresVolume:/var/lib/postgresql/data -p 8000:8000 $imageName

if ($?) {
    Write-Host "Contenedor ejecutado exitosamente. Accede a tu aplicación en http://0.0.0.0:8000" -ForegroundColor Green
} else {
    Write-Host "Hubo un error al ejecutar el contenedor." -ForegroundColor Red
    exit 1
}
