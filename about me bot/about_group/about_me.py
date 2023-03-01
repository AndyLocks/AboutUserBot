import discord
from discord.ext import commands
from bot_init import bot
from funcs.get_about_embed import getAboutEmbed
from basa.basa import Basa


@bot.hybrid_group(name="about", description = "This command writes the information you have added", fallback="user")
async def about(ctx: commands.context.Context, user: discord.User):
    if await Basa.isMemberInBasa(id=user.id):
        await ctx.send(embed=await getAboutEmbed(userid=user.id))
    else:
        await ctx.send("User is not in database", ephemeral=True)