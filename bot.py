import discord
from discord.ext import commands
import os
import asyncio
import random

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

client.remove_command("help")

#--------------------------------------------------------------------
# slash commands section down here 👇👇👇👇👇👇👇👇👇👇👇👇👇
#--------------------------------------------------------------------

# slash feedback command

@client.tree.command(name="feedback", description="for improvment of bot")
async def checkk(interaction: discord.Interaction, string : str):
    with open("./cogs/data.txt", "a") as f:
        f.write(string + "\n")
    await interaction.response.send_message("ok noted!!! thanks for suggesting us!")

# slash show feedback command

@client.tree.command(name="show_feedback", description="show pending feedbacks")
async def showdata(interaction: discord.Interaction):
        with open('./cogs/data.txt', 'r') as file:
            contents = file.read()
        await interaction.response.send_message(contents)

# slash delete last line of feedback command

@client.tree.command(name="del_last_line", description="it will delete the last feedback")
async def del_last_line(interaction: discord.Interaction):
    with open("./cogs/data.txt", "r") as f:
        lines = f.readlines()
    with open("./cogs/data.txt", "w") as f:
        for line in lines[:-1]:
            f.write(line)
    await interaction.response.send_message("ok deleted")

#--------------------------------------------------------------------
# slash commands section up there 👆👆👆👆👆👆👆👆👆👆👆👆👆
#--------------------------------------------------------------------

@client.event

async def on_ready():
    await client.tree.sync()
    print("Success: Bot is connected Discord")
    await client.change_presence(activity=discord.Game("'/feedback' to improve"))

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with client:
        await load()
        await client.start("TOKEN")

asyncio.run(main())
