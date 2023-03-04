import discord
from discord.ext import commands
from discord import app_commands
from bot_init import bot
from funcs.get_about_embed import getAboutEmbed
from basa.basa import Basa
from basa.basa import Basa, Members
from os import remove

async def deleteUserContextMenu(interaction: discord.Interaction, user: discord.User):


    if not interaction.user.guild_permissions.administrator and not interaction.user.id == user.id:
        await interaction.response.send_message("You are not an administrator", ephemeral=True)
        return

    userId = user.id
    if not await Basa.isMemberInBasa(id=userId):
        await interaction.response.send_message("User not in database", ephemeral=True)
        return
    
    emb = discord.Embed(
            title="**Attention!!!**",
            description="Are you sure?",
            color=discord.Color.yellow()
        )
    
    view = discord.ui.View()
    
    button_yes = discord.ui.Button(
        emoji="✅",
        label="Yes"
    )
    
    button_no = discord.ui.Button(
        emoji="❌",
        label="No"
    )
    
    async def result_yes(interaction: discord.Interaction):
        emb = discord.Embed(
            title="Ready",
            description="The user has been removed from the database.",
            color=discord.Color.green()
        )

        remove(f"members/member{userId}.pickle")

        await interaction.response.edit_message(embed=emb, view=None)
    
    async def result_no(interaction: discord.Interaction):
        await interaction.response.edit_message(content="Deletion has been canceled.", view=None, embed=None)
    
    button_yes.callback = result_yes
    button_no.callback = result_no

    view.add_item(button_yes)
    view.add_item(button_no)
    await interaction.response.send_message(embed=emb, ephemeral=True, view=view)


delete_user_context_menu = app_commands.ContextMenu(
    name="delete user",
    callback=deleteUserContextMenu,
    type=discord.AppCommandType.user
)

bot.tree.add_command(delete_user_context_menu)