import discord
from discord import app_commands
from bot_init import bot
from basa.basa import Basa
from basa.basa import Members
from funcs.get_about_embed import getAboutEmbed

async def authorIconContextMenu(interaction: discord.Interaction, message: discord.Message):
    if len(message.attachments) == 0:
        await interaction.response.send_message("The message has no pictures ❌", ephemeral=True)
        return
    
    if len(message.embeds) != 0:
        await interaction.response.send_message("The selected message cannot be selected as a authors image ❌", ephemeral=True)
        return

    
    emb = discord.Embed(
            title="**Attention!!!**",
            description=f"Are you sure that you want to change the author icon to:",
            color=discord.Color.yellow()
        )
    emb.set_image(url=message.attachments[0].url)
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
            description=f"Image has been changed to:",
            color=discord.Color.green()
        )
        emb.author.icon_url = message.attachments[0].url

        authorId = interaction.user.id
        if not await Basa.isMemberInBasa(id=authorId):
            await Basa.makeNewMember(id=authorId)

        member: Members = await Basa.getMember(id=authorId)
        member.author_icon = message.attachments[0].url
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
    


author_icon_context_menu = app_commands.ContextMenu(
    name="set author icon",
    callback=authorIconContextMenu
)
bot.tree.add_command(author_icon_context_menu)