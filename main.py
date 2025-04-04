import asyncio
from telethon import TelegramClient, events
import os

client = TelegramClient('alert_bot', api_id=os.getenv("APIID"),
                        api_hash=os.getenv("APIHASH"))


async def start_bot():
    await client.start(bot_token=os.getenv("BOT_TOKEN"))

    @client.on(events.NewMessage(pattern=r"@all"))
    async def mention_all(event):
        chat_id = event.chat_id

        participants = await client.get_participants(chat_id)

        mentions = []
        for user in participants:
            if user.username:
                mentions.append(f"@{user.username}")
            else:
                mentions.append(f"[{user.first_name}](tg://user?id={user.id})")

        chunk_size = 10
        for i in range(0, len(mentions), chunk_size):
            text = " ".join(mentions[i:i + chunk_size])
            await event.reply(text)

    await client.run_until_disconnected()

asyncio.run(start_bot())
