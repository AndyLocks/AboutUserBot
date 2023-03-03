import discord
from discord.ext import commands
from ..help_group import help

@help.command(name="about_footer_title")
async def helpAboutFooterTitle(ctx: commands.context.Context):
    emb = discord.Embed(
        color=discord.Color.green(),
        title="about footer_title",
        description="</about footer_title:1080568761637142580> - Sets the value as the footer title."
    )
    emb.add_field(
        name="Arguments",
        value="`value` - The value that can be set. Calling the command without an argument will remove the footer title from the body."
    )
    await ctx.send(embed=emb)