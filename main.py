import asyncio
from aiogram import Bot, Dispatcher, F, types
from config import BOT_TOKEN
from brain import get_ai_answer

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(F.text == "/start")
async def start_cmd(message: types.Message):
    await message.answer(
        "Привіт чувак! Я твій ШІ-коуч по Секаю. \n"
        "Напиши назву пісні, і я розкладу її по фактах."
    )

@dp.message(F.text)
async def handle_all_messages(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    
    answer = await get_ai_answer(message.text)
    
    await message.answer(answer)

async def main():
    print("Бот запущений (Архітектура: LLM-Centeric)...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот вимкнений.")