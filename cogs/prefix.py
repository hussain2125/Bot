import discord
from discord.ext import commands
import random
import os


class prefix(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("prefix commands are ready!")
    
    @commands.command(aliases=["del","DEL","cls"])
    @commands.has_permissions(manage_messages=True)
    async def delete(self, ctx, count: int):
        await ctx.channel.purge(limit=count+1)
        await ctx.send(f"{count} message(s) have been deleted.", delete_after=2)
    
    @commands.command()
    async def roll(self, ctx, count: int = 10):
        number = random.randint(1,count)
        await ctx.send(f'You rolled a {number}')

    @commands.command(aliases=["otag","oceantags","Oceantag","otags","ot","oceantag"])
    async def Ot(self, ctx):
        with open("./cogs/ot.txt", "r") as f:
            for line in f:
                await ctx.send(line)
    
    @commands.command(aliases=["htag","happytags","Happytag","htags","ht","happytag"])
    async def Ht(self, ctx):
        with open("./cogs/ht.txt", "r") as f:
            for line in f:
                await ctx.send(line)

    @commands.command()
    async def Bot(self, ctx):
        embed_message = discord.Embed(title="Hi im Bot", description = "I'm this server's personal bot", color = discord.Color.green())

        await ctx.send(embed=embed_message)

    @commands.command()
    async def repeat(self, ctx, times: int, content: str):
        """Repeats a message multiple times."""
        for i in range(times):
            await ctx.send(content)

    @commands.command() # !when_joined @mention
    async def when_joined(self, ctx, member: discord.Member):
        """Says when a member joined."""
        await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

    @commands.command(description='For when you wanna settle the score some other way')
    async def choose(self, ctx, *choices: str):  # !choose 1 2 3 4 AA BB CC
        """Chooses between multiple choices."""
        await ctx.send(random.choice(choices))

    @commands.command()
    async def userpic(self, ctx: commands.Context, user: discord.User=None):
        if user is None:
            user = ctx.author
        else:
            user=user
        embed = discord.Embed(title=f"{user.name}'s dp", color = discord.Color.blue())
        embed.set_image(url=user.display_avatar.url)
        await ctx.send(embed=embed)

#----------------------------------------------------------------------------------
# group prefix command section down here 👇👇👇👇👇👇👇👇👇👇👇
#-----------------------------------------------------------------------------------

# example: !cool bot ---> cool will work with all sub commands "bot" is subcommand

    @commands.group()
    async def cool(self, ctx):
        """Says if a user is cool.
        In reality this just checks if a subcommand is being invoked.
        """
        if ctx.invoked_subcommand is None:
            await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


    @cool.command(name='bot')
    async def _bot(self, ctx):
        """Is the bot cool?"""
        await ctx.send('Yes, the bot is cool.')

    @cool.command(name='ocean')
    async def _ocean(self, ctx):
        """Is the bot cool?"""
        await ctx.send('Yes, the ocean is cool. he is intelligent')

async def setup(client):
    await client.add_cog(prefix(client))