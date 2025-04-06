number_10 = int(input("Введите число для перевода из десятичной системы\n"))  # система счисления
n = input("Введите число для перевода в десятичную систему\n")  # число
osnova = int(input("Введите основание системы счисления\n"))  # система счисления
value = n[::-1]


def calc_syst(n, osnova, value):
    number = 0

    for i in range(len(value)):
        number += int(value[i]) * osnova**i
    return number

def convert_to(number_10, osnova):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if osnova > len(digits): return None
    result = ''
    while number_10 > 0:
        result = digits[number_10 % osnova] + result
        number_10 //= osnova
    return result.upper() 

if n != '':
    # перевод в десятичную
    print(f'Число {n} в десятичной системе: {int(n, osnova)}')

if number_10 != '':
    # перевод из десятичной   
    print(f'Число в {number_10} в системе счисления {osnova}: {convert_to(number_10, osnova)}')