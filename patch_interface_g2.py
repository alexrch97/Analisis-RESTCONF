# Programa que recolecta la informacion de la interfaz
# GigabitEthernet 2 del agente
# Autor: Alex Remache
# Fecha: Julio 14, 2022
# Version: 1.0
# Metodo HTTPS: PATCH

import sys # acceso a variables
sys.path.append("/home/devasc/labs/devnet-src/restconf_labs") # directorio actual
import info_basica as i # info_basica.py
import metodo_get as get # metodo_get.py
import metodo_patch as patch # metodo_patch.py

# URL
url = f"https://{i.server}:{i.port}/{i.rest_path}/data/ietf-interfaces:interfaces/interface=GigabitEthernet2" 
print(url)

# Payload
yangConfig = """
{
    "ietf-interfaces:interface": {
        "enabled": "true",
        "description": "To R1",
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "10.1.1.10",
                    "netmask": "255.255.255.0"
                }
            ]
        }
    }
}
"""

patch.metodo_patch(url,yangConfig)
get.metodo_get(url)
