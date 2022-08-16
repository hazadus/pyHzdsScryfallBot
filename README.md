# pyHzdsScryfallBot

Telegram bot to access Scryfall API from chats.

[Here is a link to the Scryfall API documentation.](https://scryfall.com/docs/api)

## Dependencies
- Scryfall API:
- - `scrython` [Source code](https://github.com/NandaScott/Scrython)
- - `requests`
- Telegram API:
- - `telebot`
- - `pytelegrambotapi`


## References
- Scryfall API:
- - [Scrython - Examples from source code](https://github.com/NandaScott/Scrython/tree/main/examples)
- Telegram API:
- - [YouTube video](https://www.youtube.com/watch?v=CR7B19aJo9A)
- - [pyTelegramBotAPI Docs](https://pypi.org/project/pyTelegramBotAPI/)
- - [Telegram Bot API - Formatting options](https://core.telegram.org/bots/api#markdownv2-style)
- - [Inline Bots](https://core.telegram.org/bots/inline)
- - [Форматирование текста python telebot](https://ru.stackoverflow.com/questions/1034947/Форматирование-текста-python-telebot)

## Installation
- ...
- Change `loop = asyncio.get_event_loop` to `        loop = asyncio.new_event_loop() asyncio.set_event_loop(loop)` in `./scrython/foundation.py` to make Scrython calls work from bot.
