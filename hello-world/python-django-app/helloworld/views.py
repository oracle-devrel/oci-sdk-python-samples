from django.http import HttpResponse

import oci
import os.path
import sys

def index(request):
    config = oci.config.from_file()
    config['region'] = "us-ashburn-1"

    compute_client = oci.core.ComputeClient(config)

    response = compute_client.list_instances(compartment_id = config['tenancy'])

    output = ""
    for instance in response.data:
        output += instance.id + "<br>"

    return HttpResponse(output)
