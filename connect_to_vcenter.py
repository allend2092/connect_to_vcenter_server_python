# This script connects to vCenter Server using a python library
#
# Author: Daryl Allen
#
#
from __future__ import print_function
from vconnector.core import VConnector
import time
import pyVmomi


# Start of the program
if __name__ == '__main__':
    client = VConnector(
        user = 'administrator@vsphere.local',
        pwd = 'VMware1!',
        host = '172.17.0.100'
    )

    client.connect()
    print("I have connected!!!")
    time.sleep(.5)

    vms = client.get_vm_view()
    print(vms.view)

    time.sleep(.5)

    host = client.get_object_by_property(
        property_name='name',
        property_value='esxi1.home.local',
        obj_type=pyVmomi.vim.HostSystem
    )

    print(host.name)
    
    time.sleep(.5)

    datastores = client.get_datastore_view()
    result = client.collect_properties(
        view_ref= datastores,
        obj_type=pyVmomi.vim.Datastore,
        path_set=['name', 'summary.capacity']
    )

    print(result)

    client.disconnect()
    print("I have disconnected!!!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
