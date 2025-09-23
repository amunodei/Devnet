import requests
import json

url = "https://192.168.8.155/ins"

payload = json.dumps({
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "show version",
    "output_format": "json"
  }
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic YWRtaW46TUF0dGhldzEyIyQ=',
  'Cookie': 'nxapi_auth=admin:175865248116235612'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
