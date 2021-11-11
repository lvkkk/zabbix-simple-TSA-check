#!/usr/bin/env python3

import sys
import struct, json, re, socket 


#10351
data='{"request":"sender data","data":[{"host":"mtstsa","key":"timestamp","value":"' + sys.argv[1] + '"}]}'
print(data)
packet = "ZBXD\1" + struct.pack('<Q', len(data)).decode('ascii') + data

zabbix = socket.socket()
# ~ zabbix_host = "127.0.0.1"
zabbix_host = "10.2.36.22"
zabbix_port = 10051
try:
    zabbix.connect((zabbix_host, zabbix_port))
except ImportError:
    print("Network exception")
zabbix.sendall(packet.encode('ascii'))

data = ''
while True:
    packet = zabbix.recv(16)
    if not packet: break
    data += packet.decode('ascii')

print(data)
res_str = json.dumps(data, indent=4, separators=(',', ': '))
# ~ print(res_str)
zabbix.close()

"""

#!/usr/bin/env python3

import sys
import struct, json, re, socket 
# ~ import urllib.request
# ~ import urllib.parse

# ~ zbxHost = {"host":"127.0.0.1"}
zbxHost = {"host":"10.2.36.22"}
zbxHost["trapperport"] = 10051

# ~ data='{"request":"sender data","data":[{"host":"10351","key":"timestamp","value":"' + sys.argv[1] + '"}]}'
data='{"request":"sender data","data":[{"host":"mtstsa","key":"timestamp","value":"' + sys.argv[1] + '"}]}'
print(data)
packet = "ZBXD\1" + struct.pack('<Q', len(data)).decode('ascii') + data

zabbix = socket.socket()
try:
	zabbix.connect((zbxHost["host"], zbxHost["trapperport"]))
	print("debug 1")
except ImportError:
	print("Network exception")
	zabbix.sendall(packet.encode('ascii'))
	print("debug 2")

data = ''
while True:
	packet = zabbix.recv(16)
	print("debug 3")
	if not packet: break
	data += packet.decode('ascii')
	print("debug 32")

print(data)
res_str = json.dumps(data, indent=4, separators=(',', ': '))
print("debug 4")
zabbix.close()



#10351
"""
