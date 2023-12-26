import asyncio
import os

from dotenv import load_dotenv
from pyrogram import Client
from pyrogram.types import InputMediaPhoto

from constants import chat_id_dict, text

# constants
HALF_HOUR_RECYCLE = 1800
RECYCLE_TIME = 3600
MEDIA_GROUP = [
    InputMediaPhoto('s-size.jpg', caption=text),
    InputMediaPhoto('m-size.jpg'),
    InputMediaPhoto('2l-size.jpg'),
    InputMediaPhoto('caviat.jpg'),
    InputMediaPhoto('logo.jpg'),
]

load_dotenv()
api_id = os.getenv('M_API_ID')
api_hash = os.getenv('M_API_HASH')
maksim_id = os.getenv('MAKSIM_ID')


async def main():
    app = Client('my_account', api_id, api_hash)
    async with app:
        # Send a message to group listed in "chat_id_dict"
        await app.send_media_group(maksim_id, MEDIA_GROUP)
        await app.send_message(
            maksim_id,
            f'Проверка работы бота. Бот будет отправлять в 8, 14, и 17:30.'
            f' \n Пока только мне. Вот список всех групп {chat_id_dict}')


if __name__ == '__main__':
    asyncio.run(main())
