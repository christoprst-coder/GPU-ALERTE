import discord
import os
from discord.ext import tasks

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 1517834960751427668

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Connecté en tant que {client.user}")
    check_prices.start()

@tasks.loop(minutes=15)
async def check_prices():
    channel = client.get_channel(CHANNEL_ID)

    if channel:
        print("Vérification des prix...")
        # Ici on ajoutera les recherches RTX
        # await channel.send("Test surveillance RTX")

client.run(TOKEN)
