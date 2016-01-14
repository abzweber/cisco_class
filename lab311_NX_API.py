from device import Device

sw1 = Device(ip='172.31.217.138', username='admin', password='cisco123')

sw1.open()

command = sw1.show('show int e1/48')
print command

import xmltodict
import json
command = sw1.show('sh int e1/48')
result = xmltodict.parse(command[1])
print json.dumps( result, indent=4)



ip = result['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']['eth_ip_addr']
print ip

mask = result['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']['eth_ip_mask']
print mask

print ip + '/' + mask

sh_vlan = sw1.show('sh vl')
sh_vlan_dict = xmltodict.parse(sh_vlan[1])
print json.dumps( sh_vlan_dict, indent=4)


vlan10_name = sh_vlan_dict['ins_api']['outputs']['output']['body']['TABLE_vlanbrief']['ROW_vlanbrief'][1]['vlanshowbr-vlanname']
print vlan10_name


vlans = sh_vlan_dict['ins_api']['outputs']['output']['body']['TABLE_vlanbrief']['ROW_vlanbrief']
for each in vlans:
	print 'VLAN ID: ', each['vlanshowbr-vlanid-utf']
	print 'VLAN NAME: ', each['vlanshowbr-vlanname']
	print '=' * 25

push_l3port = sw1.conf('config t ; interface e1/24 ; no switchport ')
push_l3ip = sw1.conf('config t ; interface e1/24 ; ip address 172.19.21.1/24 ')
cmd = 'config t ; int e1/24 ; '

