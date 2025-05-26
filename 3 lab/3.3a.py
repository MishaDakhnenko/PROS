def process_cam_table(filename):
    entries = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.split()
                # Проверяем, содержит ли строка MAC-адрес
                if len(parts) == 4 and parts[1].count('.') == 2:
                    vlan = parts[0]
                    mac_address = parts[1]
                    interface = parts[3]
                    entries.append((int(vlan), mac_address, interface))
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    # Сортировка по номеру VLAN
    entries.sort()

    for vlan, mac_address, interface in entries:
        print(f"{vlan}\t{mac_address}\t{interface}")


if __name__ == "__main__":

    process_cam_table('CAM_table.txt')
