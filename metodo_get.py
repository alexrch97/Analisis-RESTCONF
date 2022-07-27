# Programa que establece la funcion HTTPS GET
# Autor: Alex Remache
# Fecha: Julio 14, 2022
# Version: 1.0

# Librerias
import sys # acceso a variables
sys.path.append("/home/devasc/labs/devnet-src/restconf_labs") # directorio actual
import info_basica as i # info_basica.py
import requests # Permite realizar APIs HTTP 
import json # JSON

# Funcion 
def metodo_get(url): 
    # peticion 
    resp = requests.get(url, auth=i.ingreso, headers=i.encabezado, verify=False)
    # Respuesta
    if resp.status_code in [200, 201, 202, 204]:
        print(f"Exitoso. Metodo GET. Status code: {resp.status_code}")
        response_json = resp.json()
        print(json.dumps(response_json, indent=4))
    else:
        print(f"Error al recuperar datos. Status code: {resp.status_code}")
