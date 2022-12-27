
import config

from main import dp, bot
from state.default_state import *
from keyboards.kb import *

import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


@dp.message_handler(text="/start", state="*")
async def start(message: types.Message, state: FSMContext):
    await state.finish()
    text = f"Добрый день, <code>{message.from_user.first_name}</code>" \
            "Мы рады приветствовать Вас в чат-боте\n" \
            "<b>«НАЗВАНИЕ»!</b>\n\n" \
            "Для выбора интересующего вас раздела воспользуйтесь кнопками из меню ниже 👇\n\n" \
            "👁 Если вы не видите внизу кнопки меню, нажмите квадрат с 4-мя точкам правее окна ввода сообщений. ✉"
    
    await message.answer_photo(photo="Логотип бота",
                               caption=text,
                               reply_markup=mainkb(message.from_user.id))
