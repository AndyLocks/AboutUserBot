import discord
from discord.ext import commands
from bot_init import bot

@bot.listen()
async def on_command_error(ctx: commands.context.Context, error: commands.CommandError):
    if str(error).startswith("Colour"):
        await ctx.send("Unknown colour format ❌", ephemeral=True)