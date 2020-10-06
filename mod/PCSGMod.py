import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()
from random import randint
import aiosqlite

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="p.", case_insensitive=True, intents=intents)
bot.help_command = None

bot.load_extension("roles")
bot.load_extension("levels")
bot.load_extension("sfw")

@bot.event
async def on_ready():
    print(f"Right...")
    activity = discord.Activity(name='for p.help', type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)

    async with aiosqlite.connect("PCSGDB.sqlite3") as db:
            await db.execute("""CREATE TABLE IF NOT EXISTS WarnUser(
                Name Text NOT NULL
                ID INTEGER PRIMARY KEY UNIQUE NOT NULL
                WarnLevel INTEGER NOT NULL
            )""")
        
            await db.execute("""CREATE TABLE IF NOT EXISTS Users (
                Name TEXT NOT NULL,
                ID INTEGER PRIMARY KEY UNIQUE NOT NULL,
                Level INTEGER NOT NULL,
                Exp INTEGER NOT NULL,
                ExpThresh INTEGER NOT NULL
                );""")

        await db.commit()


    

@bot.command()
@commands.is_owner()
async def rc(ctx):
    bot.reload_extension("roles")
    bot.reload_extension("levels")
    bot.reload_extension("sfw")
    await ctx.send("Cogs Have been reloaded")

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Showing Help",
        color=randint(0, 0xffffff)
    )

    embed.set_thumbnail(url=bot.user.avatar_url)
    embed.add_field(name="p.profile", value="Shows your profile for this server", inline=False)
    embed.add_field(name="p.top", value="Shows top 5 active users", inline=False)
    embed.add_field(name="p.rank", value="Shows your rank for this server", inline=False)
    
    await ctx.send(embed=embed)


yes = os.getenv("keymod")
bot.run(yes)
