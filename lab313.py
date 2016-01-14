#/usr/bin/env python -tt

import xmltodict
import json
from device import Device

sw1 = Device(ip='172.31.217.138', username='admin', password='cisco123')
sw1.open()

cmd_sh_hardware = sw1.show('show hardware')
result_hardware = xmltodict.parse(cmd_sh_hardware[1])

cmd_sh_intf_mgmt = sw1.show('sh int mgmt0')
result_intf_mgmt = xmltodict.parse(cmd_sh_intf_mgmt[1])

hostname = result_hardware['ins_api']['outputs']['output']['body']['host_name']
os_version = result_hardware['ins_api']['outputs']['output']['body']['rr_sys_ver']

mgmt_intf_ip = result_intf_mgmt['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']['eth_ip_addr']
mgmt_intf_mask = result_intf_mgmt['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']['eth_ip_mask']
mgmt_intf_desc = result_intf_mgmt['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']['desc']
mgmt_intf_speed = result_intf_mgmt['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']['eth_speed']
mgmt_intf_duplex = result_intf_mgmt['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']['eth_duplex']
device_make = result_hardware['ins_api']['outputs']['output']['body']['chassis_id']
device_rr = result_hardware['ins_api']['outputs']['output']['body']['rr_reason']
device_uptime_days = result_hardware['ins_api']['outputs']['output']['body']['kern_uptm_days']
device_uptime_hours = result_hardware['ins_api']['outputs']['output']['body']['kern_uptm_hrs']
device_uptime_min = result_hardware['ins_api']['outputs']['output']['body']['kern_uptm_mins']
device_uptime_sec = result_hardware['ins_api']['outputs']['output']['body']['kern_uptm_secs']
device_btflash = result_hardware['ins_api']['outputs']['output']['body']['bootflash_size']
device_sn = result_hardware['ins_api']['outputs']['output']['body']['TABLE_slot']['ROW_slot']['TABLE_slot_info']['ROW_slot_info']


print 'OS Version ' + os_version
print 'Management IP: ' + mgmt_intf_ip + '/' + mgmt_intf_mask
print 'Interface description: ' + mgmt_intf_desc
print 'Speed / Duplex ' + mgmt_intf_speed + ', ' + mgmt_intf_duplex + ' duplex'
print 'Device Make: ' + device_make
print 'Device Reboot Reason: ' + device_rr
print 'Device Uptime: ' + device_uptime_days + ' days, ' + device_uptime_hours + ' hours, ' + device_uptime_min + ' minutes, and ' + device_uptime_sec + ' seconds'
print 'Bootflash: ' + device_btflash + ' bytes '
try:
	for each in device_sn:
		print each['type']
		print 'Serial Number: ' , each['serial_num']
		print '=' * 45
except:
	pass


