import asyncio, re
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from vars import FROM_GRP

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@Client.on_message(filters.chat(FROM_GRP))
async def auto_reply(bot, message):
    if not message.from_user:
        return
    try:
        reply = await message.reply_text('''अपनी मूवी हमारे बायो में जो लिंक दी है वह आपको सब मूवी मिल जाएगी ज्वाइन फास्ट एंड एंजॉय करे

@Kajalsharma110
@Kajalsharma110''', reply_to_message_id=message.id)
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
    except Exception as e:
        logger.error(f"An error occurred: {e}")
