import discord, requests, json, os, sys, traceback
from discord.ext import commands
from dotenv import load_dotenv
from messages import messages

# cogs
extensions = ['rng', 'cog_messages']

bot = commands.Bot(command_prefix = '!', case_insensitive = True)

if __name__ == '__main__':
    for ext in extensions:
        bot.load_extension(ext)

# Initial login
@bot.event
async def on_ready():
    print('\n\nLogged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name="on the grind"))
    print('Successfully booted!')

# Responses to commands and words
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    message.content = message.content.casefold()

    # Respond to messages
    phrase = messages(message)
    if phrase:
        for line in phrase:
            await message.channel.send(line)
    
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name = "general")
    await channel.send(f'Hi @{member.name}, welcome to The Skate Park!')

# activating the bot
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN, bot = True, reconnect = True)