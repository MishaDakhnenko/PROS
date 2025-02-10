IP = '192.168.3.1'

octets = IP.split('.')
decimal_row = ''.join(f"{octet:<10}" for octet in octets)
binary_row = ''.join(f"{int(octet):08b}  " for octet in octets)
print(decimal_row)
print(binary_row)