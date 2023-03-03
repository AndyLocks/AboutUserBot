import discord
from discord.ext import commands
from ..help_group import help

@help.command(name="about_footer_icon")
async def helpAboutFooterIcon(ctx: commands.context.Context):
    emb = discord.Embed(
        color=discord.Color.green(),
        title="about footer_icon",
        description="</about footer_icon:1080568761637142580> - Set file as footer icon."
    )
    emb.add_field(
        name="Arguments",
        value="`file` - The value that can be set. Calling the command without an argument will remove the footer icon from the body."
    )
    await ctx.send(embed=emb)