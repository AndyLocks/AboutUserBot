import discord
from discord.ext import commands
from basa.basa import Basa
from basa.members import Members
from ..about_me import about
from funcs.get_about_embed import getAboutEmbed

@about.command(name="author_icon", description="set author icon")
async def setAuthorIcon(ctx: commands.context.Context, file: discord.Attachment | None):
    authorId = ctx.author.id
    if not await Basa.isMemberInBasa(id=authorId):
        await Basa.makeNewMember(id=authorId)

    member: Members = await Basa.getMember(id=authorId)
    if file == None:
        member.author_icon = None
    else:
        member.author_icon = file.url
    
    await Basa.updateMember(
        id=authorId,
        member=member
    )
    text = "The message has been updated✅"
    if member.author_title == None:
        text = "The message has been updated✅\n\n⚠️Author title is empty. The message will not display a icon without text.\n</about author_title:1080568761637142580>"
    await ctx.send(
        text,
        ephemeral=True,
        embed= await getAboutEmbed(userid=ctx.author.id)
    )