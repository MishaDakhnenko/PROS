ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

route_parts = ospf_route.replace(',', '').split()

protocol = 'OSPF'
prefix = route_parts[1]
ad_metric = route_parts[2].strip('[]')
next_hop = route_parts[4]
last_update = route_parts[5]
outbound_interface = route_parts[6]

print(f"Protocol:            {protocol}")
print(f"Prefix:              {prefix}")
print(f"AD/Metric:           {ad_metric}")
print(f"Next-Hop:            {next_hop}")
print(f"Last update:         {last_update}")
print(f"Outbound Interface:  {outbound_interface}")