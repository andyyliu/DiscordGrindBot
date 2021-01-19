import discord, requests, json, os, sys, traceback
from discord.ext import commands
from dotenv import load_dotenv


# cogs
extensions = ['rng', 'messages', 'date']

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
    

# Activating the bot
load_dotenv()

# Insert your custom discord token here (placed in an .env file: DISCORD_TOKEN = *your custom token*)
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN, bot = True, reconnect = True)