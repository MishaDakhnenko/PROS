def get_int_vlan_map(config_filename):
    access_ports = {}
    trunk_ports = {}

    with open(config_filename) as f:
        for line in f:
            if line.startswith("interface"):
                interface = line.split()[1]
            elif "switchport mode access" in line:
                access_mode = True
            elif "switchport access vlan" in line:
                vlan = int(line.split()[-1])
                access_ports[interface] = vlan
            elif "switchport trunk allowed vlan" in line:
                vlans = [int(vlan) for vlan in line.split()[-1].split(',')]
                trunk_ports[interface] = vlans

    return access_ports, trunk_ports

# Проверим работу функции на примере файла config_sw1.txt
access_ports, trunk_ports = get_int_vlan_map("config_sw1.txt")
print("Access Ports:", access_ports)
print("Trunk Ports:", trunk_ports)

