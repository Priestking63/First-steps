import random
import tkinter as tk
from tkinter import messagebox

# Список ответов
answers = [
    "Ёп, это сто пудов 😎",
    "Ну, типа, да, наверное 🤔",
    "Хз, спроси ещё раз, братан 🤷‍♂️",
    "Да ты чё, бля, забей 😤",
    "Дело в шляпе, чё уж там 🎩",
    "Скорее всего, да, но хз 🤨",
    "Отъебись, потом спроси 🙄",
    "Нет, бля, и не спорь 🚫",
    "Да тут даже думать не надо, конечно! 🤯",
    "Норм всё будет, расслабься 😌",
    "Бля, молчи, а то беда будет 🤫",
    "Нет, я ща проверил, херня это 🤥",
    "Да ты не парься, это точно ✅",
    "Ага, да 👍",
    "Собери мозги в кучу и спроси ещё раз 🧠",
    "Херня какая-то, не верю 🤨",
]

# Функция для генерации случайного ответа
def get_answer():
    random_answ = random.choice(answers)
    answer_label.config(text=random_answ)

# Функция для выхода из приложения
def exit_app():
    if messagebox.askyesno("Выход", "Хотите выйти из приложения?"):
        root.destroy()

# Создание основного окна
root = tk.Tk()
root.title("Магический шар")
root.geometry("400x300")

# Заголовок
title_label = tk.Label(root, text="МАГИЧЕСКИЙ ШАР", font=("Arial", 20))
title_label.pack(pady=10)

# Инструкция
instruction_label = tk.Label(root, text="ЗАДАЙ ВОПРОС И НАЖМИ", font=("Arial", 14))
instruction_label.pack(pady=10)

# Кнопка для получения ответа
ask_button = tk.Button(root, text="Получить ответ", command=get_answer, font=("Arial", 12))
ask_button.pack(pady=20)

# Метка для отображения ответа
answer_label = tk.Label(root, text="", font=("Arial", 14), wraplength=300)
answer_label.pack(pady=20)

# Кнопка для выхода
exit_button = tk.Button(root, text="Выход", command=exit_app, font=("Arial", 12))
exit_button.pack(pady=10)

# Запуск основного цикла
root.mainloop()