import discord
from discord.ext import commands
from discord import app_commands
from bot_init import bot
from funcs.get_about_embed import getAboutEmbed
from basa.basa import Basa

async def aboutUserContextMenu(interaction: discord.Interaction, user: discord.User):
    if await Basa.isMemberInBasa(id=user.id):
        await interaction.response.send_message(embed=await getAboutEmbed(userid=user.id))
    else:
        await interaction.response.send_message("User is not in database", ephemeral=True)

about_user_context_menu = app_commands.ContextMenu(
    name="about user",
    callback=aboutUserContextMenu,
    type=discord.AppCommandType.user
)
bot.tree.add_command(about_user_context_menu)