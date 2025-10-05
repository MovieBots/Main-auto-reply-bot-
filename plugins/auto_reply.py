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
        reply = await message.reply_text('''Y͜͡o͜͡u͜͡r͜͡ m͜͡o͜͡v͜͡e͜͡ i͜͡s͜͡ i͜͡n͜͡ m͜͡y͜͡ p͜͡r͜͡o͜͡f͜͡i͜͡l͜͡e͜͡ p͜͡l͜͡e͜͡a͜͡s͜͡e͜͡ c͜͡h͜͡a͜͡k͜͡ m͜͡y͜͡ b͜͡i͜͡o͜͡
''', reply_to_message_id=message.id)
        await asyncio.sleep(60)
        try:
            await asyncio.sleep(10)
            await reply.delete()
        except:
            pass
    except FloodWait as e:
        logger.warning(f"Got FloodWait.\n\nWaiting for {e.value} seconds.")
        await asyncio.sleep(e.value + 2)
        logger.info("Floodwait ended")
