import sys

ignore = ['duplex', 'alias', 'Current configuration']

def should_ignore(line):
    for word in ignore:
        if word in line:
            return True
    return False

def process_config_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line in infile:
                if not should_ignore(line):
                    outfile.write(line)
    except FileNotFoundError:
        print(f"Файл {input_filename} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python script.py config_sw1.txt")
    else:
        process_config_file(sys.argv[1], 'config_sw1_cleared.txt')
