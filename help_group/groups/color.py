import discord
from discord.ext import commands
from ..help_group import help

@help.command(name="about_color")
async def helpAboutColor(ctx: commands.context.Context):


    emb = discord.Embed(
        color=discord.Color.green(),
        title="about color",
        description="</about color:1081294170917965894> - Sets the color of the bar on the right"
    )
    
    emb.add_field(
        name="Arguments",
        value="`color` - The color you want to set. Words can also be colors(red, dark blue)"
    )
    
    await ctx.send(embed=emb)