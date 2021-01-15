import discord, random
from words import ball, day
from discord.ext import commands
from messages import get_quote


class Decisions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # Generate a random dice roll (numbers from 1-6)
    @commands.command()
    async def dice(self, ctx):
        username = ctx.author.mention
        await ctx.send(username + ' takes a deep breath, and rolls the die, the number is.....' + str(random.randint(1, 6)) + '!')
    

    # Generate a random coin flip (heads, tails, or edge(~1/6000))
    @commands.command()
    async def coin(self, ctx):
        username = ctx.author.mention
        outcomes = ['heads', 'tails', 'its edge, OMG THAT\'S 1 in 6000']
        rand = random.randint(0, 6000)
        result = ''
        if rand == 0:
            result = outcomes[2]
        elif rand % 2 == 0:
            result = outcomes[0]
        else:
            result = outcomes[1]
        await ctx.send(username + ' flips the coin as high as possible, it lands on.....' + result + '!')    


    # Generate a random forecast of user's day
    @commands.command()
    async def day(self, ctx):
        username = ctx.author.mention
        await ctx.send(username + ', today will be ' + day[random.randint(0, len(day)-1)])


    # Generate a random 8ball answer
    @commands.command(name='8ball')
    async def _8ball(self, ctx):
        username = ctx.author.mention
        await ctx.send(username + ' shakes the ball hard, it responds: ' + ball[random.randint(0, len(ball) - 1)])


    # Generate a random motivational quote
    @commands.command()
    async def quote(self, ctx):
        await ctx.send(get_quote())


# Add class to bot
def setup(bot):
    bot.add_cog(Decisions(bot))