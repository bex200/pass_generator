from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import asyncio
from bot_token import TOKEN


bot = Bot (token = TOKEN)
dp = Dispatcher()


share_contact_keyboard_button = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Share your contact", request_contact=True),
            KeyboardButton(text="Test Button")]
    ],
    resize_keyboard=True
)


@dp.message(Command(commands=["start"]))
async def start_command_handler(message: Message):
    print(message.chat.id)
    print(message.from_user.username)
    print(message.text)

    user_id = message.from_user.id
    user_name = message.from_user.username
    await message.answer(f"Hello, {user_name or 'friend'}! Your ID is {user_id}",
                         reply_markup=share_contact_keyboard_button)


@dp.message(Command(commands=["end"]))
async def end_command_handler(message: Message):
    user_name = message.from_user.username
    await message.answer(f"Good bye, my dear  {user_name or 'friend'}! See you next time!")


@dp.message()
async def handle_any_message(message: Message):
    print(message.text)
    await message.reply(text=message.text )



async def main():
    print ("Bot is running. Press Ctrl+C for stopping  ")
    await  dp.start_polling(bot)


asyncio.run(main())
