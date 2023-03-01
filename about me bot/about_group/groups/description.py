import discord
from discord.ext import commands
from basa.basa import Basa
from basa.members import Members
from ..about_me import about

@about.command(name="description", description="set description")
async def setDescription(ctx: commands.context.Context, value: str):
    authorId = ctx.author.id
    if not await Basa.isMemberInBasa(id=authorId):
        await Basa.makeNewMember(id=authorId)

    member: Members = await Basa.getMember(id=authorId)
    member.body_description = value
    await Basa.updateMember(
        id=authorId,
        member=member
    )
    try: 
        await ctx.message.add_reaction("✅")
    except discord.errors.NotFound:
        await ctx.send("✅", ephemeral=True)