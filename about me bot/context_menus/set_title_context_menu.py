import discord
from discord import app_commands
from bot_init import bot
from basa.basa import Basa
from basa.basa import Members
from funcs.get_about_embed import getAboutEmbed

async def titleContextMenu(interaction: discord.Interaction, message: discord.Message):
    if len(message.embeds) != 0:
        await interaction.response.send_message("The selected message cannot be selected as a title ❌", ephemeral=True)
        return

    if len(message.content) > 256:
        await interaction.response.send_message("Text is too long", ephemeral=True)
        return
    
    
    emb = discord.Embed(
            title="**Attention!!!**",
            description=f"Are you sure that you want to change the title to:\n>>> {message.content}",
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
            description=f"Text has been changed to:\n>>> {message.content}",
            color=discord.Color.green()
        )

        authorId = interaction.user.id
        if not await Basa.isMemberInBasa(id=authorId):
            await Basa.makeNewMember(id=authorId)

        member: Members = await Basa.getMember(id=authorId)
        member.body_title = message.content
        await Basa.updateMember(
            id=authorId,
            member=member
        )
        
        await interaction.response.edit_message(embeds=[emb, await getAboutEmbed(userid=interaction.user.id)], view=None)
    
    async def result_no(interaction: discord.Interaction):
        await interaction.response.edit_message(content="Canceled.", view=None, embed=None)
    
    button_yes.callback = result_yes
    button_no.callback = result_no

    view.add_item(button_yes)
    view.add_item(button_no)
    await interaction.response.send_message(embed=emb, ephemeral=True, view=view)
    


title_contetx_menu = app_commands.ContextMenu(
    name="set as title",
    callback=titleContextMenu
)
bot.tree.add_command(title_contetx_menu)