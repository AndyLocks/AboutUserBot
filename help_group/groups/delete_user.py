import discord
from discord.ext import commands
from ..help_group import help

@help.command(name="delete_user")
async def helpDeleteUser(ctx: commands.context.Context):


    emb = discord.Embed(
        color=discord.Color.green(),
        title="delete user",
        description="</delete user:1081294170917965895> - Deletes the user specified as an argument from the database."
    )
    
    emb.add_field(
        name="Arguments",
        value="`user` - The person you want to delete."
    )
    
    await ctx.send(embed=emb)