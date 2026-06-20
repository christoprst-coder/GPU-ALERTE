import discord
import os
import aiohttp
from discord.ext import tasks
from config import CHANNEL_ID, CHECK_INTERVAL

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def check_ldlc():
try:
url = "https://www.ldlc.com/recherche/rtx+5080/"

    async with aiohttp.ClientSession() as session:
        async with session.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        ) as response:

            print("Status LDLC:", response.status)

            html = await response.text()

    soup = BeautifulSoup(html, "lxml")

    print(
        "Titre page :",
        soup.title.text if soup.title else "Aucun titre"
    )

    print("Page LDLC récupérée:", len(html))

except Exception as e:
    print("Erreur LDLC:", str(e))

@client.event
async def on_ready():
    print(f"Connecté en tant que {client.user}")

    channel = client.get_channel(CHANNEL_ID)

    if channel:
        await channel.send("🚀 Surveillance GPU démarrée")

    if not check_prices.is_running():
        check_prices.start()

@tasks.loop(minutes=CHECK_INTERVAL)
async def check_prices():
    print("🔍 Vérification des prix...")
    await check_ldlc()

client.run(TOKEN)
