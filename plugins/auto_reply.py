import asyncio, re
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from vars import FROM_GRP

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

lock = asyncio.Lock()

@Client.on_message(filters.chat(FROM_GRP) & ~filters.bot)
async def auto_reply(bot, message):
    try:
        reply = await message.reply_text('''𝙂𝘼𝙔𝙀𝙎 𝘼𝙇𝙇 𝙊𝙇𝘿+𝙉𝙀𝙒 𝙈𝙊𝙑𝙄𝙀 𝙁𝙄𝙇𝙀 🍿https://t.me/+HvkOX6x9RIJkYjZl''', reply_to_message_id=message.id)
        await asyncio.sleep(60)
        try:
            await asyncio.sleep(100)
            await reply.delete()
        except:
            pass
    except FloodWait as e:
        logger.warning(f"Got FloodWait.\n\nWaiting for {e.value} seconds.")
        await asyncio.sleep(e.value + 2)
        logger.info("Floodwait ended")
