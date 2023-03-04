import discord
from discord.ext import commands
from ..help_group import help

@help.command(name="about_user")
async def helpAboutUser(ctx: commands.context.Context):

    emb = discord.Embed(
        color=discord.Color.green(),
        title="about user",
        description="</about user:1081294170917965894> - Displays information added by the user."
    )
    
    emb.add_field(
        name="Arguments",
        value="`user` - The user whose information you want to display."
    )
    
    await ctx.send(embed=emb)