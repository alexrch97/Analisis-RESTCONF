# Programa que establece los parametros iniciales 
# Autor: Alex Remache
# Fecha: Julio 14, 2022
# Version: 1.0

# Librerias
import json # JSON
import requests # Permite realizar APIs HTTP
from requests.auth import  HTTPBasicAuth # Autenticacion
import urllib3 # Certificados SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # Deshabilita

# Variables
user = "admin" # usuario 
pwd = "admin" # contrasenia del usuario
formato = "application/yang-data+json" # formato JSON
server = "192.168.2.1" # IP servidor RESTCONF
port = 443 # Puerto HTTPS
rest_path = "restconf" # URL del modulo YANG

# Autenticacion
ingreso = HTTPBasicAuth(user, pwd)

# Encabezado HTTP-GET
encabezado = { "Accept": formato, 
                "Content-Type": formato } # Encabezado
