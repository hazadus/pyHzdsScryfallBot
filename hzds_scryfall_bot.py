import scrython
import requests
import time
import telebot
from datetime import datetime
import bot_token

BOT_NAME = '@HzdsScryfallBot'
IMAGE_SAVE_PATH = "./card_images"

bot = telebot.TeleBot(bot_token.TOKEN)


def save_image(path, image_url, file_name):
    response = requests.get(image_url)
    image_file_path = f'{path}/{file_name}.png'

    with open(image_file_path, 'wb') as file:
        file.write(response.content)

    return image_file_path


def query_scryfall(query):
    auto = ""
    answer = {
        "image_file_path": "",
        "card_description": " "
    }
    try:
        time.sleep(0.05)
        card = scrython.cards.Named(exact=query)
    except Exception:
        time.sleep(0.05)
        auto = scrython.cards.Autocomplete(q=query, query=query)

    if auto:
        answer['card_description'] = "Вы хотели найти "
        for item in auto.data():
            answer['card_description'] = answer['card_description'] + "[" + item + "]"
            answer['card_description'] = answer['card_description'] + "?"
    else:
        answer['card_description'] = f"<b>{card.name()}</b>\n<i>{card.rarity()}</i> from <i>{card.set_name()}</i>\n{card.mana_cost()}\n{card.oracle_text()}"
        answer['image_file_path'] = save_image(IMAGE_SAVE_PATH, card.image_uris(0, 'normal'), card.name())

    return answer


# любой текст
@bot.message_handler(content_types=['text'])
def text(message):
    if message.text[:len(BOT_NAME)] == BOT_NAME:
        print(datetime.now().strftime('>>> %d %b %Y %H:%M (') + str(message.chat.type) + " "
              + str(message.chat.id) + "): " + message.text)
        query = message.text[len(BOT_NAME) + 1:]
        scry_answer = query_scryfall(query)
        bot.reply_to(message, scry_answer['card_description'], parse_mode="HTML")
        if not scry_answer['image_file_path'] == "":
            card_image = open(scry_answer['image_file_path'], 'rb')
            bot.send_photo(message.chat.id, card_image)


while True:
    try:
        bot.polling(none_stop=True)
        # ConnectionError and ReadTimeout because of possible timout of the requests library
        # maybe there are others, therefore Exception
    except Exception:
        time.sleep(15)
