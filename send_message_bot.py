import datetime
import logging
import time
import os

from dotenv import load_dotenv
from pyrogram import Client
from pyrogram.errors import BadRequest, Flood, SeeOther
from pyrogram.types import InputMediaPhoto

from constants import chat_id_array, text

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
# setup logging
logging.basicConfig(
    format='%(asctime)s, %(levelname)s, %(message)s',
    filename='logs.log',
    filemode='w'
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

load_dotenv()
api_id = os.getenv('I_API_ID')
api_hash = os.getenv('I_API_HASH')
maksim_id = os.getenv('MAKSIM_ID')

app = Client('my_account', api_id, api_hash)


def check_log_status():
    message = (next(app.get_chat_history(chat_id='me', limit=1)))
    if message.text == 'status':
        text = open('logs.log', 'r')
        try:
            app.send_message('me', text=text.read())
        except BadRequest:
            app.send_message('me', text='logs is empty.')

def get_chat_array(array=None):
    if not array:
        array = []
    for dialog in app.get_dialogs():
        if dialog.chat.id in chat_id_array:
            array.append(dialog.chat.title)
    return array


def send_media_message(to_adress, message):
    try:
        app.send_media_group(
                    to_adress,
                    message
                )

    except Flood:
        app.send_message('me', text='Происходит спам сообщений')
        app.stop()

    except BadRequest as error:
        logger.error(
            f'{datetime.datetime.utcnow().hour}, smth is wrong.{error}')
        app.send_message(
            maksim_id, text='что то сломалось, нужно починить.')

    except SeeOther as error:
        logger.error(
            f'{datetime.datetime.utcnow().hour}, smth is wrong.{error}')
        app.send_message(
            maksim_id, text='что то сломалось, нужно починить.')


def main():
    app.start()
    array = get_chat_array()
    while True:
        check_log_status()
        now = datetime.datetime.utcnow()
        if now.hour == 5 or now.hour == 11:
            send_media_message(maksim_id, MEDIA_GROUP)
            logger.debug(f'{now.hour}:{now.minute} all work well.')
            #
            app.send_message(
                maksim_id,
                f'Проверка работы бота. Бот будет отправлять в 8, 14, и 17:30.'
                f' \n Пока только мне. Вот список всех групп {array}')
            #
        elif now.hour == 14:
            time.sleep(HALF_HOUR_RECYCLE)
            send_media_message(maksim_id, MEDIA_GROUP)
            logger.debug(f'{now.hour}:{now.minute} all work well.')
            #
            app.send_message(
                maksim_id,
                f'Проверка работы бота. Бот будет отправлять в 8, 14, и 17:30.'
                f' \n Пока только мне. Вот список всех групп {array}')
            #
            time.sleep(HALF_HOUR_RECYCLE)
        else:
            logger.debug(f'{now.hour}:{now.minute}, i am waiting')
        time.sleep(RECYCLE_TIME)
    app.stop()


if __name__ == '__main__':
    main()
