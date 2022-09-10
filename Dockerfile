#!/usr/bin/env bash
# UltraBot - UserBot
# Copyright (C) 2022-2023 UltraBot
#
# This file is a part of < https://github.com/Fahmiiiiiiii/UltraBot/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/Fahmiiiiiiii/UltraBot/blob/main/LICENSE/>.

FROM UltraBotTeam/UltraBot:main

# set timezone
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY installer.sh .

RUN bash installer.sh

# changing workdir
WORKDIR "/root/TeamUltroid"

# start the bot.
CMD ["bash", "startup"]
