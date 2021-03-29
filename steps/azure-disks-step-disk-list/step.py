#!/usr/bin/env python

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient
from relay_sdk import Interface, Dynamic as D

relay = Interface()

credentials = ServicePrincipalCredentials(
    client_id=relay.get(D.azure.connection.clientID),
    secret=relay.get(D.azure.connection.secret),
    tenant=relay.get(D.azure.connection.tenantID)
)
subscription_id=relay.get(D.azure.connection.subscriptionID)
compute_client = ComputeManagementClient(credentials, subscription_id)

list_of_disks = []

# If resource group is specified, use that
rg = ''
try:
  rg=relay.get(D.resourceGroup)
except:
  print('No resource group specified. Looking up all disks under subscription id.')

if (rg):
 print('Looking up all disks under resource group {0}'.format(rg))
 disks = compute_client.disks.list_by_resource_group(rg)

# Get all disks under a Subscription ID
else: 
  disks = compute_client.disks.list()

# Append disk rsesource ID to list 
print('Found the following Azure Managed Disks:')
print("\n{:<100} {:<30} {:<30} {:<30}".format('NAME', 'LOCATION', 'DISK STATE', 'TAGS')) 

for disk in disks:
  print("{:<100} {:<30} {:<30} {:<30}".format(disk.name, disk.location, disk.disk_state, str(disk.tags)))
  list_of_disks.append(disk.as_dict())


# Setting output variable `disks` to list of Azure disks
print('Setting output `disks` to list of {0} found disks'.format(len(list_of_disks)))
relay.outputs.set('disks', list_of_disks)
