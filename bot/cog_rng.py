import discord, random
# from words import ball, day
from discord.ext import commands

class RngCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dice(self, ctx):
        username = '@' + ctx.author.mention
        await ctx.send(username + ' takes a deep breath, and rolls the die, the number is.....' + str(random.randint(1, 6)) + '!')
    @commands.command()
    async def coin(self, ctx):
        username = '@' + ctx.author.mention
        await ctx.send([username + ' takes a deep breath, and rolls the die, the number is.....' + str(random.randint(1, 6)) + '!')    

def setup(bot):
    bot.add_cog(RngCog(bot))
# def rng(message):
#     username = '@' + message.author.name

#     # Return a list of commands
#     if message.content.startswith('!help'):
#         phrase = ['A list of currently avaiable commands are: !dice, !coin, !8ball, !day, and !help']
#         return phrase

#     # Return a random number from 1-6 when !dice is sent
#     if message.content.startswith('!dice'):
#         phrase = [username + ' takes a deep breath, and rolls the die, the number is.....' + str(random.randint(1, 6)) + '!']
#         return phrase

#     # Return heads or tails when !coin is sent
#     if message.content.startswith('!coin'):
#         result = ['heads', 'tails']
#         phrase = [username + ' flips the coin as high as possible, it lands on.....' + result[random.randint(0, len(result)- 1)] + '!']
#         return phrase
    
#     # Return an 8ball answer
#     if message.content.startswith('!8ball'):
#         phrase = [username + ' shakes the ball hard, it responds: ' + ball[random.randint(0, len(ball) - 1)]]
#         return phrase
    
#     # Return prediction of day
#     if message.content == '!day':
#         phrase = [username + ', today will be ' + day[random.randint(0, len(day) - 1)]]
#         return phrase