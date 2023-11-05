import datetime
import logging
import time
import os

from dotenv import load_dotenv
from pyrogram import Client
from pyrogram.types import InputMediaPhoto

from constants import chat_id_array, text

HALF_HOUR_RECYCLE = 1800
RECYCLE_TIME = 3600
load_dotenv()

logging.basicConfig(
    format='%(asctime)s, %(levelname)s, %(message)s',
    filename='logs.log',
    filemode='w'
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
api_id = os.getenv('M_API_ID')
api_hash = os.getenv('M_API_HASH')
maksim_id = os.getenv('MAKSIM_ID')

app = Client('my_account', api_id, api_hash)
array = []

def get_chat_array():
    for dialog in app.get_dialogs():
            if dialog.chat.id in chat_id_array:
                array.append(dialog.chat.title)

def send_meessage():
    try:
        app.send_media_group(
                    maksim_id,
                    [
                        InputMediaPhoto('s-size.jpg', caption=text),
                        InputMediaPhoto('m-size.jpg'),
                        InputMediaPhoto('2l-size.jpg'),
                        InputMediaPhoto('caviat.jpg'),
                        InputMediaPhoto('logo.jpg'),
                    ]
                )
        app.send_message(
            maksim_id,
            f'Проверка работы бота. Бот будет отправлять в 8, 14, и 17:30. \n'
            f'Пока только мне. Вот список всех групп {array}')
    except:
        logger.error(f'{datetime.datetime.utcnow()}, smth is wrong.')
        app.send_message(
            maksim_id, text='что то сломалось, нужно починить.')
    else:
        logger.debug(f'{datetime.datetime.utcnow()} all work well.')

def main():
    app.start()
    get_chat_array()
    while True:
        now = datetime.datetime.utcnow().hour
        if now == 5 or now == 11:
            send_meessage()
        if now == 14:
            time.sleep(HALF_HOUR_RECYCLE)
            send_meessage()
            time.sleep(HALF_HOUR_RECYCLE)
        logger.debug(f'{now}, i am waiting')
        time.sleep(RECYCLE_TIME)
    app.stop()

if __name__ == '__main__':
    main()
