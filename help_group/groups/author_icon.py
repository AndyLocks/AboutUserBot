import discord
from discord.ext import commands
from ..help_group import help

@help.command(name="about_author_icon")
async def helpAboutAuthorIcon(ctx: commands.context.Context):


    emb = discord.Embed(
        color=discord.Color.green(),
        title="about author_icon",
        description="</about author_icon:1081294170917965894> - Set value as author icon."
    )
    
    emb.add_field(
        name="Arguments",
        value="`value` - The value that can be set. Calling the command without an argument will remove the author icon from the body."
    )
    
    await ctx.send(embed=emb)