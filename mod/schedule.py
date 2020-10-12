import discord
from discord.ext import commands, tasks
import asyncio
import random
from dataclasses import dataclass
import aiosqlite
from time import ctime

@dataclass
class Scheduler:
    name: str
    tag: int
    monday: str=None
    tuesday: str=None
    wednesday: str=None
    thursday: str=None
    friday: str=None
    saturday: str=None
    sunday: str=None

class MySchedule(commands.Cog):

    users = []

    def __init__(self, bot):
        self.bot = bot
        bot.loop.create_task(self.async_init())

    async def async_init(self):
        await self.bot.wait_until_ready()
        async with aiosqlite.connect("PCSGDB.sqlite3") as db:
            await db.execute("""CREATE TABLE IF NOT EXISTS User_Schedules(
                name TEXT,
                id INTEGER PRIMARY KEY UNIQUE,
                monday TEXT,
                tuesday TEXT,
                wednesday TEXT,
                thursday TEXT,
                friday TEXT,
                saturday TEXT,
                sunday TEXT
            )""")

            await db.commit()
        
        await self.setup()
        #self.saving.start()

    # Commands
    @commands.command()
    async def scheduleset(self, ctx, dayset=None):
        await ctx.send("For privacy, let's go to dms >:)")
        _ = ctx.author
        user = await self.getuser(ctx)
        if not user: await ctx.send("An error occured. Contact a mod if the error persists")
        await ctx.author.send("Did you know that you can do p.scheduleset monday to set a schedule for monday etc?")
        def check(m):
            return m.author == ctx.author and m.channel == ctx.author.channel

        skipped = False
        dsotw = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        if dayset:
            if dayset.lower() not in dsotw: await ctx.send("Invalid day"); return
            dotw = [dayset.lower()]
        if not dayset:
            dotw = dsotw

        for day in dotw:
            while True:
                await ctx.author.send(f"Tell me a list of tasks you generally do on {day}. Say Skip to move onto the next day, and exit to exit")
                try: 
                    msg = await self.bot.wait_for('message', timeout=400, check=check)   
                    if msg.content.lower() == "exit": await ctx.send("Exiting"); return
                    if msg.content.lower() == "skip": await ctx.send("Skipping"); skipped = True; break
                
                except TimeoutError: await ctx.author.send("Could have just said no instead of leaving me hanging...")
                
                if len(msg.content) > 900: await ctx.author.send("Those tasks are a bit too long for me. Trim it a bit please"); continue
                
                await ctx.author.send(f"So to confirm. Your tasks for {day} are {msg.content} correct? Say no for no, and anything else for yes")
                
                try:
                    conf = await self.bot.wait_for("message", timeout=60, check=check)
                    if conf.content.lower() == "no": continue
                    elif conf.content.lower() == "exit": await ctx.author.send("Leaving"); return
                    else: break
                
                except TimeoutError: await ctx.author.send("Took to long. I'm leaving"); return

            if skipped: 
                skipped = False
                if len(dotw) == 1: break
                else: continue

            async with aiosqlite.connect("PCSGDB.sqlite") as db:
                await db.execute("INSERT OR REPLACE INTO User_Schedules (?) WHERE ID = ? VALUES(?)", (day, ctx.author.id, msg.content.lower()))
                setattr(user, day, msg.content)

        await ctx.author.send("Completed. Thank you for taking time out to do this. :bowing: View it with p.myschedule")

    @commands.command()
    async def myschedule(self, ctx, day=None):
        dotw = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

        if not day: 
            await ctx.send("Did you know that you can do p.myschedule monday to view your schedule for monday etc etc?")
            day = [d for d in dotw if d.startswith(ctime().split(" ")[0].lower())]
            day = day[0]
        
        if day:
            day = day.lower()
            if day not in dotw: await ctx.send("Invalid day"); return

        user = await self.getuser(ctx)
        value = getattr(user, day, None)
        if not value: await ctx.send("You don't seem to have anything for that day."); return
        embed = discord.Embed(
            title=f"Showing {day} schedule for {ctx.author.name}",
            description=value,
            color=random.randint(0, 0xffffff)
        )

        embed.set_thumbnail(url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def clrschedule(self, ctx, day, conf=False):
        user = await self.getuser(ctx)
        dotw = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]
        print(day)
        if day.lower() not in dotw:
            await ctx.send("Invalid value")
            return

        if day.lower() == "all":
            if not conf: await ctx.send("If you are sure that you wish to clear all of your schedules, do p.clrschedule all True"); return
            for d in dotw:
                setattr(user, d, None)

            await ctx.send("Cleared all of your schedules")

        if not conf: await ctx.send(f"To confirm that you want to clear your schedule for {day} do p.clrschedule {day} True"); return
        setattr(user, day.lower(), None)
        await ctx.send(f"Cleared your schedule for {day}")
        

    # Functions
    async def setup(self):
        guild = self.bot.get_guild(693608235835326464)
        
        async with aiosqlite.connect("PCSGDB.sqlite3") as db:
            for member in guild.members:
                if member.bot: continue
                await db.execute("INSERT OR IGNORE INTO User_Schedules (Name, ID) VALUES (?, ?)",
                (str(member), member.id))

            await db.commit()

            async with db.execute("SELECT * FROM User_Schedules") as cursor:
                async for row in cursor:
                    self.users.append(Scheduler(row[0], row[1], row[2], row[3], row[4]))

        print("Setup for Scheduling Complete")


    async def getuser(self, ctx):
        user = [x for x in self.users if x.tag == ctx.author.id]
        if not user: return None
        return user[0]


    # Saving
    @tasks.loop(minutes=5)
    async def saving(self):
        # async with aiosqlite.connect("PCSGDB.sqlite3") as db:
        #     for user in self.users:
        #         await db.execute("""INSERT OR REPLACE INTO User_Schedules (name, id, monday, tuesday, wednesday, thursday, friday, 
        #         saturday, sunday) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (user.name, user.tag, user.monday, user.tuesday, user.wednesday,
        #         user.thursday, user.friday, user.saturday, user.sunday))

        #     await db.commit()
        pass

    
def setup(bot):
    bot.add_cog(MySchedule(bot))