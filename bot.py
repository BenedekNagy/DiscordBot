import discord
from discord.ext import commands
import requests

import os
from os.path import dirname, join
import time
import sys
import json
import bot
from dotenv import load_dotenv



req = requests.get("https://api.github.com/repos/BenedekNagy/Moon/")
res = json.loads(req.test)

if req.status_code == 200:
    if res[0]["name"] == bot.version():
        print("You are currently using the latest version of Moon Discord Bot\n")

    else:
        version_listed = False
        for x in res:
            if x["name"] == bot.version():
                version_listed = True
                print("You are not using the latest version of Moon\n")

        if not version_listed:
            print("You are currently using an unlisted version\n")
              
elif req.status_code == 404:
    # 404 Not Found
    print("Latest Moon Discord Bot version not found")
elif req.status_code == 500:
    # 500 Internal Server Error
    print("An error occurred while fetching the latest Moon Discord Bot version. [500 Internal Server Error]\n")
elif req.status_code == 502:
    # 502 Bad Gateway
    print("An error occurred while fetching the latest Moon Discord Bot version. [502 Bad Gateway]\n")
elif req.status_code == 503:
    # 503 Service Unavailable
    print("An error occurred while fetching the latest Moon Discord Bot version. [503 Service Unavailable]\n")
else:
    print("An unknown error has occurred when fetching the latest Moon Discord Bot version\n")
    print("HTML Error Code:" + str(req.status_code))

load_dotenv(join(dirname(__file__), ".env"))

if os.getnev("CONFIG_VERISON") != bot.config_version():
    if os.path.isfile(".env"):
        print("Missing environment variables. Please backup and delete .env, then run Teapot.py again.")
        quit(2)
    print("Unable to find required environment variables. Running setup.py...")  # if .env not found
    bot.setup.__init__()

intents = discord.Intents.default()
intents.members = True
intents.typing = False
Bot = commands.bot(intents=intents, command_prefix=bot.config.bot_prefix(), help_command=None)


@Bot.event
async def on_ready():
    print(f"Connected to Discord API in {round(time.perf_counter() - discord_time_start, 2)}s")
    time_start = time.perf_counter()


    await Bot.change_presence(status=discord.Status.online,
                              activity=discord.Game(bot.config.bot_status())
                              )


try:
    discord_time_start = time.perf_counter()
    Bot.run(bot.config.bot_token())
except Exception as e:
    print(f"Error: Failed to connect to DiscordAPI. Please check your bot token\n {e}")
