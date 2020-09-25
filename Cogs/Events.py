import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random

import Cluster

simpDictionary = ["belle",
"delphine",
"donate",
"donated",
"donation",
"subcribe",
"subscribed",
"pokimane",
"alinity",
"holo",
"hololive",
"stream",
"streamer"]

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

        sentence = (ctx.content.lower())
        simpFlag = 0
        sentence = sentence.split(' ')
        for i in range(0, len(sentence)):
            for j in range(0, len(simpDictionary)):
                if(sentence[i] == simpDictionary[j]):
                    simpFlag = 1

        if simpFlag == 1:
            # if randomise(4):
                if randomise(2):
                    await ctx.channel.send("simp")
                else:
                    await ctx.channel.send("get a load of this simp!")



        if "money" in str(ctx.content.lower()):
            if randomise(4):
                await ctx.channel.send("here! take some coins you pityful creature")

        if (Cluster.collection.count_documents(myquery) == 0):
            if "crispy" in str(ctx.content.lower()):
                post = {"_id": ctx.author.id, "score": 1}
                Cluster.collection.insert_one(post)
                await ctx.channel.send('accepted!')
        else:
            if "crispy" in str(ctx.content.lower()):
                query = {"_id": ctx.author.id}
                user = Cluster.collection.find(query)
                for result in user:
                    score = result["score"]
                score = score + 1
                Cluster.collection.update_one({"_id":ctx.author.id}, {"$set":{"score":score}})
                await ctx.channel.send('accepted!')


def setup(bot):
    bot.add_cog(Events(bot))

def randomise(boundary):
    Number = random.randint(1, boundary)

    if Number == 1:
        return 1
    else:
        return 0
