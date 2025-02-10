CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
vlans = CONFIG.split()[-1].split(',')
print(vlans)