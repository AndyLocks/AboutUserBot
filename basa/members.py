import discord
from discord.ext import commands
from dataclasses import dataclass


@dataclass
class Members:
    body_title: str | None = None
    body_description: str | None = None
    body_url: str | None = None
    body_color: discord.Colour = discord.Colour.green()
    author_title: str | None = None
    author_url: str | None = None
    author_icon: str | None = None
    image_url: str | None = None
    image_thumbnail: str | None = None
    footer_title: str | None = None
    footer_icon: str | None = None