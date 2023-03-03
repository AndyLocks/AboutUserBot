import discord
from discord.ext import commands
from ..help_group import help

@help.command(name="delete_me")
async def helpDeleteMe(ctx: commands.context.Context):
    emb = discord.Embed(
        color=discord.Color.green(),
        title="delete me",
        description="</delete me:1080574945110786048> - Deletes the user from the database that called the command."
    )

    await ctx.send(embed=emb)