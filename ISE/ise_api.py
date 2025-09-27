import requests

# ISE API configuration
ISE_HOST = "https://<ise_host>"  # Replace with your ISE server address
USERNAME = "<username>"          # Replace with your ISE username
PASSWORD = "<password>"          # Replace with your ISE password

# Disable SSL warnings (not recommended for production)
requests.packages.urllib3.disable_warnings()

def get_ise_info(endpoint="/ers/config/endpoint"):
    url = f"{ISE_HOST}{endpoint}"
    headers = {
        "Accept": "application/json"
    }
    response = requests.get(url, auth=(USERNAME, PASSWORD), headers=headers, verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

if __name__ == "__main__":
    # Example: Get endpoints from ISE
    data = get_ise_info()
    if data:
        print(data)