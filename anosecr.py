import asyncio
import aiocron
from telethon import TelegramClient, events

# Replace with your API ID and API hash
api_id = 26236995
api_hash = '7f235ff5ca650fcd8eff6c46c970ea47'

client = TelegramClient('user', api_id, api_hash).start()

# Define the specific sentence you want to trigger the auto-reply for
specific_sentence = "You have been matched with another user"

# These multi-line messages can contain any text, links, and emoji:
auto_reply_message_1 = """\
Aradhya Baliyan (F , 24 , Paid Girl, North Delhi)
300rs extreme squirt with fingering and boobs show
400rs 1 hr videocall full nude (on demand acts like cream on boobs,
700rs sex chat for 7 days
2220rs personal number message 'hi' on my id @abaliyan1 if interested.
"""

auto_reply_message_2 = """\
/new_chat
"""


@client.on(events.NewMessage(incoming=True))
async def handler(event):
    sender = await event.get_input_sender()
    if specific_sentence in event.message.message:
        await client.send_message(sender, auto_reply_message_1)
        await client.send_message(sender, auto_reply_message_2)

async def send_periodic_message():
    while True:
        try:
            await client.send_message('@Anonymous_Talk_Secret_Chat_Bot', '/new_chat')
        except Exception as e:
            print(f"Error sending message: {e}")
        await asyncio.sleep(60)  # 1 minutes

# Schedule the periodic message using aiocron
aiocron.crontab('*/1 * * * *', func=send_periodic_message)

# Run the client until disconnected
client.run_until_disconnected()



