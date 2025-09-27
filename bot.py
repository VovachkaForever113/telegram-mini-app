import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup

API_TOKEN = "7171819867:AAFpVc41Ab9YCOlY05xqVK17F5KgfhAZ81M"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# /start команда
@dp.message(F.text == "/start")
async def start_cmd(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="Открыть мини-приложение",
                web_app=WebAppInfo(url="https://vovachkaforever113.github.io/telegram-mini-app/")
            )]
        ]
    )
    await message.answer("Привет! Жми кнопку 👇", reply_markup=keyboard)

# Приём данных из мини-приложения
@dp.message(F.web_app_data)
async def web_app_data_handler(message: types.Message):
    data = message.web_app_data.data
    await message.answer(f"Я получил из мини-приложения: {data}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
