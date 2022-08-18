# 
#  Sample code creates new boot volume from existing boot volume
#  You may still add more attributes to CreateBootVolumeDetails and create_boot_volume.
#  Refer: https://docs.oracle.com/en-us/iaas/tools/python/2.79.0/api/core/models/oci.core.models.CreateBootVolumeDetails.html
#  
#  Sample Output (Masked):
#  {
#    "auto_tuned_vpus_per_gb": 10,
#    "availability_domain": "Qhab:US-ASHBURN-AD-3",
#    "boot_volume_replicas": null,
#    "compartment_id": "ocid1.tenancy.oc1..<MASKED>",
#    "defined_tags": {},
#    "display_name": "NEW-BOOT-VOLUME",
#    "freeform_tags": {},
#    "id": "ocid1.bootvolume.oc1.iad.<MASKED>",
#    "image_id": "ocid1.image.oc1.iad.<MASKED>",
#    "is_auto_tune_enabled": true,
#    "is_hydrated": false,
#    "kms_key_id": null,
#    "lifecycle_state": "PROVISIONING",
#    "size_in_gbs": 47,
#    "size_in_mbs": 47694,
#    "source_details": {
#      "id": "ocid1.bootvolume.oc1.iad.<MASKED>",
#      "type": "bootVolume"
#    },
#    "system_tags": {},
#    "time_created": "2022-08-18T03:37:08.070000+00:00",
#    "volume_group_id": null,
#    "vpus_per_gb": 10
#  }
# 

import oci
import os.path
import sys

config = oci.config.from_file()
config['region'] = "us-ashburn-1"

core_client = oci.core.BlockstorageClient(config)

create_boot_volume_response = core_client.create_boot_volume(
    create_boot_volume_details=oci.core.models.CreateBootVolumeDetails(
        compartment_id=config['tenancy'],
        display_name="NEW-BOOT-VOLUME",
        source_details=oci.core.models.BootVolumeSourceFromBootVolumeDetails(
            type="bootVolume",
            id="ocid1.bootvolume.oc1.iad.abuwcljsfuccmyusdas46altaqh4up6qkuznnbmaklb5zhcsxepkv3wxhpnq")))

# Get the data from response
print(create_boot_volume_response.data)
