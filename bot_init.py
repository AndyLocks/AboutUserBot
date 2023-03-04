import discord
from discord.ext import commands

bot = commands.Bot(
    command_prefix = ".",
    intents = discord.Intents.all(),
    status=discord.Status.idle
)

bot.help_command = None