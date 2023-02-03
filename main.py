import telethon.utils
from telethon import TelegramClient
from telethon import functions
import re
'https://t.me/working_4ever/7'
api_id = 9411854
api_hash = '499c76606cefdeadd4b1ece84a5a9932'
client = TelegramClient('my_account', api_id, api_hash)

async def main():
    await client.connect()
    msg_link = input('Отправьте ссылку на сообщение: ')
    if msg_link.startswith('https://'):
        msg_link = msg_link[8:]
    if msg_link.startswith('t.me/'):
        msg_link = msg_link[5:]
    if msg_link.startswith('c/'):
        msg_link = msg_link[2:]
    msg_link = msg_link.split('/')

    msg = await client(functions.channels.GetMessagesRequest(msg_link[0], [int(msg_link[1])]))
    msg = msg.messages[0]
    text = msg.message
    urls = re.findall('(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)
    print(urls)
    try:
        await client.send_file('me', caption=text,file=msg.media)
    except:
        await client.send_message('me', message=text)

with client:
    client.loop.run_until_complete(main())
