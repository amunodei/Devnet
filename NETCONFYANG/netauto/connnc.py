import paramiko
from ncclient import manager

# Device credentials
HOST = '192.168.8.120'  # Replace with your device IP
USERNAME = 'admin'
PASSWORD = 'admin'
COMMAND = 'show ip interface brief'

def get_show_ip_int_br(host, username, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, username=username, password=password, look_for_keys=False, allow_agent=False)
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        print(output)
    finally:
        client.close()

if __name__ == "__main__":
    def get_show_ip_int_br_netconf(host, username, password):
        with manager.connect(host=host, port=830, username=username, password=password,
                            hostkey_verify=False, device_params={'name': 'default'}) as m:
            filter = '''
            <filter>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <interface/>
                </native>
            </filter>
            '''
            response = m.get(filter)
            print(response.xml)

    get_show_ip_int_br_netconf(HOST, USERNAME, PASSWORD)