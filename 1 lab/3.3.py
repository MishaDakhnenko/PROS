command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

vlans1 = set(command1.split()[-1].split(','))
vlans2 = set(command2.split()[-1].split(','))

common_vlans = sorted(map(int, vlans1 & vlans2))
print(common_vlans)