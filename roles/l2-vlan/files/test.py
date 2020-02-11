#!/usr/bin/env python2
import sys
import json

def get_range(list):
  return range(list[0],list[1]+1)

vlans = json.loads(sys.argv[1])
function = json.loads(sys.argv[2])
vlan_ids = []
vlan_names = []

for vlan in vlans:
  if vlan['vlan_id'] not in get_range(function[(vlan['function'])]['vlan_range']):
    print "ERROR: vlan not in function range"
    break
  if vlan['name'] not in function[vlan['function']['vlan_prefix']:
    print "ERROR: Invalid vlan value"
    break

#print type(vlans[0]['vlan_id'])
#print vlan_names
#print vlan_ids
#print vlans[0]['vlan_id']
