# azure-disks-step-disk-delete

This [Azure](https://azure.microsoft.com/en-us/services/storage/disks/) step container deletes a set of
Azure disks in an Azure subscription given a list of resource IDs.

## Specification

| Setting | Child setting | Data type | Description | Default | Required |
|---------|---------------|-----------|-------------|---------|----------|
| `azure` || mapping | A mapping of Azure account configuration. | None | True |
|| `connection` | Azure Connection | Connection for the Azure account. Use the Connection sidebar to configure the Azure Connection | None | True |
| `resourceIDs` ||  An array of Azure Disk resource IDs | The list of resource IDs of the Azure Disks to be deleted | None | True |
| `waitForDeletion` ||  boolean | Determines whether to wait for Disks to be deleted before continuing | False | False | 


## Outputs
None

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


