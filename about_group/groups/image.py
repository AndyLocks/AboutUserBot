import discord
from discord.ext import commands
from basa.basa import Basa
from basa.members import Members
from ..about_me import about
from funcs.get_about_embed import getAboutEmbed

@about.command(name="image", description="set image")
async def setImage(ctx: commands.context.Context, file: discord.Attachment | None):


    authorId = ctx.author.id

    if not await Basa.isMemberInBasa(id=authorId):
        await Basa.makeNewMember(id=authorId)

    member: Members = await Basa.getMember(id=authorId)
    
    if file == None:
        member.image_url = None
    
    else:
        member.image_url = file.url

    await Basa.updateMember(
        id=authorId,
        member=member
    )
    
    await ctx.send(
        "The message has been updated✅",
        ephemeral=True,
        embed= await getAboutEmbed(userid=ctx.author.id)
    )