MAC = 'AAAA:BBBB:CCCC'
binary_mac = ''.join(f"{int(part, 16):016b}" for part in MAC.split(':'))
print(binary_mac)