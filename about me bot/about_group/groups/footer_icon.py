import discord
from discord.ext import commands
from basa.basa import Basa
from basa.members import Members
from ..about_me import about
from funcs.get_about_embed import getAboutEmbed

@about.command(name="footer_icon", description="set footer icon")
async def setFooterIcon(ctx: commands.context.Context, file: discord.Attachment | None):
    authorId = ctx.author.id
    if not await Basa.isMemberInBasa(id=authorId):
        await Basa.makeNewMember(id=authorId)


    member: Members = await Basa.getMember(id=authorId)
    
    if file == None:
        member.footer_icon = None
    else:
        member.footer_icon = file.url
    
    text = "The message has been updated✅"
    if member.footer_title == None:
        text = "The message has been updated✅\n\n⚠️Footer title is empty. The message will not display a icon without text.\n</about footer_title:1080568761637142580>"

    
    await Basa.updateMember(
        id=authorId,
        member=member
    )
    await ctx.send(
        text,
        ephemeral=True,
        embed=await getAboutEmbed(userid=ctx.author.id)
    )