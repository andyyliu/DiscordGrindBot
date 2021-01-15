import discord, datetime
from datetime import date, datetime
from discord.ext import commands

class Date(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Generate current date
    @commands.command()
    async def date(self, ctx):
        username = ctx.author.mention
        today = date.today()
        format_today = today.strftime('%B %d. %Y')
        await ctx.send(username + ', today\'s date is ' + format_today)
    
    @commands.command()
    async def time(self, ctx):
        username = ctx.author.mention
        now = datetime.now()
        format_now = now.strftime('%I:%M:%-S %p')
        await ctx.send(username + ', the current time is ' + format_now)

    @commands.command()
    async def today(self, ctx):
        username = ctx.author.mention
        now = datetime.now()
        format_now = now.strftime('%c')
        await ctx.send(username + ': ' + format_now)

# Add class to bot
def setup(bot):
    bot.add_cog(Date(bot))
