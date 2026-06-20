import discord
import os
from discord.ext import tasks
import aiohttp
from bs4 import BeautifulSoup
from config import CHANNEL_ID, CHECK_INTERVAL

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

already_sent = set()

@client.event
async def on_ready():
    print(f"✅ Connecté en tant que {client.user}")

    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("🚀 Surveillance GPU démarrée")

    if not check_prices.is_running():
        check_prices.start()

@tasks.loop(minutes=CHECK_INTERVAL)
async def check_prices():
    print("🔍 Vérification des prix...")

    channel = client.get_channel(CHANNEL_ID)

    if not channel:
        return

    # Ici nous ajouterons les scrapers plus tard
    # Exemple :
    # await channel.send("Test vérification")
async def check_ldlc():
    url = "https://www.ldlc.com/recherche/rtx+5080/"

    async with aiohttp.ClientSession() as session:
        async with session.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        ) as response:

            html = await response.text()

    print("Page LDLC récupérée :", len(html))
client.run(TOKEN)
