import string

def caesar_cipher(text, shift, lang, decrypt=False):
    if lang == 'en':
        alphabet = string.ascii_lowercase
        alphabet_upper = string.ascii_uppercase
    elif lang == 'ru':
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        alphabet_upper = alphabet.upper()
    else:
        raise ValueError("Unsupported language")
    
    shift = -shift if decrypt else shift
    result = []
    
    for char in text:
        if char in alphabet:
            new_char = alphabet[(alphabet.index(char) + shift) % len(alphabet)]
        elif char in alphabet_upper:
            new_char = alphabet_upper[(alphabet_upper.index(char) + shift) % len(alphabet_upper)]
        else:
            new_char = char
        result.append(new_char)
    
    return ''.join(result)

def encrypt_words(text):
    words = text.split()
    encrypted_words = []
    
    for word in words:
        clean_word = ''.join(filter(str.isalpha, word))
        shift = len(clean_word)
        encrypted_word = caesar_cipher(word, shift, 'en')
        encrypted_words.append(encrypted_word)
    
    return ' '.join(encrypted_words)

# Запрос данных у пользователя
direction = input("Введите 'шифрование' или 'дешифрование': ").strip().lower()
language = input("Введите язык алфавита ('ru' для русского, 'en' для английского): ").strip().lower()
shift = int(input("Введите шаг сдвига: "))
text = input("Введите текст: ")

decrypt = direction == 'дешифрование'
result = caesar_cipher(text, shift, language, decrypt)
print("Результат:", result)

# Пример для шифрования каждого слова по длине слова
input_text = "Day, mice. \"Year\" is a mistake!"
output_text = encrypt_words(input_text)
print("Шифрованный текст:", output_text)
