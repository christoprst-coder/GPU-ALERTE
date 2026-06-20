import discord
import os
import aiohttp
from bs4 import BeautifulSoup
from discord.ext import tasks
from config import CHANNEL_ID, CHECK_INTERVAL

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

already_sent = set()

async def check_ldlc():
    try:
        url = "https://www.ldlc.com/recherche/rtx+5080/"

        async with aiohttp.ClientSession() as session:
            async with session.get(
                url,
                headers={"User-Agent": "Mozilla/5.0"}
            ) as response:

                print("Status LDLC :", response.status)

                html = await response.text()

        print("Page LDLC récupérée :", len(html))

    except Exception as e:
        print("Erreur LDLC :", str(e))
