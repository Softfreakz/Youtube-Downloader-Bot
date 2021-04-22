from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Visit My Master's Website", url="www.softfreakz.com")],
        [InlineKeyboardButton(
            "Contact My Master!", url="https://t.me/Softfreakz")]
    ])
    welcomed = f"Hey there Hello! <b>{message.from_user.first_name}</b>\n Send me any youtube link to get direct Telegram File 😉 \n My master Softfreakz ordered me to work only 12 Hours a day from 10 AM IST to 10 PM IST, for any help/support/report you can contact my master Softfreakz!"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
