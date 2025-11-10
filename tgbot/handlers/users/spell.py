from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from tgbot.misc import check_word, to_cyrillic, to_latin

spell_router = Router()


@spell_router.message(CommandStart())
async def user_start(message: Message):
    await message.reply("uz_imlo Botiga Xush Kelibsiz!")

@spell_router.message()
async def check_imlo(message: Message) -> None:
    text = message.text

    if text.isascii():
        text = to_cyrillic(text)
        
    result = check_word(text)

    if message.text.isascii():
        text = to_latin(text)
    
    if result['available']:
        response = f"{text.capitalize()}\t✅"
    else: 
        if message.text.isascii():
            matches = [to_latin(text) for text in result['matches']]
        else:
            matches = [text for text in result['matches']]

        if matches:
            response = f"❌\t{text.capitalize()}\n"
        else:
            response = f"{text.capitalize()}\t⁉️\n"

        for text in matches:
            response += f"✅\t{text.capitalize()}\n"

    await message.reply(response)