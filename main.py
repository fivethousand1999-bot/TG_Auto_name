import os
import asyncio
from datetime import datetime
import pytz

from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest

# ===== ENV =====
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session = os.getenv("STRING_SESSION")

# ===== TIMEZONE =====
tz = pytz.timezone("Asia/Kabul")

# ===== CLIENT =====
client = TelegramClient(StringSession(session), api_id, api_hash)

async def run():
    await client.start()

    while True:
        # زمان دقیق منطقه خودت
        now = datetime.now(tz).strftime("%H:%M")

        name = f"⇢ ˗ˏˋ ᗩᗷOᒪᖴᗩᘔᒪ ࿐ྂ  | {now}"
        bio = f"⚡ Online | {now}"

        await client(UpdateProfileRequest(
            first_name=name,
            about=bio
        ))

        print("Updated:", now)

        # جلوگیری از محدودیت تلگرام
        await asyncio.sleep(60)

with client:
    client.loop.run_until_complete(run())
