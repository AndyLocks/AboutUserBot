import discord
from discord.ext import commands
from basa.basa import Basa
from basa.members import Members
from ..about_me import about
from funcs.get_about_embed import getAboutEmbed

@about.command(name="thumbnail_image", description="set thumbnail image")
async def setThumbnailImage(ctx: commands.context.Context, file: discord.Attachment | None):


    authorId = ctx.author.id

    if not await Basa.isMemberInBasa(id=authorId):
        await Basa.makeNewMember(id=authorId)

    member: Members = await Basa.getMember(id=authorId)
    
    if file == None:
        member.image_thumbnail = None
    
    else:
        member.image_thumbnail = file.url
    
    await Basa.updateMember(
        id=authorId,
        member=member
    )
    
    await ctx.send(
        "The message has been updated✅",
        ephemeral=True,
        embed= await getAboutEmbed(userid=ctx.author.id)
    )