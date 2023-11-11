import discord
import asyncio
from datetime import datetime

intents = discord.Intents().all()
client = discord.Client(intents=intents)
channel_1 = 1081610454721380492

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

def channel():
    channel = client.get_channel(channel_1)

@client.event
async def on_ready():
    while not client.is_closed():
        now = datetime.now()

        hour = now.hour % 12
        minute = now.minute

        if minute == 0 and hour in range(12):
            time_dict = {
                0: "🕛 0 A.M.",
                1: "🕐 1 A.M.",
                2: "🕑 2 A.M.",
                3: "🕒 3 A.M.",
                4: "🕓 4 A.M.",
                5: "🕔 5 A.M.",
                6: "🌅",
                7: "🕖 7 A.M.",
                8: "🕗 8 A.M.",
                9: "🕘 9 A.M.",
                10: "🕙 10 A.M.",
                11: "🕚 11 A.M.",
            }
        elif minute == 0 and hour in range(12, 24):
            time_dict = {
                0: "🕛 0 P.M.",
                1: "🕐 1 P.M.",
                2: "🕑 2 P.M.",
                3: "🕒 3 P.M.",
                4: "🕓 4 P.M.",
                5: "🕔 5 P.M.",
                6: "🌇",
                7: "🕖 7 P.M.",
                8: "🕗 8 P.M.",
                9: "🕘 9 P.M.",
                10: "🕙 10 P.M.",
                11: "🕚 11 P.M.",
            }
        else:
            await asyncio.sleep(1)
            continue

        channel()
        await channel.send(time_dict[hour])

        await asyncio.sleep(60 - now.second)    
        
client.run("token")