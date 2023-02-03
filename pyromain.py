import asyncio

from pyrogram import Client
api_id = 9411854
api_hash = '499c76606cefdeadd4b1ece84a5a9932'

app = Client('pyro_account', api_id=api_id, api_hash=api_hash)

async def main():
    msg_link = 'https://t.me/turonworld/2398'
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

        if msg.media_group_id:
            await app.copy_media_group('me',from_chat_id=msg_link[0],message_id=int(msg_link[1]), captions=text)
        else:
            await app.copy_message('me', from_chat_id=msg_link[0], message_id=int(msg_link[1]), caption=text)
asyncio.run(main())