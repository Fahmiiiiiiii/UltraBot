#!/usr/bin/env bash
# UltraBot - UserBot
# Copyright (C) 2022-2023 UltraBot
#
# This file is a part of < https://github.com/Fahmiiiiiiii/UltraBot/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/Fahmiiiiiiii/UltraBot/blob/main/LICENSE/>.

clear
echo -e "\e[1m"
echo " ᴜʟᴛʀᴀʙᴏᴛ - ᴜsᴇʀʙᴏᴛ ɪɴsᴛᴀʟʟ"
echo -e "\e[0m"
sec=5
spinner=(⣻ ⢿ ⡿ ⣟ ⣯ ⣷)
while [ $sec -gt 0 ]; do
    echo -ne "\e[33m ${spinner[sec]} Starting dependency installation in $sec seconds...\r"
    sleep 1
    sec=$(($sec - 1))
done
echo -e "\e[1;32mInstalling Dependencies ---------------------------\e[0m\n" # Don't Remove Dashes / Fix it
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://raw.githubusercontent.com/Fahmiiiiiiii/UltraBot/main/resources/session/ssgen.py
pip uninstall telethon -y && install telethon
clear
python3 ssgen.py
