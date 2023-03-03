import discord
from discord.ext import commands
from bot_init import bot

@bot.group(name="help")
async def help(ctx: commands.context.Context):
    emb = discord.Embed(
        color=discord.Color.green(),
        description="Do `.help` <command> for extended information on a command.\n\
            Example:\n\
            `.help about_user`\n\
            `.help delete_me`\n\n\n\
            </about user:1080568761637142580> - User information.\n\
            </about title:1080568761637142580> - Set title\n\
            </about description:1080568761637142580> - Set description\n\
            </about author_title:1080568761637142580> - Set author title\n\
            </about author_icon:1080568761637142580> - Set author icon\n\
            </about author_url:1080568761637142580> - Set author url\n\
            </about image:1080568761637142580> - Set image\n\
            </about thumbnail_image:1080568761637142580> - Set image thumbnail\n\
            </about body_url:1080568761637142580> - Set body url\n\
            </about footer_title:1080568761637142580> - Set footer title\n\
            </about color:1080568761637142580> - Sets the color of the bar on the right\n\
            </about footer_icon:1080568761637142580> - Set footer icon\n\n\
            </delete me:1080574945110786048> - Removes the person from the database who called the command\n\
            </delete user:1080574945110786048> - Deletes the given user from the database. Only administrators can use this command."
    )
    emb2 = discord.Embed(
        title="Context menu",
        color=discord.Color.green()
    )
    emb2.add_field(
        name="User",
        value="`about user` - Displays information added by the user.\n\n\
            `delete user` - Deletes a user. Administrators can use it for all members. And not administrators, only to yourself."
    )
    emb2.add_field(
        name="Message",
        value="`set as title` - Sets the selected message as title\n\n\
            `set as description` - Sets the selected message as description\n\n\
            `set as image` - Sets the first photo in the selected message\n\n\
            `set as authors title` - Sets the selected message as the author's title\n\n\
            `aet as authors icon` - Sets the first photo in the selected message as the author icon"
    )
    emb.set_author(
        name="AboutUser",
        icon_url=bot.application.icon.url
    )
    
    await ctx.send(embeds=[emb, emb2])