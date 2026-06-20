import discord
import os
import aiohttp
from bs4 import BeautifulSoup
from discord.ext import tasks
from config import CHANNEL_ID, CHECK_INTERVAL

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def check_ldlc():
try:
url = "https://www.ldlc.com/recherche/rtx+5080/"

```
    async with aiohttp.ClientSession() as session:
        async with session.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        ) as response:

            print("Status LDLC:", response.status)

            html = await response.text()

    soup = BeautifulSoup(html, "html.parser")

    price_div = soup.find(attrs={"data-price": True})

    if price_div:
        price = float(price_div["data-price"])

        print("Prix trouvé :", price)

        if price <= 1000:
            channel = client.get_channel(CHANNEL_ID)

            if channel:
                await channel.send(
                    f"🚨 RTX 5080 trouvée sous 1000€ !\nPrix : {price} €"
                )
    else:
        print("Prix non trouvé")

except Exception as e:
    print("Erreur LDLC:", str(e))
```

@client.event
async def on_ready():
print(f"Connecté en tant que {client.user}")

```
channel = client.get_channel(CHANNEL_ID)

if channel:
    await channel.send("🚀 Surveillance GPU démarrée")

if not check_prices.is_running():
    check_prices.start()
```

@tasks.loop(minutes=CHECK_INTERVAL)
async def check_prices():
print("🔍 Vérification des prix...")
await check_ldlc()

client.run(TOKEN)
