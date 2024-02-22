# Using data file sample-data.json, create output that resembles the following by parsing the included JSON file.

'''
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/35]                              inherit   9150 
'''

import json

with open('lab4/json/sample-data.json', 'r', encoding='utf8') as f:
    data = json.load(f)
    

print('Interface Status')
print('=' * 80)
print(f'{"DN":<50} {"Description":<20} {"Speed":<7} {"MTU":<7}')
print(f'{"-" * 50} {"-" * 20} {"-" * 7} {"-" * 7}')
for im in data['imdata']:
    interface = im['l1PhysIf']['attributes']
    print(f"{interface['dn']:<50} {interface['descr']:<20} {interface['speed']:<7} {interface['mtu']:<7}")