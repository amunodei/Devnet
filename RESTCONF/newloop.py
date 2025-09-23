import requests
from requests.auth import HTTPBasicAuth

# RESTCONF details
HOST = "192.168.8.152"
USERNAME = "atkins"
PASSWORD = "atkins"
URL = f"https://{HOST}/restconf/data/ietf-interfaces:interfaces"

# Loopback interface payload
payload = {
    "ietf-interfaces:interface": {
        "name": "Loopback22",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "22.22.22.22",
                    "netmask": "255.255.255.255"
                }
            ]
        }
    }
}

headers = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json"
}

# Disable SSL warnings (for demo purposes)
requests.packages.urllib3.disable_warnings()

response = requests.post(
    URL,
    json=payload,
    headers=headers,
    auth=HTTPBasicAuth(USERNAME, PASSWORD),
    verify=False
)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")