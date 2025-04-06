import random
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

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


# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_name = update.message.from_user.first_name
    await update.message.reply_text(f"Ну привет, {user_name}! Задавай свой вопрос.")


# Обработчик текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_input = update.message.text
    if user_input.lower() in ["да", "нет"]:
        if user_input.lower() == "да":
            await update.message.reply_text("Пизда")
            await update.message.reply_text("Задавай свой вопрос:")
        else:
            await update.message.reply_text("Ну и иди нахуй 💩")
    else:
        random_answ = random.choice(answers)
        await update.message.reply_text(random_answ)
        await update.message.reply_text("Еще вопросы есть? (да/нет)")


# Основная функция
def main() -> None:
    # Вставь сюда токен своего бота
    token = "7760675136:AAGXEFmyHE8-uAr5YcqaCSuofTJxcRsKcWg"

    # Создаем Application и передаем ему токен
    application = Application.builder().token(token).build()

    # Регистрируем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    # Запускаем бота
    application.run_polling()


if __name__ == "__main__":
    main()
