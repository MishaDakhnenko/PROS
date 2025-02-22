def generate_trunk_config(trunk):
    """
    trunk - словарь trunk-портов, для которых необходимо сгенерировать конфигурацию, вида:
    { 'FastEthernet0/1': [10, 20], 'FastEthernet0/2': [11, 30], 'FastEthernet0/4': [17] }
    Возвращает словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе
    """
    trunk_template = [
        'switchport trunk encapsulation dot1q',
        'switchport mode trunk',
        'switchport trunk native vlan 999',
        'switchport trunk allowed vlan'
    ]
    
    config_dict = {}
    
    for port, vlans in trunk.items():
        port_config = []
        
        # Добавляем команды для каждого порта
        port_config.append(f'interface {port}')
        
        # Добавляем стандартные команды из шаблона
        for line in trunk_template:
            if 'allowed vlan' in line:
                # Формируем строку с разрешенными VLAN
                port_config.append(f'{line} {",".join(map(str, vlans))}')
            else:
                port_config.append(line)
        
        # Сохраняем команду конфигурации для этого порта в словарь
        config_dict[port] = port_config
    
    return config_dict


# Пример использования
trunk_dict = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}

# Генерация конфигурации
config = generate_trunk_config(trunk_dict)

# Вывод конфигурации
for port, commands in config.items():
    print(f'{port}:')
    for command in commands:
        print(f'  {command}')
