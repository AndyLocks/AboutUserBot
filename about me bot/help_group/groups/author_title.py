import discord
from discord.ext import commands
from ..help_group import help

@help.command(name="about_author_title")
async def helpAboutAuthorTitle(ctx: commands.context.Context):
    emb = discord.Embed(
        color=discord.Color.green(),
        title="about author_title",
        description="</about author_title:1080568761637142580> - Set value as author title."
    )
    emb.add_field(
        name="Arguments",
        value="`value` - The value that can be set. Calling the command without an argument will remove the author title from the body."
    )
    await ctx.send(embed=emb)