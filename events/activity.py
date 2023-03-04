import discord
from discord.ext import commands
from bot_init import bot

@bot.listen()
async def on_ready():


    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching,
                                name=f"{len(bot.guilds)} guilds"),
        status=discord.Status.idle
    )

@bot.listen()
async def on_guild_join(guild: discord.Guild):


    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching,
                                name=f"{len(bot.guilds)} guilds"),
        status=discord.Status.idle
    )

@bot.listen()
async def on_guild_remove(guild: discord.Guild):

    
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching,
                                name=f"{len(bot.guilds)} guilds"),
        status=discord.Status.idle
    )