def generate_access_config(access):
    """
    access - словарь access-портов, для которых необходимо сгенерировать конфигурацию, вида:
    { 'FastEthernet0/12': 10, 'FastEthernet0/14': 11, 'FastEthernet0/16': 17 }
    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    """
    access_template = [
        'switchport mode access',
        'switchport access vlan',
        'switchport nonegotiate',
        'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]
    
    config_list = []
    
    for port, vlan in access.items():
        config_list.append(f'interface {port}')
        for line in access_template:
            if 'vlan' in line:
                config_list.append(f'{line} {vlan}')
            else:
                config_list.append(line)
    
    return config_list

# Пример использования
access_dict = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17,
    'FastEthernet0/17': 150
}

config = generate_access_config(access_dict)

# Выводим результат
for line in config:
    print(line)
