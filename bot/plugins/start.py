from pyrogram import Filters, InlineKeyboardMarkup, InlineKeyboardButton

from ..config import Config
from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(Filters.private & Filters.command("start"))
async def start(c, m):
    
    if not await c.db.is_user_exist(m.chat.id):
        await c.db.add_user(m.chat.id)
        await c.send_message(
            Config.LOG_CHANNEL,
            f"New User [{m.from_user.first_name}](tg://user?id={m.chat.id}) started."
        )
    
    await m.reply_text(
        text=f"Hello {m.from_user.first_name}.\n\nI'm Night Screenshot. I can provide screenshots from your video files with out downloading the entire file (almost instantly). For more details check /help.",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('📣  Update Channel', url='https://t.me/joinchat/AAAAAE7LN2nDxp9EzkthPw'),
                    InlineKeyboardButton('📌  Leech Group', url='https://t.me/joinchat/OzszilP_FnoER7ip9FT9HA')
                ],
                [
                    InlineKeyboardButton('📡  Movie Channel', url='https://t.me/joinchat/AAAAAEz-e_b0qd105jGyuQ'),
                    InlineKeyboardButton('👮  Master', url='https://t.me/MuSkysM')
                ]
            ]
        )
    )
