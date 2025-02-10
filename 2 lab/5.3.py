trunk_template = [
    'switchport trunk encapsulation dot1q',
    'switchport mode trunk',
    'switchport trunk allowed vlan'
]

fast_int = {
    'access': {
        '0/12': '10', '0/14': '11', '0/16': '17', '0/17': '150'
    },
    'trunk': {
        '0/1': ['add', '10', '20'],
        '0/2': ['only', '11', '30'],
        '0/4': ['del', '17']
    }
}

for intf, vlan_data in fast_int['trunk'].items():
    action, *vlans = vlan_data
    print(f'interface FastEthernet{intf}')
    for command in trunk_template:
        if command.endswith('allowed vlan'):
            if action == 'add':
                print(f'    {command} add {" ".join(vlans)}')
            elif action == 'del':
                print(f'    {command} remove {" ".join(vlans)}')
            elif action == 'only':
                print(f'    {command} {" ".join(vlans)}')
        else:
            print(f'    {command}')