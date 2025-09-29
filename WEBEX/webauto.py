import requests

url = "https://webexapis.com/v1/teams"

payload = '''{ "name": "DEVNET TEAM" }'''

headers = {
    "Authorization": "Bearer M2E1MmU3YmItMjkyZS00YTkyLWI5ODktMDIyZDU0MmI5NGVmODVhMzM2NjktYjVk_P0A1_bdd2aed2-da17-481d-bd6f-b43037ee90b7",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.request('POST', url, headers=headers, data = payload)

print(response.text.encode('utf8'))

