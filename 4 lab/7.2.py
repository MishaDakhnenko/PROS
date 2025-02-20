def generate_trunk_config(trunk):
    """
    trunk - словарь trunk-портов, для которых необходимо сгенерировать конфигурацию.
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    trunk_template = [
        'switchport trunk encapsulation dot1q',
        'switchport mode trunk',
        'switchport trunk native vlan 999',
        'switchport trunk allowed vlan'
    ]
    
    config_list = []
    
    for port, vlans in trunk.items():
        config_list.append(f'interface {port}')
        
        # Добавляем команды из шаблона
        for line in trunk_template:
            if 'allowed vlan' in line:
                # Формируем строку с разрешенными VLAN
                config_list.append(f'{line} {",".join(map(str, vlans))}')
            else:
                config_list.append(line)
    
    return config_list


# Пример использования
trunk_dict = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}

# Генерация конфигурации
config = generate_trunk_config(trunk_dict)

# Вывод конфигурации
for command in config:
    print(command)
