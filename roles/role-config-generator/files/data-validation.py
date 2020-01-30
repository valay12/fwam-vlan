import ipaddress

def ipv4_subnet_of(subnet,supernet):
  subnet = ipaddress.ip_network(unicode(subnet))
  supernet = ipaddress.ip_network(unicode(supernet))
  if supernet.network_address <= subnet.network_address and supernet.broadcast_address >= subnet.broadcast_address:
    return True
  else:
    return False
