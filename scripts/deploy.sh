#!/bin/bash

# Verifica si Docker está instalado
if ! command -v docker &> /dev/null; then
    echo -e "\e[31mDocker no está instalado. Por favor, instala Docker primero.\e[0m"
    exit 1
fi

# Definir nombre para la imagen y el contenedor
appName="esprolama"
imageVersion="latest"
imageName="${appName}:${imageVersion}"
containerName="${appName}"
postgresVolume="${appName}_postgres_data"

# Construir la imagen Docker
echo "Construyendo la imagen Docker..."
if docker build -t "$imageName" .; then
    echo -e "\e[32mImagen construida exitosamente.\e[0m"
else
    echo -e "\e[31mHubo un error al construir la imagen.\e[0m"
    exit 1
fi

# Verificar si el volumen de PostgreSQL ya existe, si no, crearlo
if ! docker volume inspect "$postgresVolume" > /dev/null 2>&1; then
    echo "Creando volumen de PostgreSQL..."
    if docker volume create "$postgresVolume" > /dev/null; then
        echo -e "\e[32mVolumen creado exitosamente.\e[0m"
    else
        echo -e "\e[31mHubo un error al crear el volumen.\e[0m"
        exit 1
    fi
else
    echo -e "\e[33mEl volumen '$postgresVolume' ya existe.\e[0m"
fi

# Ejecutar el contenedor Docker con el volumen mapeado
echo "Ejecutando el contenedor Docker..."
if docker run -d --name "$containerName" -v "${postgresVolume}:/var/lib/postgresql/data" -p 8000:8000 "$imageName"; then
    echo -e "\e[32mContenedor ejecutado exitosamente. Accede a tu aplicación en http://0.0.0.0:8000\e[0m"
else
    echo -e "\e[31mHubo un error al ejecutar el contenedor.\e[0m"
    exit 1
fi
