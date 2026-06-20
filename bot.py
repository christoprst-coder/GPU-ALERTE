import discord
import os

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 1517834960751427668

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Connecté en tant que {client.user}")

    channel = client.get_channel(CHANNEL_ID)

    if channel:
        await channel.send("✅ Bot GPU démarré avec succès !")

client.run(TOKEN)
