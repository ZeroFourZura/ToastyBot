import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

SimpDictionary = ["belle",
"delphine",
"donate",
"donated",
"donation",
"subcribe",
"subscribed",
"pokimane",
"alinity",
"holo",
"hololive"]

class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Event Cog is ready for some action")

    #Dd's messy command. It also doesn't work
    @commands.Cog.listener()
    async def on_message(self, ctx):
        #print(f"{ctx.channel}: {ctx.author}: {ctx.author.name}: {ctx.content}")
        myquery = {"_id": ctx.author.id}
        #first check if the message is from bot itelf
        # if ctx.author==self.bot.user:
        #     await self.bot.process_commands(self, ctx)

        for i in SimpDictionary:
            if i in str(ctx.content.lower()):
                if Randomise(3):
                    if Randomise(2):
                        await ctx.channel.send("Get a load of this simp!")
                    else:
                        await ctx.channel.send("Simp!")
                break

        if "money" in str(ctx.content.lower()):
            if Randomise(2):
                await ctx.channel.send("here! take some coins you pityful creature")




def setup(bot):
    bot.add_cog(Events(bot))

def setup(bot):
    bot.add_cog(Events(bot))

def Randomise(Boundary):
    Number = random.randint(1, Boundary)

    if Number == 1:
        return 1
    else:
        return 0
