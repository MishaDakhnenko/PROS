def get_int_vlan_map(config_sw2):
    access_ports = {}
    trunk_ports = {}

    with open(config_sw2) as f:
        for line in f:
            if line.startswith("interface"):
                interface = line.split()[1]
                access_mode = False
            elif "switchport mode access" in line:
                access_mode = True
            elif "switchport access vlan" in line and access_mode:
                vlan = int(line.split()[-1])
                access_ports[interface] = vlan
            elif "switchport trunk allowed vlan" in line:
                vlans = [int(vlan) for vlan in line.split()[-1].split(',')]
                trunk_ports[interface] = vlans
            elif access_mode and "duplex auto" in line and interface not in access_ports:
                access_ports[interface] = 1

    return access_ports, trunk_ports

# Проверим работу функции на примере файла config_sw2.txt
access_ports, trunk_ports = get_int_vlan_map("config_sw2.txt")
print("Access Ports:", access_ports)
print("Trunk Ports:", trunk_ports)
