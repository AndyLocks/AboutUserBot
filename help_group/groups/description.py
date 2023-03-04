import discord
from discord.ext import commands
from ..help_group import help

@help.command(name="about_description")
async def helpAboutDescription(ctx: commands.context.Context):


    emb = discord.Embed(
        color=discord.Color.green(),
        title="about description",
        description="</about description:1081294170917965894> - Sets the value as the description."
    )
    
    emb.add_field(
        name="Arguments",
        value="`value` - The value that can be set. Calling the command without an argument will remove the description from the body."
    )
    
    await ctx.send(embed=emb)