#busan meraki get the ID of all device
#python3

import json
from meraki_sdk.meraki_sdk_client import MerakiSdkClient
from meraki_sdk.exceptions.api_exception import APIException

x_cisco_meraki_api_key = 'meraki key'
meraki = MerakiSdkClient(x_cisco_meraki_api_key)


orgs = meraki.organizations.get_organizations()
print (orgs)

#

params = {}
params["organization_id"] = "org id"
nets = meraki.networks.get_organization_networks(params)
print(nets)

#

meraki = MerakiSdkClient(x_cisco_meraki_api_key)

devices_controller = meraki.devices

network_id = 'network id'

try:
    result = devices_controller.get_network_devices(network_id)
except APIException as e:
    print(e)

print (result)

j = len(result)
print (j)

for i in range (0, j):
    #print (json.dumps(result[i], indent=4))
    ppp = result[i]
    print (ppp["mac"],ppp["name"],ppp["lat"],ppp["lng"] )

