import discord
from discord.ext import commands
from bot_init import bot
from funcs.get_about_embed import getAboutEmbed
from basa.basa import Basa
from os import remove


@bot.hybrid_group(name="about", description = "This command writes the information you have added", fallback="user")
async def about(ctx: commands.context.Context, user: discord.User):
    if await Basa.isMemberInBasa(id=user.id):
        emb = await getAboutEmbed(userid=user.id)
        if emb.title == None and\
            emb.description == None and\
            emb.footer.icon_url  == None and\
            emb.footer.text == None and\
            emb.author.url  == None and\
            emb.author.icon_url == None and\
            emb.thumbnail.url == None and\
            emb.url  == None and\
            emb.author.name  == None:
            remove(f"members/member{user.id}.pickle")

            await ctx.send("User is not in database", ephemeral=True)
            return
        
        await ctx.send(embed=emb)
    else:
        await ctx.send("User is not in database", ephemeral=True)