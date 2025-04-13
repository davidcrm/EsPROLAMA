# EsPROLAMA[^1]
[^1]: Evaluación y Desarrollo de Programas de Español como Lengua Adicional para Migrantes Adultos

**EsPROLAMA** es una herramienta diseñada para apoyar la enseñanza y el aprendizaje del español en contextos migratorios.

Su objetivo es facilitar la integración lingüística y cultural de personas adultas que necesitan el español para su vida cotidiana, su trabajo y su desarrollo social. A través de estrategias de autoevaluación, materiales didácticos interactivos y enfoques comunicativos, EsPROLAMA busca ofrecer un aprendizaje flexible y adaptado a las necesidades de cada migrante. Además, proporciona recursos para docentes y facilitadores, asegurando una enseñanza efectiva y contextualizada. 

Los centros encargados de impartir español como lengua  adicional para migrantes pueden autoevaluar sus competencias con esta herramienta y obtener el certificado Cervantes.


## Despliegue

### Clonar el repositorio

Primero, clona el repositorio en tu máquina local:

```shell
git clone https://github.com/davidcrm/EsPROLAMA.git
cd EsPROLAMA
```

### Ubuntu

1. **Instalar Apache:**<br />
   Ejecuta el siguiente comando para instalar Apache en tu sistema:

   ```shell
   sudo apt install apache2 -y
   ```
   
2. **Habilitar los módulos necesarios de Apache:**
    ```shell
    sudo a2enmod proxy
    sudo a2enmod proxy_http
    ```

3. **Reemplazar el contenido del archivo de configuración de Apache:**<br />
    Abre el archivo `/etc/apache2/sites-available/000-default.conf` y reemplaza su contenido por el siguiente:

    ```shell
    <VirtualHost *:80>
      # ServerAdmin webmaster@localhost
      DocumentRoot /var/www/html

      # Proxy inverso: redirige todas las solicitudes a localhost:8000
      ProxyPass / http://localhost:8000/
      ProxyPassReverse / http://localhost:8000/

      # Configuración adicional para logs
      ErrorLog ${APACHE_LOG_DIR}/esprolama-error.log
      CustomLog ${APACHE_LOG_DIR}/esprolama-access.log combined
    </VirtualHost>
    ```

4. **Reiniciar Apache:**
   ```shell
   sudo systemctl restart apache2
   ```
   
5. **Levantar los contenedores Docker:**
    ```shell
    ./scripts/deploy.sh
    ```
   
### Windows

1. **Instalar XAMPP:**<br />
    Si aún no tienes XAMPP instalado, descárgalo e instálalo desde su [sitio web oficial](https://www.apachefriends.org/).

2. **Configurar Apache en XAMPP:**

   - Ir a `C:\xampp\apache\conf\httpd.conf` y descomentar las siguientes líneas:

     ```apache
     LoadModule proxy_module modules/mod_proxy.so
     LoadModule proxy_http_module modules/mod_proxy_http.so
     ```

   - Ir a `C:\xampp\apache\conf\extra\httpd-vhosts.conf` y reemplazar el contenido del archivo por el siguiente:

     ```apache
     <VirtualHost *:80>
         # ServerAdmin webmaster@localhost
         DocumentRoot "C:/xampp/htdocs/"

         # Proxy inverso: redirige todas las solicitudes a localhost:8000
         ProxyPass / http://localhost:8000/
         ProxyPassReverse / http://localhost:8000/

         # Configuración adicional para logs
         ErrorLog "logs/esprolama-error.log"
         CustomLog "logs/esprolama-access.log" combined
     </VirtualHost>
     ```

3. **Reiniciar Apache:**
    <p>Después de realizar los cambios, reinicia el servicio de Apache en XAMPP desde el panel de control de XAMPP.</p>

4. **Levantar los contenedores Docker:**<br />
    Finalmente, ejecuta los siguientes comandos para iniciar los contenedores Docker en segundo plano:

   ```bash
   ./scripts/deploy.ps1
   ```
