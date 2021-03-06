# azure-disks-step-disk-list

This [Azure](https://azure.microsoft.com/en-us/services/storage/disks/) step container lists the disks
in an Azure subscription or resource group and sets an output, `disks`, to an array of disks objects.

## Example output `disks`

```
[
  {
   "id":"/subscriptions/c82736ee-c108-452b-8178-f548c95d18fe/resourceGroups/kenaz/providers/Microsoft.Compute/disks/vm-1_OsDisk_1_31a0429f0a2a4d23a92d8258d4686e46",
   "name":"vm-1_OsDisk_1_31a0429f0a2a4d23a92d8258d4686e46",
   "type":"Microsoft.Compute/disks",
   "location":"westus",
   "sku":{
      "name":"Premium_LRS",
      "tier":"Premium"
   },
   "time_created":"2020-05-01T20:55:49.301463Z",
   "os_type":"Linux",
   "hyper_vgeneration":"V1",
   "creation_data":{
      "create_option":"FromImage",
      "image_reference":{
         "id":"/Subscriptions/c82736ee-c108-452b-8178-f548c95d18fe/Providers/Microsoft.Compute/Locations/westus/Publishers/Canonical/ArtifactTypes/VMImage/Offers/UbuntuServer/Skus/18.04-LTS/Versions/18.04.202004290"
      }
   },
   "disk_size_gb":30,
   "disk_size_bytes":32213303296,
   "unique_id":"31a0429f-0a2a-4d23-a92d-8258d4686e46",
   "provisioning_state":"Succeeded",
   "disk_iops_read_write":120,
   "disk_mbps_read_write":25,
   "disk_state":"Unattached",
   "encryption":{
      "type":"EncryptionAtRestWithPlatformKey"
   }
  }
]
```

