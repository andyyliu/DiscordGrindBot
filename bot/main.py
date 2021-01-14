import discord, requests, json, random, os
from discord.ext import commands
from dotenv import load_dotenv
from messages import messages
from rng import rng

# cogs
# extensions = ["messages", "rng", "economy"]

# client = discord.Client()
client = commands.Bot(command_prefix = '!', case_insensitive = True)

# Initial login
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Responses to commands and words
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    message.content = message.content.casefold()

    # Respond to messages
    phrase = messages(message)
    if phrase:
        for line in phrase:
            await message.channel.send(line)
    await client.process_commands(message)

    #Respond to commands (need to change to command function instead of messages)
    phrase = rng(message)
    if phrase:
        for line in phrase:
            await message.channel.send(line)
    await client.process_commands(message)

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name = "general")
    await channel.send(f'Hi @{member.name}, welcome to The Skate Park!')

# activating the bot
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)