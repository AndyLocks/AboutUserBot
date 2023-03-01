import discord
from discord.ext import commands
from dataclasses import dataclass

@dataclass
class Members:
    body_title: str = None
    body_description: str = None
    body_url: str = None
    body_color: discord.Colour = discord.Colour.green()
    author_title: str = None
    author_url: str = None
    author_icon: str = None
    image_url: str = None
    image_thumbnail: str = None
    footer_title: str = None
    footer_icon: str = None