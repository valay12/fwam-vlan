def ipv4_subnet_of(subnet,supernet):
  subnet_of = False
  if is_valid(subnet) & is_valid(supernet):
    

def is_valid(subnet):
  is_valid = False
  [network_addr,mask] = subnet.split("/")
  


def octet(int_octet):
  int_octet = int(int_octet)
  raw_octet = bin(int_octet)[2:]
  zero_padding = '0'*(8-len(raw_octet))
  return zero_padding+raw_octet

