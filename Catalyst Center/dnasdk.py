from dnacentersdk import DNACenterAPI

# Replace these with your DevNet Sandbox credentials
DNAC_URL = "https://sandboxdnac.cisco.com"
USERNAME = "devnetuser"
PASSWORD = "Cisco123!"

# Create DNACenterAPI object and authenticate
dnac = DNACenterAPI(
    base_url=DNAC_URL,
    username=USERNAME,
    password=PASSWORD,
    verify=False
)

# Get list of devices
devices = dnac.devices.get_device_list()

# Print devices
for device in devices:
    print(device)