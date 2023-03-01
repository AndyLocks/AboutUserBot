import discord
from discord.ext import commands
from bot_init import bot
from basa.basa import Members, Basa
from os import remove

async def removeRoleWithInfo(ctx: commands.context.Context, userId: int):
    if not await Basa.isMemberInBasa(id=userId):
        await ctx.send("User not in database", ephemeral=True)
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
    await ctx.send(embed=emb, ephemeral=True, view=view)

@bot.hybrid_group(name="delete", description = "Delete user", fallback="me")
async def deleteUser(ctx: commands.context.Context):
    await removeRoleWithInfo(ctx=ctx, userId=ctx.author.id)

@deleteUser.command(name="user", description = "Delete user")
async def deleteUserById(ctx: commands.context.Context, user: discord.User):
    await removeRoleWithInfo(ctx=ctx, userId=user.id)

aboba = discord.Embed()
aboba.set_footer(
    
)