import sys

ignore = ['duplex', 'alias', 'Current configuration']

def should_ignore(line):
    for word in ignore:
        if word in line:
            return True
    return False

def process_config_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if not line.startswith('!') and not should_ignore(line):
                    print(line.strip())
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python script.py config_sw1.txt")
    else:
        process_config_file(sys.argv[1])
