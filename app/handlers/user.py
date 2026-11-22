import logging
from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.enums import ChatAction

from app.services.gemini import generate_text

router = Router()
logger = logging.getLogger(__name__)


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я готов к работе, задавай любой вопрос 😎")


@router.message(F.text)
async def handler_text_message(message: types.Message):
    await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)

    try:
        ai_response = await generate_text(message.text)

        for i in range(0, len(ai_response), 4096):
            await message.answer(ai_response[i:i+4096])

    except Exception as e:
        logger.error(f"Ошибка при обращении к Gemini: {e}")
        await message.answer("415 база ответьте...Нейросеть пока не отвечает (Проверь ВПН или попробуй чуть позже)")
