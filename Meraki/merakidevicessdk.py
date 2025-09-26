import meraki

# Replace with your actual Devnet Sandbox API key
API_KEY = 'YOUR_DEVNET_SANDBOX_API_KEY'

# Initialize the Meraki dashboard API client
dashboard = meraki.DashboardAPI(API_KEY)

# Find the organization ID for 'Devnet Sandbox'
orgs = dashboard.organizations.getOrganizations()
org_id = next((org['id'] for org in orgs if org['name'] == 'Devnet Sandbox'), None)

if not org_id:
    print("Organization 'Devnet Sandbox' not found.")
    exit(1)

# Get all networks in the organization
networks = dashboard.organizations.getOrganizationNetworks(org_id)

# For each network, get the list of clients
for network in networks:
    print(f"Clients for network: {network['name']} ({network['id']})")
    try:
        clients = dashboard.networks.getNetworkClients(network['id'], total_pages='all')
        for client in clients:
            print(f" - {client.get('description', client.get('mac', 'Unknown'))}")
    except Exception as e:
        print(f"Error retrieving clients for network {network['name']}: {e}")