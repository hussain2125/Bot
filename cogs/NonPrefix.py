import discord
from discord.ext import commands
import time

class Nonprefix(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Non-Prefix commands are ready!")
   
    @commands.Cog.listener()
    @commands.has_permissions(manage_messages=True)
    async def on_message(self, message):

        message_content = message.content.lower()
        banned_words = ["FEK", "FUCK","BITCH"]
        banned_words_2 = [('LOL', 'replaced_substring_1'),('LEL', 'replaced_substring_2'),('L0L', 'replaced_substring_3')]

        if message.author.bot:
            return

        elif "chup kr" in message_content:
            print("chup working")
            await message.channel.send("Acha Chup houn, bye!!!") 
    
        elif "ocean" in message_content:
            print("ocean working")
            await message.channel.send("His Name is:")
            embed_message = discord.Embed(title="Hussain", color = discord.Color.green())
            await message.channel.send(embed=embed_message)
        
        elif "ahsan" in message_content:
            print("Ahsan working")
            embed_message = discord.Embed(title="Hi Ahsan", color = discord.Color.red())
            await message.channel.send(embed=embed_message)
        
#        elif message.mentions:
#            for user in message.mentions:
#                await message.channel.send("mat kro yr isko tang")

        elif "happy" in message_content:
            print("happy working")
            await message.channel.send("```Omg bro happyyyy ?? don't mess with him```")

        elif "pc" in message_content:
            print("pc working")
            await message.channel.send("```wait a min!! pc!! He has a lot of ids in coc and he's so pro```")

        elif "sami" in message_content:
            print("sami working")
            embed_message = discord.Embed(title="Sami is proooo 🥵", color = discord.Color.blue())
            await message.channel.send(embed=embed_message)

        elif "roshni" in message_content:
            print("roshni working")
            embed_message = discord.Embed(title="Roshni noobri 🥵", color = discord.Color.blue())
            await message.channel.send(embed=embed_message)

        for word in banned_words:
            if word in message.content.lower() or word in message.content.upper():
               await message.delete()
               await message.channel.send(f"{message.author.mention} gali mat do 😞 ") 
               break 
      
#this is not working down section .... 

        for word in banned_words_2:
            if word in message.content:
                message.content = message.content.replace(word, "***")
                await message.edit(content=message.content)

                #await message.delete()
                #await message.channel.send("bruhh! lol & lel are not allowed " ,  delete_after=3)


async def setup(client):
    await client.add_cog(Nonprefix(client))