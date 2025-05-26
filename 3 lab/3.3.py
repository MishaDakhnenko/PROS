def process_cam_table(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.split()
                # Проверяем, содержит ли строка MAC-адрес
                if len(parts) == 4 and parts[1].count('.') == 2:
                    vlan = parts[0]
                    mac_address = parts[1]
                    interface = parts[3]
                    print(f"{vlan}\t{mac_address}\t{interface}")
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":

    process_cam_table('CAM_table.txt')
