import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
chars = ""
options_Y = ["д", "Д", "y", "Y", "Yes", "Да"]
options_N = ["н", "Н", "n", "N", "No", "Нет"]

cntPw = input("Укажите количество паролей для генерации:")
lenPw = input("Укажите длину одного пароля:")
digOn = input("Включать ли цифры 0123456789? (да/нет)")
ABCon = input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да/нет)")
abcOn = input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (да/нет)")
chOn = input("Включать ли символы !#$%&*+-=?@^_? (да/нет)")
excOn = input("Исключать ли неоднозначные символы il1Lo0O? (да/нет)")
if digOn in options_Y:
    chars += digits
if ABCon in options_Y:
    chars += uppercase_letters
if abcOn in options_Y:
    chars += lowercase_letters
if chOn in options_Y:
    chars += punctuation
if chOn in options_Y:
    chars = chars.replace("i", "")
    chars = chars.replace("l", "")
    chars = chars.replace("1", "")
    chars = chars.replace("L", "")
    chars = chars.replace("o", "")
    chars = chars.replace("0", "")
    chars = chars.replace("O", "")


def generate_password(lenPw, chars):
    length = int(lenPw)
    password = ""
    for j in range(length):
        password += random.choice(chars)
    return password


for _ in range(int(cntPw)):
    print(*generate_password(lenPw, chars), sep="")
