import os
import asyncio
from datetime import datetime
import pytz

from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session = os.getenv("STRING_SESSION")

tz = pytz.timezone("Asia/Kabul")

client = TelegramClient(StringSession(session), api_id, api_hash)

async def run():
    await client.start()

    while True:
        now = datetime.now(tz).strftime("%H:%M")

        name = f"⇢ ˗ˏˋ ᗩᗷOᒪᖴᗩᘔᒪ ࿐ྂ  | 🕒 {now}"
        bio = f"⚡ Online | {now}"

        # جدا جدا آپدیت کن (خیلی مهم)
        await client(UpdateProfileRequest(first_name=name))
        await client(UpdateProfileRequest(about=bio))

        print("Updated:", now)

        await asyncio.sleep(120)

with client:
    client.loop.run_until_complete(run())
