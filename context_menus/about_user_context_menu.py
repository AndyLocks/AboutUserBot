import discord
from discord.ext import commands
from discord import app_commands
from bot_init import bot
from funcs.get_about_embed import getAboutEmbed
from basa.basa import Basa
from basa.basa import Basa, Members
from os import remove

async def aboutUserContextMenu(interaction: discord.Interaction, user: discord.User):


    if await Basa.isMemberInBasa(id=user.id):
        
        emb = await getAboutEmbed(userid=user.id)
        if emb.title == None and\
            emb.description == None and\
            emb.image.url == None and\
            emb.footer.icon_url  == None and\
            emb.footer.text == None and\
            emb.author.url  == None and\
            emb.author.icon_url == None and\
            emb.thumbnail.url == None and\
            emb.url  == None and\
            emb.author.name  == None:
            remove(f"members/member{user.id}.pickle")

            await interaction.response.send_message("User is not in database", ephemeral=True)
            return
        
        await interaction.response.send_message(f"**{user.name}**", embed=emb)
    else:
        await interaction.response.send_message("User is not in database", ephemeral=True)


about_user_context_menu = app_commands.ContextMenu(
    name="about user",
    callback=aboutUserContextMenu,
    type=discord.AppCommandType.user
)

bot.tree.add_command(about_user_context_menu)