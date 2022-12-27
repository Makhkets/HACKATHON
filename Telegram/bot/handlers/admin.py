
import config

from main import dp, bot
from state.default_state import *
from keyboards.kb import *

import requests

import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor


@dp.message_handler(text="Название", state="*")
async def start(message: types.Message, state: FSMContext):
    """
    Обычный handler для администраторов
    """
    
    await state.finish()
    if message.from_user.id in config.ADMINS:
        pass
    else: await message.answer("❌ Обойти защиту не получилось :)")



@dp.callback_query_handler(text_startswith="Каллбэк", state="*")
async def find(call: types.CallbackQuery, state: FSMContext):
    """
    handler для инлайн кнопок
    """