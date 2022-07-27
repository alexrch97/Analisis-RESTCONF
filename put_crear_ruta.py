# Programa que crea la ruta estatica a la LAN2 
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
url = f"https://{i.server}:{i.port}/{i.rest_path}/data/ietf-routing:routing/routing-instance=default/routing-protocols/routing-protocol=static,1" 
print(url)

# Payload
yangConfig = """
{
    "ietf-routing:routing-protocol": {
        "type": "ietf-routing:static",
        "name": "1",
        "static-routes": {
            "ietf-ipv4-unicast-routing:ipv4": {
                "route": [
                    {
                        "destination-prefix": "192.168.3.0/24",
                        "next-hop": {
                            "next-hop-address": "10.1.1.20"
                        }
                    }
                ]
            }
        }
    }
}
"""

put.metodo_put(url,yangConfig)
get.metodo_get(url)
