import subprocess

routers = [
    "192.168.1.1",
    "192.168.1.2",
    "192.168.1.3",
    "192.168.1.4",
    "192.168.1.5"
]

def ping(host):
    try:
        output = subprocess.check_output(
            ["ping", "-n", "1", host],
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        return True
    except subprocess.CalledProcessError:
        return False

for router in routers:
    result = ping(router)
    print(f"{router}: {'Reachable' if result else 'Unreachable'}")
    print(f"welcome to devnet")