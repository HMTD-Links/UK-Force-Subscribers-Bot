async def admin_check(bot, msg, user_id=None, callback_query=None):
    if not user_id:
        user_id = msg.from_user.id
    bot_id = (await bot.get_me()).id
    if msg.chat.type not in ["supergroup", "group"]:
        await msg.reply("<b>This Command Can Only be Used in Groups !</b>", quote=True)
        return False
    chat_member = await msg.chat.get_member(user_id)
    bot_chat_member = await msg.chat.get_member(bot_id)
    if bot_chat_member.status != "administrator":
        text = "<b>Please make me Admin and then try Again !</b>"
        if callback_query:
            await callback_query.answer(text, show_alert=True)
        else:
            await msg.reply(text)
        return False
    if chat_member.status not in ("creator", "administrator"):
        text = "<b>This Command is only for Admins !</b>"
        if callback_query:
            await callback_query.answer(text, show_alert=True)
        else:
            await msg.reply(text)
        return False
    return True
