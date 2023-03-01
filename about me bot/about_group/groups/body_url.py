import discord
from discord.ext import commands
from basa.basa import Basa
from basa.members import Members
from ..about_me import about

@about.command(name="body_url", description="set body url")
async def setBodyUrl(ctx: commands.context.Context, value: str):
    if not value.startswith("http"):
        await ctx.send("Url link is not correct ❌", ephemeral=True)
        return

    authorId = ctx.author.id
    if not await Basa.isMemberInBasa(id=authorId):
        await Basa.makeNewMember(id=authorId)

    member: Members = await Basa.getMember(id=authorId)
    member.body_url = value
    await Basa.updateMember(
        id=authorId,
        member=member
    )
    try: 
        await ctx.message.add_reaction("✅")
    except discord.errors.NotFound:
        await ctx.send("✅", ephemeral=True)