from acitool.acitoolkit import Session, Tenant
from acitool.acitoolkit.aciphysobject import *

session = Session('https://sandboxapicdc.cisco.com', 'admin', 'admin')
resp = session.login()
if not resp.ok:
    print("Login failed")
else:
    tenants = Tenant.get(session)
    for tenant in tenants:
        print(tenant.name)