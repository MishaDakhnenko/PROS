def generate_access_config(access, psecurity=False):
    """
    access - словарь access-портов, для которых необходимо сгенерировать конфигурацию, вида:
    { 'FastEthernet0/12': 10, 'FastEthernet0/14': 11, 'FastEthernet0/16': 17 }
    psecurity - контролирует, нужна ли настройка Port Security. По умолчанию значение False.
                Если значение True, то настройка выполняется с добавлением шаблона port_security.
                Если значение False, то настройка не выполняется.
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    access_template = [
        'switchport mode access',
        'switchport access vlan',
        'switchport nonegotiate',
        'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]
    
    port_security = [
        'switchport port-security maximum 2',
        'switchport port-security violation restrict',
        'switchport port-security'
    ]
    
    config_list = []
    
    for port, vlan in access.items():
        config_list.append(f'interface {port}')
        for line in access_template:
            if 'vlan' in line:
                config_list.append(f'{line} {vlan}')
            else:
                config_list.append(line)
        
        # Если psecurity=True, добавляем настройки для Port Security
        if psecurity:
            config_list.extend(port_security)
    
    return config_list

# Пример использования
access_dict = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17,
    'FastEthernet0/17': 150
}

# Генерация конфигурации без port security
config_no_security = generate_access_config(access_dict, psecurity=False)
print("Конфигурация без Port Security:")
for line in config_no_security:
    print(line)

# Генерация конфигурации с port security
config_with_security = generate_access_config(access_dict, psecurity=True)
print("\nКонфигурация с Port Security:")
for line in config_with_security:
    print(line)
