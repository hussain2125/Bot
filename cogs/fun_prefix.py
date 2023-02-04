import discord
from discord.ext import commands
import random

class fun_prefix(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("fun prefix commands are ready!")

    @commands.command(aliases=["Ding","ping ding","Ring"])
    async def ping(self, ctx):
        await ctx.send("Hello I'm Ocean's bot, Kyu Chonk gye naa !!!")

    @commands.command(aliases=["Hola","olla"])
    async def hola(self, ctx):
        await ctx.send("Salam Alaikum olla! how are you?")
    
async def setup(client):
    await client.add_cog(fun_prefix(client))