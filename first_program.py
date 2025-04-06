import random

num = random.randint(1, 100)
user_num = int(input("Введите число от 0 до 100        "))

while user_num in range(0, 101):
    if user_num > num:
        print("Слишком много, попробуйте еще раз")
        user_num = int(input("Введите число от 0 до 100        "))
    elif user_num < num:
        print("Слишком мало, попробуйте еще раз")
        user_num = int(input("Введите число от 0 до 100        "))
    elif user_num == num:
        print("Вы угадали, поздравляем!")
        break
