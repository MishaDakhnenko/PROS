def generate_access_config(access, psecurity=False):
    """
    access - словарь access-портов, для которых необходимо сгенерировать конфигурацию, вида:
    { 'FastEthernet0/12': 10, 'FastEthernet0/14': 11, 'FastEthernet0/16': 17 }
    psecurity - контролирует, нужна ли настройка Port Security. По умолчанию значение False.
                Если значение True, то настройка выполняется с добавлением шаблона port_security.
                Если значение False, то настройка не выполняется.
    Функция возвращает словарь:
    ключи: имена интерфейсов (вида 'FastEthernet0/1')
    значения: список команд, которые надо выполнить на этом интерфейсе
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
    
    config_dict = {}
    
    for port, vlan in access.items():
        port_config = []
        
        # Добавляем команды для порта
        port_config.append(f'interface {port}')
        
        for line in access_template:
            if 'vlan' in line:
                port_config.append(f'{line} {vlan}')
            else:
                port_config.append(line)
        
        # Если psecurity=True, добавляем настройки для Port Security
        if psecurity:
            port_config.extend(port_security)
        
        # Сохраняем список команд для этого порта в словарь
        config_dict[port] = port_config
    
    return config_dict

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
for port, commands in config_no_security.items():
    print(f'{port}:')
    for command in commands:
        print(f'  {command}')

# Генерация конфигурации с port security
config_with_security = generate_access_config(access_dict, psecurity=True)
print("\nКонфигурация с Port Security:")
for port, commands in config_with_security.items():
    print(f'{port}:')
    for command in commands:
        print(f'  {command}')
