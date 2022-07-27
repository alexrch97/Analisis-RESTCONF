# Programa que recolecta las estadisticas de RESTCONF del agente
# Autor: Alex Remache
# Fecha: Julio 14, 2022
# Version: 1.0
# Metodo HTTPS: GET

# Librerias
import sys # acceso a variables
sys.path.append("/home/devasc/labs/devnet-src/restconf_labs") # directorio actual
import info_basica as i # info_basica.py
import metodo_get as get # metodo_get.py

# URL
url = f"https://{i.server}:{i.port}/{i.rest_path}/data/ietf-restconf-monitoring:restconf-state" 
print(url)

get.metodo_get(url)