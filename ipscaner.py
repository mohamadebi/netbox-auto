import networkscan
from netbox import NetBox
netbox=NetBox(host='192.168.70.238', port=8000 ,use_ssl=False, auth_token='b80b683247388c0c579924f886a37267237e7df1')

if __name__ == '__main__':
    
    my_network = "192.168.70.0/24"

    my_scan = networkscan.Networkscan(my_network)

    my_scan.run()

    for address in my_scan.list_of_hosts_found:
        print(address)
        netbox.ipam.create_ip_address(address)

