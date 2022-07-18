import discord
import time
from discord.ext import commands

bot = commands.Bot(command_prefix='>', self_bot=True)
script = open('script.txt','r', encoding='utf-8')

@bot.command()
async def send(ctx):
    for ligne in script:
        time.sleep(1.5)
        await ctx.send(ligne)


bot.run('your token here')

script.close()