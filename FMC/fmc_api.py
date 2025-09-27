import requests
import json

# Replace with your FMC details
FMC_HOST = "https://<fmc-ip>"
USERNAME = "<your-username>"
PASSWORD = "<your-password>"

def get_auth_token():
    url = f"{FMC_HOST}/api/fmc_platform/v1/auth/generatetoken"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, auth=(USERNAME, PASSWORD), headers=headers, verify=False)
    response.raise_for_status()
    token = response.headers.get('X-auth-access-token')
    domain_uuid = response.headers.get('DOMAIN_UUID')
    if not token:
        raise Exception("Failed to get auth token")
    return token, domain_uuid

def get_devices(token, domain_uuid):
    url = f"{FMC_HOST}/api/fmc_config/v1/domain/{domain_uuid}/devices/devicerecords"
    headers = {
        'X-auth-access-token': token,
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()

def get_access_policies(token, domain_uuid):
    url = f"{FMC_HOST}/api/fmc_config/v1/domain/{domain_uuid}/policy/accesspolicies"
    headers = {
        'X-auth-access-token': token,
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    requests.packages.urllib3.disable_warnings()
    token, domain_uuid = get_auth_token()
    devices = get_devices(token, domain_uuid)
    policies = get_access_policies(token, domain_uuid)

    print("Devices:")
    print(json.dumps(devices, indent=2))
    print("\nAccess Policies:")
    print(json.dumps(policies, indent=2))