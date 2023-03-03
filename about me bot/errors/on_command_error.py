import discord
from discord.ext import commands
from bot_init import bot

@bot.listen()
async def on_command_error(ctx: commands.context.Context, error: commands.CommandError):
    if str(error).startswith("Colour"):
        await ctx.send("Unknown colour format ❌", ephemeral=True)

    elif str(error).startswith("Hybrid"):
        emb = discord.Embed(
            title="**Attention!!!**",
            description="Invalid form body.",
            color=discord.Color.red()
        )
    
        await ctx.send(embed=emb, ephemeral=True)
    
    print(error)