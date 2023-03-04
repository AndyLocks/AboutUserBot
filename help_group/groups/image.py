import discord
from discord.ext import commands
from ..help_group import help

@help.command(name="about_image")
async def helpAboutImage(ctx: commands.context.Context):


    emb = discord.Embed(
        color=discord.Color.green(),
        title="about image",
        description="</about image:1081294170917965894> - Set file as image."
    )
    
    emb.add_field(
        name="Arguments",
        value="`file` - The value that can be set. Calling the command without an argument will remove the image from the body."
    )
    
    await ctx.send(embed=emb)