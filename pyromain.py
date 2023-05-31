import asyncio

from pyrogram import Client

api_id = 0
api_hash = ''

app = Client('pyro_account', api_id=api_id, api_hash=api_hash)
with open('link.txt', 'r') as file:
    link = file.readline().strip()
channel = link
if channel.startswith('https://'):
    channel = channel[8:]
if channel.startswith('t.me/'):
    channel = channel[5:]
if channel.startswith('c/'):
    channel = channel[2:]
async def main():
    msg_link = input('Введите ссылку на сообщение: ')
    if msg_link.startswith('https://'):
        msg_link = msg_link[8:]
    if msg_link.startswith('t.me/'):
        msg_link = msg_link[5:]
    if msg_link.startswith('c/'):
        msg_link = msg_link[2:]
    msg_link = msg_link.split('/')
    async with app:
        msg = await app.get_messages(chat_id=msg_link[0], message_ids=int(msg_link[1]))
        if msg.caption:
            text = msg.caption
        else:
            text = msg.text
        text = text.replace('https://', '')
        text = text.replace('telegram.me', '.me')
        text = text.replace('t.me', '.me')
        start = text.find('.me')
        stop = text.find('.me')
        if stop != -1:
            for i in range(text.find('.me'), len(text)):
                if text[i] == ' ':
                    break
                stop = i
            text = text[:start] + link + text[stop + 1:]
        if msg.media_group_id:
            await app.copy_media_group(channel, from_chat_id=msg_link[0], message_id=int(msg_link[1]), captions=text)
        elif msg.media:
            await app.copy_message(channel, from_chat_id=msg_link[0], message_id=int(msg_link[1]), caption=text)
        else:
            await app.send_message(channel, text=text)


asyncio.run(main())
