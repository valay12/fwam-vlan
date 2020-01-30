This repository contains the playbook and role needed for generating 
vlan trunking configuration.

It will be developed in 2 phases:
1) Online Read/Offline Write:
User enters change variables (vlan(s), routers, switch) in inventory 
file, runs playbook, finds implementation, backout configuration in output 
folder.

2) Online Read/Write:
User generates change configuration as per Phase-1. Then runs 
configuration playbook, changes are implemented on device, verified, 
backed out if there is any issue.

Workflow:

1) User enters following change variables:
- Vlan number
- Vlan description
- Vlan function
- ipv4 subnet
- ipv6 subnet
- function-specific variables (unique_id, acl, qos, dhcp_relay, etc)

2) User enters command to run config_generation playbook specifying the 
change variables inventory.

3) config_generation playbook calls config_generation role.

4) config_generation role contains tasks:
    
Task-1: Verify that change variables are compliant with 
infrastructure standards
[pending detailed description]

Task-2: Obtain device variables using ios_facts, nxos_facts modules.
[pending detailed description]

Task-3: Reference change variables, device variables into change 
templates and generate configuration in ouput folder.
[pending detailed description]

5) User validates configuration files, runs 
vlan configuration playbook.

6) Configuration playbook contains following tasks:

Task-1: Perform pre-change checks on devices and generates Green/Red 
flag.
[pending detailed description]

Task-2: If green flag, implement changes on devices. If red flag, 
generate error message
[pending detailed description]

Task-3: Perform post-change checks on devices and generates Green/Red 
flag.
[pending detailed description]

Task-4: If green flag, exit. If red flag, perform backout changes, 
compare with pre-change state. If error persists, generate 
need_manual_intervention flag.
[pending detailed description]

VARIABLES:

There will be 3 types of variables utilized in this process:
1) Change variables (User enters)
- vlan_id
- vlan_name
- vlan_function
- vlan_ipv4_subnet
- vlan_ipv6_subnet
- unique_id
- dhcp_relay

2) Standards variables (Static, cannot be changed)
3) Device variables (Ansible enters)
