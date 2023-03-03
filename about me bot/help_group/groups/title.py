import discord
from discord.ext import commands
from ..help_group import help

@help.command(name="about_title")
async def helpAboutTitle(ctx: commands.context.Context):
    emb = discord.Embed(
        color=discord.Color.green(),
        title="about title",
        description="</about title:1080568761637142580> - Sets the value as the title."
    )
    emb.add_field(
        name="Arguments",
        value="`value` - The value that can be set. Calling the command without an argument will remove the title from the body."
    )
    await ctx.send(embed=emb)