from aiogram import types

import config


def mainkb(user_id):
    """ 
    Обычная клавиатура
    """
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("Пользователь")

    if user_id in config.ADMINS:
        """
        Клавиатура для админов
        """
        kb.row("Админ")

    return kb

def department():
    """
    Инлайн клавиатура
    """
    inline_kb_full = types.InlineKeyboardMarkup()
    inline_kb_full.row(types.InlineKeyboardButton("Название кнопки", callback_data="Каллбэк"))
    return inline_kb_full

