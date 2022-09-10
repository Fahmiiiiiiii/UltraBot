# ultrabot - UserBot
# Copyright (C) 2021-2022 Teamultrabot
#
# This file is a part of < https://github.com/Teamultrabot/ultrabot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Teamultrabot/ultrabot/blob/main/LICENSE/>.

from telethon import Button, custom

from plugins import ATRA_COL, InlinePlugin
from pyultrabot import *
from pyultrabot import _ult_cache
from pyultrabot._misc import owner_and_sudos
from pyultrabot._misc._assistant import asst_cmd, callback, in_pattern
from pyultrabot.fns.helper import *
from pyultrabot.fns.tools import get_stored_file
from strings import get_languages, get_string

OWNER_NAME = ultrabot_bot.full_name
OWNER_ID = ultrabot_bot.uid

AST_PLUGINS = {}


async def setit(event, name, value):
    try:
        udB.set_key(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    return [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
