#!/usr/bin/env bash
# UltraBot - UserBot
# Copyright (C) 2022-2023 UltraBot
#
# This file is a part of < https://github.com/Fahmiiiiiiii/UltraBot/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/Fahmiiiiiiii/UltraBot/blob/main/LICENSE/>.

import os
import sys

from .version import __version__

run_as_module = False

class ULTConfig:
    lang = "en"
    thumb = "resources/extras/ultrabot.jpg"

if sys.argv[0] == "-m":
    run_as_module = True

    import time

    from .configs import Var
    from .startup import *
    from .startup._database import ultrabotDB
    from .startup.BaseClient import ultrabotClient
    from .startup.connections import validate_session, vc_connection
    from .startup.funcs import _version_changes, autobot, enable_inline, update_envs
    from .version import ultrabot_version

    if not os.path.exists("./plugins"):
        LOGS.error(
            "'plugins' folder not found!\nMake sure that, you are on correct path."
        )
        exit()

    start_time = time.time()
    _ult_cache = {}
    _ignore_eval = []

    udB = ultrabotDB()
    update_envs()

    LOGS.info(f"Connecting to {udB.name}...")
    if udB.ping():
        LOGS.info(f"Connected to {udB.name} Successfully!")

    BOT_MODE = udB.get_key("BOTMODE")
    DUAL_MODE = udB.get_key("DUAL_MODE")

    if BOT_MODE:
        if DUAL_MODE:
            udB.del_key("DUAL_MODE")
            DUAL_MODE = False
        ultrabot_bot = None

        if not udB.get_key("BOT_TOKEN"):
            LOGS.critical(
                '"BOT_TOKEN" not Found! Please add it, in order to use "BOTMODE"'
            )

            sys.exit()
    else:
        ultrabot_bot = ultrabotClient(
            validate_session(Var.SESSION, LOGS),
            udB=udB,
            app_version=ultrabot_version,
            device_model="ultrabot",
        )
        ultrabot_bot.run_in_loop(autobot())

    asst = UltrabotClient(None, bot_token=udB.get_key("BOT_TOKEN"), udB=udB)

    if BOT_MODE:
        ultrabot_bot = asst
        if udB.get_key("OWNER_ID"):
            try:
                Ultrabot_bot.me = ultrabot_bot.run_in_loop(
                    ultrabot_bot.get_entity(udB.get_key("OWNER_ID"))
                )
            except Exception as er:
                LOGS.exception(er)
    elif not asst.me.bot_inline_placeholder:
        ultrabot_bot.run_in_loop(enable_inline(ultrabot_bot, asst.me.username))

    vcClient = vc_connection(udB, ultrabot_bot)

    _version_changes(udB)

    HNDLR = udB.get_key("HNDLR") or "."
    DUAL_HNDLR = udB.get_key("DUAL_HNDLR") or "/"
    SUDO_HNDLR = udB.get_key("SUDO_HNDLR") or HNDLR
else:
    print("UltraBot 2022 © TeamUltrabot")

    from logging import getLogger

    LOGS = getLogger("pyultrabot")

    ultrabot_bot = asst = udB = vcClient = None
