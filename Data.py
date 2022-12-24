from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
<b>Hello 👋🏻 {},

Welcome to {},

I can Force your Group's Users to Join a Particular Chat. 
The chat can be a Group or Channel. It can be Private or Public.

Use below buttons to learn more !

By @UK_Studios_Official</b>
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Home 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ Our Movie Request Group ✨", url="https://t.me/+hRqnoWzkKXtiYjBl")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("📢 Update Channel", url="https://t.me/UK_Studios_Official")],
        [InlineKeyboardButton("👥 Support Group 👥", url="https://t.me/HMTD_Discussion_Group")],
    ]

    # Help Message
    HELP = """
**1) Add me as Admin to a Group.

2) Add me to the particular chat as Admin where you want to force your users to join. It can be any group or channel, public or private.

3) Use /fsub chat_id/username to make me functional. Use /id if you need chat id.
Example : `/fsub -1001811940117` or `/forcesubscribe -1001811940117`

4) [Optional] Use /settings to Change Settings!

5) You are good to go. Leave the rest to me.**

✨ **Available Commands** ✨

**/fsub - See Current Force subscribers Chat 
/fsub chat_id/username - Force users to Join the Particular Chat 
/settings - Change Group Settings
/id - Get the chat id of any Group or Channel 
/about - About The Bot
/help - This Message
/start - Start the Bot**

**Note - You Can also Use `/forcesubscribe` Instead of** `/fsub`
    """

    # About Message
    ABOUT = """
**About This Bot** 

**A Telegram Force Subscribing Bot by @UK_Studios_Official

Source Code : [Click Here](https://bit.ly/3MyHHyQ)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @GreyMatter_Owner**
    """
