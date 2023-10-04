# Вспомогательные функции
from time import asctime


colors = {"black": 30,
          "red": 31,
          "green": 32,
          "yellow": 33,
          "blue": 34,
          "purple": 35,
          "turquoise": 36,
          "grey": 37,
          "white": 38}


# Объявление события
def addEvent(text_event: str, message=None, type_chat="...", id_user=0, first_name="...", last_name="...",
             username="...", start_string="", end_string="", color_consol="white"):
    if message:
        type_chat = message.chat.type if type_chat == "..." else type_chat
        first_name = message.from_user.first_name if first_name == "..." else first_name
        last_name = message.from_user.last_name if last_name == "..." else last_name
        username = message.from_user.username if username == "..." else username
        id_user = message.from_user.id if not id_user else id_user

    event = f"{start_string}//" \
            f"{type_chat}//" \
            f"{asctime()}//" \
            f"{id_user}//" \
            f"{first_name}//" \
            f"{last_name}//" \
            f"{username}//" \
            f"'{text_event}'" \
            f"{end_string}"

    # Добавление в БД действия
    # add_new_event_to_database(type_chat, text_event, asctime(), id_user, first_name, last_name, username,
    # start_string, end_string)
    print(f"\033[{str(colors[color_consol])}m{event}")
