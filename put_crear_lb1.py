# Programa que crea la interfaz Loopback1 del agente
# Autor: Alex Remache
# Fecha: Julio 14, 2022
# Version: 1.0
# Metodo HTTPS: PUT

import sys # acceso a variables
sys.path.append("/home/devasc/labs/devnet-src/restconf_labs") # directorio actual
import info_basica as i # info_basica.py
import metodo_get as get # metodo_get.py
import metodo_put as put # metodo_put.py

# URL
url = f"https://{i.server}:{i.port}/{i.rest_path}/data/ietf-interfaces:interfaces/interface=Loopback1" 
print(url)

# Payload
yangConfig = """
{
    "ietf-interfaces:interface": {
        "name": "Loopback1",
        "description": "Loopback 1",
        "type": "iana-if-type:softwareLoopback",
        "enabled": true,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "20.1.1.1",
                    "netmask": "255.255.255.0"
                }
                ]
            },
        "ietf-ip:ipv6": {}
    }
}
"""

put.metodo_put(url,yangConfig)
get.metodo_get(url)
