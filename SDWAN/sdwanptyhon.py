import requests
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

VMANAGE_HOST = "https://your-vmanage-host"  # Replace with your vManage IP or hostname
USERNAME = "devenetuser"
PASSWORD = "Cisco12345!"

def get_jsessionid(host, username, password):
    url = f"{host}/j_security_check"
    payload = {'j_username': username, 'j_password': password}
    session = requests.session()
    response = session.post(url, data=payload, verify=False)
    if response.status_code == 200 and 'JSESSIONID' in session.cookies:
        return session.cookies['JSESSIONID'], session
    else:
        print("Authentication failed.")
        exit(1)

def get_devices(host, session):
    url = f"{host}/dataservice/device"
    headers = {'Content-Type': 'application/json'}
    response = session.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        print("Failed to retrieve devices.")
        exit(1)

def print_devices(devices):
    if not devices:
        print("No devices found.")
        return
    print(f"{'Hostname':20} {'Device Type':15} {'System IP':15} {'Site ID':10}")
    print("-" * 65)
    for device in devices:
        print(f"{device.get('host-name', 'N/A'):20} {device.get('device-type', 'N/A'):15} {device.get('system-ip', 'N/A'):15} {device.get('site-id', 'N/A'):10}")

if __name__ == "__main__":
    jsessionid, session = get_jsessionid(VMANAGE_HOST, USERNAME, PASSWORD)
    devices = get_devices(VMANAGE_HOST, session)
    print_devices(devices)