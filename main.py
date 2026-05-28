import os
import asyncio
from datetime import datetime, timedelta

from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session = os.getenv("STRING_SESSION")

client = TelegramClient(StringSession(session), api_id, api_hash)

# 🔥 اختلاف دستی (UTC + 4:30 برای کابل)
OFFSET_HOURS = 4
OFFSET_MINUTES = 30

async def run():
    await client.start()

    while True:
        utc_now = datetime.utcnow()

        local_time = utc_now + timedelta(
            hours=OFFSET_HOURS,
            minutes=OFFSET_MINUTES
        )

        now = local_time.strftime("%H:%M")

        name = f"⇢ ˗ˏˋ ᗩᗷOᒪᖴᗩᘔᒪ ࿐ྂ | 🕒 {now}"
        bio = f"⚡ Online | {now}"

        await client(UpdateProfileRequest(
            first_name=name,
            about=bio
        ))

        print("Updated:", now)

        await asyncio.sleep(60)

with client:
    client.loop.run_until_complete(run())
