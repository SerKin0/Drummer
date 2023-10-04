from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.misc.util import addEvent


def creatInlineButtonIndex(buttons: list, indices: list, row_width=2, add_last=0):
    markup = InlineKeyboardMarkup(row_width=row_width)
    if add_last > len(buttons):
        addEvent(f"Кол-во add кнопок ({add_last}) больше количества кнопок ({len(buttons)})",
                 start_string="Error Inline Keyboard", color_consol="red")
        return None
    elif len(buttons) != len(indices):
        addEvent(f"Кол-во кнопок ({len(buttons)}) не совпадает с количеством индексов ({len(indices)})",
                 start_string="Error Inline Keyboard", color_consol="red")
        return None
    else:
        # Добавление остальных кнопок (insert)
        for button, index in zip(buttons if add_last == 0 else buttons[:-add_last],
                                 indices if add_last == 0 else indices[:-add_last]):
            print(1, button, index)
            markup.insert(InlineKeyboardButton(button, callback_data=index))

        # Добавление последних отдельных кнопок (add)
        if add_last != 0:
            for button, index in zip(buttons[-add_last:], indices[-add_last:]):
                print(2, button, index)
                markup.add(InlineKeyboardButton(button, callback_data=index))

        return markup
