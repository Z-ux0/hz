import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

session = vk_api.VkApi(token="xxx")


def send_message(user_id, message):
    session.method("messages.send", {
        "user_id": user_id,
        "message": message,
        "random_id": 0
    })

for event in VkLongPoll(session).listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        text = event.text.lower()
        user_id = event.user_id

        if text == "команды":
            send_message(user_id, "Мои команды:\n\n🌍 Информация:\n᠌᠌ ᠌ ᠌᠌ ᠌ ᠌᠌ ᠌ ᠌᠌🎮 Сервера\n᠌᠌ ᠌ ᠌᠌ ᠌ ᠌᠌ ᠌ ᠌👾 Дискорд\n᠌᠌ ᠌ ᠌᠌ ᠌ ᠌᠌ ᠌ ᠌💠 Сайт")

        if text == "сервера":
            send_message(user_id, "🎮 Наши официальные сервера\n\n🪓 » MANIAC: 46.174.49.227:27015\n🔫 » PUBLIC: 37.18.21.234:27015\n🏹 » AWP: 193.19.119.53:27066")
        
        if text == "дискорд":
            send_message(user_id, "👾 Дискорд сообщество — https://discord.gg/3WvafuWpT9")
        
        if text == "сайт":
            send_message(user_id, "💠 Сайт с автодонатом — spyllonnycs.ru")