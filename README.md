<p align="center">
  <img src="./resources/extras/logo_readme.jpg" alt="Fahmiiiiiiii Logo">
</p>
<h1 align="center">
  <b>UltraBot - UserBot</b>
</h1>

<b>A stable pluggable Telegram userbot + Voice & Video Call music bot, based on Telethon.</b>

[![](https://img.shields.io/badge/UltraBot-v0.7-darkgreen)](#)
[![Stars](https://img.shields.io/github/stars/Fahmiiiiiiii/UltraBot?style=flat-square&color=yellow)](https://github.com/Fahmiiiiiiii/UltraBot/stargazers)
[![Forks](https://img.shields.io/github/forks/Fahmiiiiiiii/UltraBot?style=flat-square&color=orange)](https://github.com/Fahmiiiiiiii/UltraBot/fork)
[![Size](https://img.shields.io/github/repo-size/Fahmiiiiiiii/UltraBot?style=flat-square&color=green)](https://github.com/Fahmiiiiiiii/UltraBot/)   
[![Python](https://img.shields.io/badge/Python-v3.10.3-blue)](https://www.python.org/)
[![CodeFactor](https://www.codefactor.io/repository/github/Fahmiiiiiiii/UltraBot/badge/main)](https://www.codefactor.io/repository/github/Fahmiiiiiiii/UltraBot/overview/main)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/Fahmiiiiiiii/UltraBot/graphs/commit-activity)
[![Docker Pulls](https://img.shields.io/docker/pulls/theFahmiiiiiiii/UltraBot?style=flat-square)](https://img.shields.io/docker/pulls/theFahmiiiiiiii/UltraBot?style=flat-square)   
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/Fahmiiiiiiii/UltraBot)
[![Contributors](https://img.shields.io/github/contributors/Fahmiiiiiiii/UltraBot?style=flat-square&color=green)](https://github.com/Fahmiiiiiiii/UltraBot/graphs/contributors)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)
[![License](https://img.shields.io/badge/License-AGPL-blue)](https://github.com/Fahmiiiiiiii/UltraBot/blob/main/LICENSE)   
[![Sparkline](https://stars.medv.io/Fahmiiiiiiii/UltraBot.svg)](https://stars.medv.io/Fahmiiiiiiii/UltraBot)
----

# Deploy
- [Heroku](#deploy-to-heroku)
- [Okteto](#deploy-to-okteto)
- [Local Machine](#deploy-locally)

# Documentation 
[![Documentation](https://img.shields.io/badge/Documentation-UltraBot-blue)](http://ultrabot.tech/)

# Tutorial 
- Full Tutorial - [![Full Tutorial](https://img.shields.io/badge/Watch%20Now-blue)](https://www.youtube.com/watch?v=0wAV7pUzhDQ)

- Tutorial to get Redis URL and password - [here.](./resources/extras/redistut.md)
---

## Deploy to Heroku
Get the [Necessary Variables](#Necessary-Variables) and then click the button below!  

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://deploy.mailprabowo.my.id)

## Deploy to Okteto
Get the [Necessary Variables](#Necessary-Variables) and then click the button below!

[![Develop on Okteto](https://okteto.com/develop-okteto.svg)](https://cloud.okteto.com/deploy?repository=https://github.com/Fahmiiiiiiii/UltraBot)

## Deploy Locally
- [Traditional Method](#local-deploy---traditional-method)
- [Easy Method](#local-deploy---easy-method)
- [UltraBot CLI](#UltraBot-cli)

### Local Deploy - Easy Method
- Linux - `wget -O locals.py https://git.io/JY9UM && python3 locals.py`
- Windows - `cd desktop ; wget https://git.io/JY9UM -o locals.py ; python locals.py`
- Termux - `wget -O install-termux https://tiny.UltraBot.tech/termux && bash install-termux`

### Local Deploy - Traditional Method
- Get your [Necessary Variables](#Necessary-Variables)
- Clone the repository:    
`git clone https://github.com/Fahmiiiiiiii/UltraBot.git`
- Go to the cloned folder:    
`cd UltraBot`
- Create a virtual env:      
`virtualenv -p /usr/bin/python3 venv`
`. ./venv/bin/activate`
- Install the requirements:      
`pip(3) install -U -r re*/st*/optional-requirements.txt`
`pip(3) install -U -r requirements.txt`
- Generate your `SESSION`:
  - For Linux users:
    `bash sessiongen`
     or
    `wget -O session.py https://git.io/JY9JI && python3 session.py`
  - For Termux users:
    `wget -O session.py https://git.io/JY9JI && python session.py`
  - For Windows Users:
    `cd desktop ; wget https://git.io/JY9JI -o UltraBot.py ; python UltraBot.py`
- Fill your details in a `.env` file, as given in [`.env.sample`](https://github.com/Fahmiiiiiiii/UltraBot/blob/main/.env.sample).
(You can either edit and rename the file or make a new file named `.env`.)
- Run the bot:
  - Linux Users:
   `bash startup`
  - Windows Users:
    `python(3) -m pyUltraBot`
<details>
<summary><h3>[OUTDATED] UltraBot CLI</h3></summary>

[UltraBot CLI](https://github.com/BLUE-DEVIL1134/UltraBotCli) is a command-line interface for deploying UltraBot.   

- **Installing** -    
Run the following code on a terminal, with curl installed.   
`ver=$(curl https://raw.githubusercontent.com/BLUE-DEVIL1134/UltraBotCli/main/version.txt) && curl -L -o UltraBot https://github.com/BLUE-DEVIL1134/UltraBotCli/releases/download/$ver/UltraBot.exe`
OR
Go to [UltraBotCli](https://github.com/BLUE-DEVIL1134/UltraBotCli) and install the version release from the Github Releases. Add the executable to your system path as specified in the [Readme](https://github.com/BLUE-DEVIL1134/UltraBotCli#how-to-use-UltraBotcli-).   

- **Documentation** -
Take a look at the [`docs`](https://blue-devil1134.github.io/UltraBotCli/) for more detailed information.
</details>

---
## Necessary Variables
- `SESSION` - SessionString for your accounts login session. Get it from [here](#Session-String)

One of the following database:
- For **Redis** (tutorial [here](./resources/extras/redistut.md))
  - `REDIS_URI` - Redis endpoint URL, from [redislabs](http://redislabs.com/).
  - `REDIS_PASSWORD` - Redis endpoint Password, from [redislabs](http://redislabs.com/).
- For **MONGODB**
  - `MONGO_URI` - Get it from [mongodb](https://mongodb.com/atlas).
- For **SQLDB**
  - `DATABASE_URL`- Get it from [elephantsql](https://elephantsql.com).

## Session String
Different ways to get your `SESSION`:
* [![Run on Repl.it](https://replit.com/badge/github/Fahmiiiiiiii/UltraBot)](https://replit.com/@Fahmiiiiiiii/UltraBotStringSession)
* Linux : `wget -O session.py https://git.io/JY9JI && python3 session.py`
* PowerShell : `cd desktop ; wget https://git.io/JY9JI ; python UltraBot.py`
* Termux : `wget -O session.py https://git.io/JY9JI && python session.py`
* TelegramBot : [@SessionGeneratorBot](https://t.me/SessionGeneratorBot)

---

# License
[![License](https://www.gnu.org/graphics/agplv3-155x51.png)](LICENSE)   
UltraBot is licensed under [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) v3 or later.

---

# Credits
* [![Fahmiiiiiiii-Devs](https://img.shields.io/static/v1?label=Fahmiiiiiiii&message=devs&color=critical)](https://t.me/UltraBotDevs)
* [Lonami](https://github.com/LonamiWebs/) for [Telethon.](https://github.com/LonamiWebs/Telethon)
* [MarshalX](https://github.com/MarshalX) for [PyTgCalls.](https://github.com/MarshalX/tgcalls)

> Made with 💕 by [@mailbintisukijem](https://t.me/mailbintisukijem).    
