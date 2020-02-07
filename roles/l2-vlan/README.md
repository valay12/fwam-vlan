Role Name
=========

Role contains tasks, data to perform vlan creation on an access switch.
Input needed:
- vlan id (user input)
- vlan name (user input)
- access ports (user input)

Tasks performed:
- Verify vlan id(s) is valid (700-800)
- Verify vlan name starts with 'FWAM'
- Verify access ports are valid (has to be between Eth1/10-Eth1/40)
- Generates pre-change, change, post-change, backout, verify restoration scripts in output directory
- Gather pre-change snapshot
- Perform change configuration
- Gather post-change snapshot and compare
- Backout if any errors
- Verify successful rollback

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
