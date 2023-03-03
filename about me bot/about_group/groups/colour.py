import discord
from discord.ext import commands
from basa.basa import Basa
from basa.members import Members
from ..about_me import about
from funcs.get_about_embed import getAboutEmbed

@about.command(name="colour", description="set Colour")
async def setBodyColour(ctx: commands.context.Context, colour: discord.Colour):
    authorId = ctx.author.id
    if not await Basa.isMemberInBasa(id=authorId):
        await Basa.makeNewMember(id=authorId)

    member: Members = await Basa.getMember(id=authorId)
    member.body_color = colour
    await Basa.updateMember(
        id=authorId,
        member=member
    )
    await ctx.send(
        "The message has been updated✅",
        ephemeral=True,
        embed= await getAboutEmbed(userid=ctx.author.id)
    )