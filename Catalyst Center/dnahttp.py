import requests

# Cisco Catalyst Center credentials and URL
url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
username = "admin"
password = "Cisco1234!"

def get_auth_token():
    response = requests.post(
        url,
        auth=(username, password),
        headers={"Content-Type": "application/json"},
        verify=False  # For sandbox, disables SSL verification
    )
    response.raise_for_status()
    token = response.json().get("Token")
    return token

if __name__ == "__main__":
    token = get_auth_token()
    print(f"Auth Token: {token}")