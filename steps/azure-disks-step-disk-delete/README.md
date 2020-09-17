# azure-disks-step-disk-delete

This [Azure](https://azure.microsoft.com/en-us/services/storage/disks/) step container deletes a set of
Azure disks in an Azure subscription given a list of resource IDs.

## Example  

```yaml
steps:
# ...
- name: azure-disks-delete-disks
  image: relaysh/azure-disks-step-disk-delete
  spec:
    azure:
      connection: !Connection { type: azure, name: my-azure-account }
    resourceIDs:
    - /subscriptions/c84756ef-c108-45cb-8138-f548c95djk9o/resourceGroups/my-rg/providers/Microsoft.Compute/disks/my-vm-osdisk
    - /subscriptions/c84756ef-c108-45cb-8138-f548c95djk9o/resourceGroups/my-rg/providers/Microsoft.Compute/disks/my-vm-datadisk
```

## Notes
To get the Azure Disk resource IDs, try the following command using the Azure CLI: 
 ```
 $ az disk list | jq ".[].id"

"/subscriptions/c84756ef-c108-45cb-8138-f548c95djk9o/resourceGroups/my-rg/providers/Microsoft.Compute/disks/my-vm-osdisk"
"/subscriptions/c84756ef-c108-45cb-8138-f548c95djk9o/resourceGroups/my-rg/providers/Microsoft.Compute/disks/my-vm-datadisk"
```

For more information on Resource IDs, check out the [documentation]("https://docs.microsoft.com/en-us/rest/api/resources/resources/getbyid"). 


