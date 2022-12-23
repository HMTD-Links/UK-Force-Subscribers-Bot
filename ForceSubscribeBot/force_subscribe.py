from pyrogram import Client, filters
from pyrogram.types import Message
from ForceSubscribeBot.admin_check import admin_check
from pyrogram.errors import UsernameInvalid, PeerIdInvalid, UserNotParticipant
from ForceSubscribeBot.database.chats_sql import get_force_chat, change_force_chat, get_only_owner


@Client.on_message(filters.text & filters.incoming & filters.command(["fsub", "forcesubscribe"]))
async def fsub(bot, msg: Message):
    chat_id = msg.chat.id
    bot_id = (await bot.get_me()).id
    success = await admin_check(bot, msg)
    if not success:
        return
    if len(msg.command) == 1:
        force_chat = await get_force_chat(chat_id)
        if force_chat:
            chat = await bot.get_chat(force_chat)
            mention = '@' + chat.username if chat.username else f"{chat.title} ({chat.id})"
            await msg.reply(f"<b>Current Force Subscribe Chat is : {mention} \n\nCould be Changed Using</b> `/forcesubscribe new_chat_id`")
        else:
            await msg.reply("<b>No Force Subscribers Chat Set! \n\nCould be set Using</b> `/forcesubscribe chat_id`")
    else:
        creator = True if (await bot.get_chat_member(chat_id, msg.from_user.id)).status == "creator" else False
        only_owner = await get_only_owner(chat_id)
        if only_owner and not creator:
            await msg.reply("Only owner can change Force Subscribe chat in this chat.")
            return
        to_be_chat = msg.command[1]
        try:
            bot_chat_member = await bot.get_chat_member(to_be_chat, bot_id)
        except (UsernameInvalid, PeerIdInvalid):
            await msg.reply(
                "<b>Unsuccessful :( \n\nPossible reasons could be: \n\n</b>"
                "<b>1) I haven't been Added there. \n</b>"
                "<b>2) The Provided chat_id/username is Invalid. \n</b>"
                "<b>3) I have been demoted there. \n</b>"
                "<b>4) You have Provided link Instead of username/chat_id. \n\n</b>"
                "<b>Please re-check all three and try Again!</b>"
                "<b>If the problem persists, try demoting and promoting again.</b>"
            )
            return
        except ValueError as e:
            await msg.reply(f"<b>Seriously? \n\n{str(e)}</b>")
            return
        except UserNotParticipant:
            await msg.reply(f"<b>I haven't been Added there.</b>")
            return
        if bot_chat_member.status == "administrator":
            to_be_chat_id = (await bot.get_chat(to_be_chat)).id
            await change_force_chat(chat_id, to_be_chat_id)
            await msg.reply("<b>Successful. Now I'll Mute People who haven't Joined that chat. \n\nUse /settings to Change Settings.</b>")
        else:
            await msg.reply("<b>Please Make me Admin there and Then try Again!</b>")
