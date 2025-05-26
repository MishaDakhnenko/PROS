# Пример содержимого файла ospf.txt:
# O    10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0

# Открываем файл ospf.txt для чтения
with open('ospf.txt', 'r') as file:
    # Проходим по каждой строке в файле
    for line in file:
        # Удаляем лишние пробелы и разделяем строку на слова
        line = line.strip().split()

        # Извлекаем необходимые части строки
        prefix = line[1]
        ad_metric = line[2].strip('[]')
        next_hop = line[4].strip(',')
        last_update = line[5].strip(',')
        outbound_interface = line[6]

        # Выводим информацию в нужном формате
        print(f"Protocol: OSPF")
        print(f"Prefix: {prefix}")
        print(f"AD/Metric: {ad_metric}")
        print(f"Next-Hop: {next_hop}")
        print(f"Last update: {last_update}")
        print(f"Outbound Interface: {outbound_interface}")
        print()
