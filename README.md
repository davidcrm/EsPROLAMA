# EsPROLAMA

<i>**TODO: Añadir una descripción en condiciones**</i>

## Setup

### Clonar el repositorio

Primero, clona el repositorio en tu máquina local:

```shell
git clone https://github.com/davidcrm/EsPROLAMA.git
cd EsPROLAMA
```

### Ubuntu

1. **Instalar Apache:**
   <p>Ejecuta el siguiente comando para instalar Apache en tu sistema:</p>

   ```shell
   sudo apt install apache2 -y
   ```
   
2. **Habilitar los módulos necesarios de Apache:**
    ```shell
    sudo a2enmod proxy
    sudo a2enmod proxy_http
    ```

3. **Reemplazar el contenido del archivo de configuración de Apache:**
    <p>Abre el archivo `/etc/apache2/sites-available/000-default.conf` y reemplaza su contenido por el siguiente:</p>

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
    docker compose up -d
    ```
   
### Windows

1. **Instalar XAMPP:**
    <p>Si aún no tienes XAMPP instalado, descárgalo e instálalo desde su [sitio web oficial](https://www.apachefriends.org/).</p>

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

4. **Levantar los contenedores Docker:**
    <p>Finalmente, ejecuta los siguientes comandos para iniciar los contenedores Docker en segundo plano:</p>

   ```bash
   docker compose up -d
   ```