import random
word_list = [
    "яблоко", "дом", "солнце", "река", "книга",
    "стол", "стул", "кошка", "собака", "цветок",
    "машина", "город", "лес", "гора", "море",
    "окно", "дверь", "часы", "лампа", "телефон",
    "ручка", "бумага", "хлеб", "молоко", "сахар",
    "чай", "кофе", "письмо", "картина", "музыка",
    "фильм", "игра", "дождь", "снег", "ветер",
    "птица", "рыба", "лист", "трава", "камень",
    "дорога", "поезд", "самолет", "автобус", "велосипед",
    "школа", "учитель", "ученик", "тетрадь", "карандаш"
]


def get_word():
    word = random.choice(word_list).upper()
    return word




def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def print_word(word_, list_):
    for c in word_:
        if c in list_:
            print(c, end=' ')
        else:
            print('_', end=' ')
    print()




def play(word):
    # тело функции
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    print('Давайте играть в угадайку слов!') 
    print(display_hangman(tries))
    print(word_completion)
    while True:
        letter = input('Введите букву или слово \n').upper()
        if not letter.isalpha():
            print('Ошибка ввода, попробуй еще раз')
            continue
        if letter in guessed_words or letter in guessed_letters:
            print('Уже было')
            continue
        if len(letter) > 1:
            if letter == word:
                print('Поздравляем, вы угадали слово! Вы победили!')
                break
            else:
                guessed_letters.append(letter)
                tries -= 1
                print(f'Не верно, осталось попыток {tries}')
                print(display_hangman(tries))
                print_word(word, guessed_letters)
        
        if letter in word:
            guessed_letters.append(letter)
            for c in word:
                if c not in guessed_letters:
                    print('Угадали букву')
                    print_word(word, guessed_letters)
                    guessed = False
                    break
                guessed = True
            if guessed:    
                print_word(word, guessed_letters)
                print('Поздравляем, вы угадали слово! Вы победили!')
                break
        else:
            guessed_letters.append(letter)
            tries -= 1
            print(f'Не верно, осталось попыток {tries}')
            print(display_hangman(tries))
            print_word(word, guessed_letters)
        if tries == 0:
            print(f'Вы не смогли угадать слово: {word}')
            break

play(get_word())    

