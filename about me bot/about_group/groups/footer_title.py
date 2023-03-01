import discord
from discord.ext import commands
from basa.basa import Basa
from basa.members import Members
from ..about_me import about

@about.command(name="footer_title", description="set footer title")
async def setFooterTitle(ctx: commands.context.Context, value: str):
    authorId = ctx.author.id
    if not await Basa.isMemberInBasa(id=authorId):
        await Basa.makeNewMember(id=authorId)

    member: Members = await Basa.getMember(id=authorId)
    member.footer_title = value
    await Basa.updateMember(
        id=authorId,
        member=member
    )
    try: 
        await ctx.message.add_reaction("✅")
    except discord.errors.NotFound:
        await ctx.send("✅", ephemeral=True)