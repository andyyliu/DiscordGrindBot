import discord, requests, json, random, os
from discord.ext import commands
from dotenv import load_dotenv
from messages import messages
from commands import commands

client = discord.Client()
# client = commands.Bot(command_prefix = '!')

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
    
    #Respond to commands
    phrase = commands(message)
    if phrase:
        for line in phrase:
            await message.channel.send(line)

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name = "general")
    await channel.send(f'Hi @{member.name}, welcome to The Skate Park!')

# @client.command()
# async def balance(ctx):
#     await open_account(ctx.author)

# async def open_account(user):
#     with open("bank.json", "r") as f:
#         users = json.load(f)
#     if str(user.id) in users:
#         return False
#     else:
#         users[str(user.id)]["wallet"] = 0
#         users[str(user.id)]["bank"] = 0
#     with open("bank.json", "w") as f:
#         json.dump(users, f)



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)