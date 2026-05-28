import os
import asyncio
from datetime import datetime

from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session = os.getenv("STRING_SESSION")

client = TelegramClient(StringSession(session), api_id, api_hash)

async def run():
    await client.start()

    while True:
        now = datetime.now().strftime("%H:%M")

        await client(UpdateProfileRequest(
            first_name=f"🕒 {now}",
            about=f"⇢ ˗ˏˋ ᗩᗷOᒪᖴᗩᘔᒪ ࿐ྂ | {now}"
        ))

        print("updated:", now)

        await asyncio.sleep(120)

with client:
    client.loop.run_until_complete(run())
