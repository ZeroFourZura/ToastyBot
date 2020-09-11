import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

import Cluster


class Com(commands.Cog):

    #initialization
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Command Cog is here too")


    #The test command
    @commands.command()
    async def test(self, ctx):
        await ctx.send("Yo!")

    #Score command
    @commands.command()
    async def score(self, ctx):
        score=Cluster.collection.find_one({"_id": ctx.author.id})
        await ctx.send(score["score"])

def setup(bot):
    bot.add_cog(Com(bot))
