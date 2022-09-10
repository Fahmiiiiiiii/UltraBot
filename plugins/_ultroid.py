# ultrabot - UserBot
# Copyright (C) 2021-2022 Teamultrabot
#
# This file is a part of < https://github.com/Teamultrabot/ultrabot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Teamultrabot/ultrabot/blob/main/LICENSE/>.

from telethon.errors import (
    BotMethodInvalidError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
)

from . import LOG_CHANNEL, LOGS, Button, asst, eor, get_string, ultrabot_cmd

REPOMSG = """
• **ultrabot USERBOT** •\n
• Repo - [Click Here](https://github.com/Fahmiiiiiiii/UltraBot)
• Addons - [Click Here](https://github.com/Fahmiiiiiiii/UltraBotAddons)
• Support - @ultrabotSupportChat
"""

RP_BUTTONS = [
    [
        Button.url(get_string("bot_3"), "https://github.com/Fahmiiiiiiii/UltraBot"),
        Button.url("Addons", "https://github.com/Teamultrabot/ultrabotAddons"),
    ],
    [Button.url("Support Group", "t.me/UltraBotSupport")],
]

ULTSTRING = """🎇 **Thanks for Deploying ultrabot Userbot!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage."""


@ultrabot_cmd(
    pattern="repo$",
    manager=True,
)
async def repify(e):
    try:
        q = await e.client.inline_query(asst.me.username, "")
        await q[0].click(e.chat_id)
        return await e.delete()
    except (
        ChatSendInlineForbiddenError,
        ChatSendMediaForbiddenError,
        BotMethodInvalidError,
    ):
        pass
    except Exception as er:
        LOGS.info(f"Error while repo command : {str(er)}")
    await e.eor(REPOMSG)


@ultrabot_cmd(pattern="ultrabot$")
async def useultrabot(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        ULTSTRING,
        file="https://graph.org/file/54a917cc9dbb94733ea5f.jpg",
        buttons=button,
    )
    if not (rs.chat_id == LOG_CHANNEL and rs.client._bot):
        await eor(rs, f"**[Click Here]({msg.message_link})**")
