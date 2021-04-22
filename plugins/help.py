from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"No one can help you, except yourself!!! 😉 /n For any issues/support/error report contact my master Softfreakz!"
    await message.reply_text(helptxt)
