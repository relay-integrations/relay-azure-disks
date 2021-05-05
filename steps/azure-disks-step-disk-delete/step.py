#!/usr/bin/env python

from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient
from relay_sdk import Interface, Dynamic as D
import logging

logging.basicConfig(level=logging.WARNING)

relay = Interface()

credentials = ClientSecretCredential(
    client_id=relay.get(D.azure.connection.clientID),
    client_secret=relay.get(D.azure.connection.secret),
    tenant_id=relay.get(D.azure.connection.tenantID)
)
subscription_id=relay.get(D.azure.connection.subscriptionID)
compute_client = ComputeManagementClient(credentials, subscription_id)

# Getting resource ids & options
resource_ids = None
wait = False 

try:
  resource_ids = relay.get(D.resourceIDs)
except:
  print('No Resource IDs found. Exiting.')
  exit

try:
  wait = relay.get(D.waitForDeletion)
except:
  pass

print('Deleting {} Azure Virtual disks(s)'.format(len(resource_ids)))

# Deletes each disk in resource_ids
disk_handle_list = []
for resource_id in resource_ids:
  resource_group_name = resource_id.split('/')[4] # Resource group name
  disk_name = resource_id.split('/')[8] # VM name
  print('Deleting Azure Disk {0} in Resource Group {1}'.format(disk_name, resource_group_name))  
  async_disk_operation = compute_client.disks.begin_delete(resource_group_name, disk_name)
  disk_handle_list.append(async_disk_operation)


# If wait is set, wait for VMs to terminate before exiting.
if wait: 
  for async_disk_operation in disk_handle_list:
    print('Waiting for Azure Disks to be deleted.')
    async_disk_operation.wait()

print('All specified Azure Disks are deleted.')
