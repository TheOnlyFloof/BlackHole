import logging
import os
import sys

import discord
from discord.ext import commands
from dotenv import load_dotenv

role_assign = "role test"

load_dotenv()

token = os.getenv("DISCORD_TOKEN")

if token is None:
    sys.exit("DISCORD_TOKEN is not set in the environment")

handler = logging.FileHandler(
    filename="discord.log",
    encoding="utf-8",
    mode="w"
)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)



@bot.event
async def on_ready():
    if bot.user is not None:
        print(f"Logged in as {bot.user.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "allo jerry" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} Tu t'es fait whoopé!")
    await bot.process_commands(message)



@bot.command()
async def poll(ctx, arg, *, msg):
    embed = discord.Embed(title="[---SONDAGE---]", description=msg)
    poll_message = await ctx.send(embed=embed)
    if arg == "1":
        await poll_message.add_reaction("👍")
        await poll_message.add_reaction("👎")

    elif arg == "2":
        await poll_message.add_reaction("1️⃣")
        await poll_message.add_reaction("2️⃣")
        await poll_message.add_reaction("3️⃣")
        await poll_message.add_reaction("4️⃣")
        await poll_message.add_reaction("5️⃣")
        await poll_message.add_reaction("6️⃣")
        await poll_message.add_reaction("7️⃣")
        await poll_message.add_reaction("8️⃣")
        await poll_message.add_reaction("9️⃣")
        await poll_message.add_reaction("🔟")

    await ctx.message.delete()




@bot.command()
async def poll_help(ctx):

    await ctx.author.send("You Used Help Argument For Poll Command : \n \n!poll 1 ... : Yes/No \n!poll 2 ... : 1 to 10 \n \nThank You for Using BlackHole.")
    await ctx.message.delete()


@bot.command()
async def send(ctx, *, content):

    await ctx.send(content)
    await ctx.message.delete()



bot.run(token, log_handler=handler, log_level=logging.DEBUG)
