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
            description="Body is empty. Set some text.\n\
                </about title:1080568761637142580>\n\
                    </about description:1080568761637142580>",
            color=discord.Color.red()
        )
    
        await ctx.send(embed=emb, ephemeral=True)
    
    print(error)