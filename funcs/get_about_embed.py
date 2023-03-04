import discord
from discord.ext import commands
from basa.members import Members
from basa.basa import Basa

async def getAboutEmbed(userid: int) -> discord.Embed:
    """Fills Embed with information from the user found by id and returns it."""

    member: Members = await Basa.getMember(id=userid)

    embed: discord.Embed = discord.Embed(
        color=member.body_color,
        title=member.body_title,
        description=member.body_description,
        url=member.body_url
    )

    embed.set_image(url=member.image_url)
    embed.set_thumbnail(url=member.image_thumbnail)
    
    if member.author_title != None:
        embed.set_author(
            name=member.author_title,
            url=member.author_url,
            icon_url=member.author_icon
        )
    
    embed.set_footer(
        text=member.footer_title,
        icon_url=member.footer_icon
    )

    return embed