import requests

# Connection details
APIC_HOST = "https://apic.example.com"  # Replace with your APIC hostname or IP
USERNAME = "admin"
PASSWORD = "12345"

def get_token():
    url = f"{APIC_HOST}/api/aaaLogin.json"
    payload = {
        "aaaUser": {
            "attributes": {
                "name": USERNAME,
                "pwd": PASSWORD
            }
        }
    }
    response = requests.post(url, json=payload, verify=False)
    response.raise_for_status()
    token = response.json()['imdata'][0]['aaaLogin']['attributes']['token']
    return token

def get_tenants(token):
    url = f"{APIC_HOST}/api/node/class/fvTenant.json"
    cookies = {'APIC-cookie': token}
    response = requests.get(url, cookies=cookies, verify=False)
    response.raise_for_status()
    tenants = response.json()['imdata']
    return [t['fvTenant']['attributes']['name'] for t in tenants]

if __name__ == "__main__":
    requests.packages.urllib3.disable_warnings()
    token = get_token()
    tenants = get_tenants(token)
    print("Tenants:")
    for tenant in tenants:
        print(tenant)