import requests

# Replace with your actual Meraki API key
API_KEY = 'YOUR_MERAKI_API_KEY'
ORG_ID = 'YOUR_ORG_ID'  # Replace with your organization ID

BASE_URL = 'https://api.meraki.com/api/v1'

headers = {
    'X-Cisco-Meraki-API-Key': API_KEY,
    'Content-Type': 'application/json'
}

def get_networks(org_id):
    url = f'{BASE_URL}/organizations/{org_id}/networks'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_devices(network_id):
    url = f'{BASE_URL}/networks/{network_id}/devices'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def main():
    networks = get_networks(ORG_ID)
    for network in networks:
        print(f"Network: {network['name']} (ID: {network['id']})")
        devices = get_devices(network['id'])
        if devices:
            for device in devices:
                print(f"  Device: {device.get('name', 'N/A')} | Model: {device.get('model', 'N/A')} | Serial: {device.get('serial', 'N/A')}")
        else:
            print("  No devices found.")
        print('-' * 40)

if __name__ == '__main__':
    main()