import datetime
import time

from pyrogram import Client
from pyrogram.types import InputMediaPhoto, InputMediaVideo


now = datetime.datetime.utcnow()
RECYCLE_TIME = 21600
# ivan
api_id = 21911363
api_hash = 'bb01dce613b6787528f15d56d0e2666d'
# maks
api_id = 29190901
api_hash = '11d78f5eaab6f231785f6260ead093c0'

app = Client('my_account', api_id, api_hash)

app.start()
# app.send_message(-696293374, 'че дел?')
# app.send_media_group(-696293374, [
while True:
    # if now.hour == 7:
    #     time.sleep(RECYCLE_TIME)
    #     app.send_message('me', 'еще не время')
    #     continue
    # app.send_media_group('me', [InputMediaVideo('test.mp4', caption='tew'),])
    app.send_message('me', 'еще не время')
    # app.send_media_group('me', [
    #     InputMediaPhoto('s-size.jpg',),
    #     InputMediaPhoto('m-size.jpg'),
    #     InputMediaPhoto('2l-size.jpg'),
    #     # InputMediaVideo('caviat.mp4', caption='tew'),
    #     InputMediaPhoto('caviat.jpg'),
    #     InputMediaPhoto('logo.jpg'),
    # ])
    time.sleep(RECYCLE_TIME)
app.stop() 

