import discord
from discord.ext import commands
from basa.basa import Basa
from basa.members import Members
from ..about_me import about
from funcs.get_about_embed import getAboutEmbed

@about.command(name="author_url", description="set author url")
async def setAuthorUrl(ctx: commands.context.Context, value: str | None):
    if not value.startswith("http") and value != None:
        await ctx.send("Url link is not correct ❌", ephemeral=True)
        return

    authorId = ctx.author.id
    if not await Basa.isMemberInBasa(id=authorId):
        await Basa.makeNewMember(id=authorId)

    member: Members = await Basa.getMember(id=authorId)

    olderAuthorUrl = member.author_url
    member.author_url = value
    await Basa.updateMember(
        id=authorId,
        member=member
    )
    try:
        text = "The message has been updated✅"
        if member.author_title == None:
            text = "The message has been updated✅\n\n⚠️Author title is empty. The message will not display a icon without text.\n</about author_title:1080568761637142580>"
        await ctx.send(
            text,
            ephemeral=True,
            embed= await getAboutEmbed(userid=ctx.author.id)
        )
    except:
        member.author_url = olderAuthorUrl
        await Basa.updateMember(id=ctx.author.id, member=member)
        await ctx.send("Invalid url ❌", ephemeral=True)