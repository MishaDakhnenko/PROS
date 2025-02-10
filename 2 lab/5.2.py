mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
mac_cisco = []

for address in mac:
    mac_cisco.append(address.replace(":", "."))

print(mac_cisco)
