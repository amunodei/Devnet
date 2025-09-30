from fmcapi import FMC
from fmcapi.api_objects.apiclasstemplate import DeviceRecords

# Replace with your FMC details
FMC_HOST = "https://your-fmc-host"
FMC_USERNAME = "your-username"
FMC_PASSWORD = "your-password"

def main():
    with FMC(host=FMC_HOST, username=FMC_USERNAME, password=FMC_PASSWORD, autodeploy=True) as fmc:
        # Example: List all devices
        devices = DeviceRecords(fmc=fmc)
        devices.get()
        for device in devices.items:
            print(f"Device Name: {device['name']}, ID: {device['id']}")

if __name__ == "__main__":
    main()