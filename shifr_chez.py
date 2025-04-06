# Функция шифра Цезаря
def cesar(char, shift):
    # Заменяем ё на е и Ё на Е перед обработкой
    if char == 'ё':
        char = 'е'
    elif char == 'Ё':
        char = 'Е'

    char_code = ord(char)
    
    # Определяем диапазон и количество букв в алфавите
    if 65 <= char_code <= 90:  # Заглавные английские буквы
        start = 65
        end = 90
        alphabet_size = 26
    elif 97 <= char_code <= 122:  # Строчные английские буквы
        start = 97
        end = 122
        alphabet_size = 26
    elif 1040 <= char_code <= 1071:  # Заглавные русские буквы (без ё)
        start = 1040
        end = 1071
        alphabet_size = 32
    elif 1072 <= char_code <= 1103:  # Строчные русские буквы (без ё)
        start = 1072
        end = 1103
        alphabet_size = 32
    elif char == 'е':  # Обработка для ё (строчная)
        start = 1072
        end = 1103
        alphabet_size = 32
        char_code = ord('е')  # Устанавливаем код для 'е'
    elif char == 'Е':  # Обработка для Ё (заглавная)
        start = 1040
        end = 1071
        alphabet_size = 32
        char_code = ord('Е')  # Устанавливаем код для 'Е'
    else:
        return char  # Возвращаем символ без изменений, если это не буква

    # Вычисляем новый символ
    new_char_code = start + (char_code - start + shift) % alphabet_size
    return chr(new_char_code)


# Основная программа
print('Введите текст для шифрования:')
text = input()
print('На какую величину будем делать сдвиг? Ввод значения с МИНУСОМ - дешифрует текст!')
shift = int(input())

# Обрабатываем текст
result = ''
for char in text:
    result += cesar(char, shift)

print('Результат:', result)
