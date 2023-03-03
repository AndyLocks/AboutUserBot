import discord
from discord.ext import commands
from ..help_group import help

@help.command(name="about_body_url")
async def helpAboutBodyUrl(ctx: commands.context.Context):
    emb = discord.Embed(
        color=discord.Color.green(),
        title="about body_url",
        description="</about body_url:1080568761637142580> - Set value as body url."
    )
    emb.add_field(
        name="Arguments",
        value="`value` - The value that can be set. Calling the command without an argument will remove the body url from the body."
    )
    await ctx.send(embed=emb)