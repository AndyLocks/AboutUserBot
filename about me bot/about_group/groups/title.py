import discord
from discord.ext import commands
from basa.basa import Basa
from basa.members import Members
from ..about_me import about
from funcs.get_about_embed import getAboutEmbed

@about.command(name="title", description="set title")
async def title(ctx: commands.context.Context, value: str | None):
    if value != None:
        if len(value) > 256:
            await ctx.send("Text is too long", ephemeral=True)
            return

    authorId = ctx.author.id
    if not await Basa.isMemberInBasa(id=authorId):
        await Basa.makeNewMember(id=authorId)

    member: Members = await Basa.getMember(id=authorId)
    member.body_title = value
    await Basa.updateMember(
        id=authorId,
        member=member
    )
    await ctx.send(
        "The message has been updated✅",
        ephemeral=True,
        embed= await getAboutEmbed(userid=ctx.author.id)
    )