from bot_init import *
import errors.on_command_error
import about_group.groups.author_icon
import about_group.groups.author_title
import about_group.groups.author_url
import about_group.groups.body_url
import about_group.groups.color
import about_group.groups.description
import about_group.groups.footer_icon
import about_group.groups.footer_title
import about_group.groups.image
import about_group.groups.image_thumbnail
import about_group.groups.title

import context_menus.about_user_context_menu
import context_menus.set_title_context_menu
import context_menus.set_image_context_menu
import context_menus.set_description_context_menu
import context_menus.set_author_icon_context_menu
import context_menus.set_author_title_context_menu
import context_menus.delete_user_context_manu

import help_group.groups.user
import help_group.groups.title
import help_group.groups.description
import help_group.groups.author_title
import help_group.groups.author_icon
import help_group.groups.author_url
import help_group.groups.image
import help_group.groups.image_thumbnail
import help_group.groups.body_url
import help_group.groups.footer_title
import help_group.groups.footer_icon
import help_group.groups.color

import help_group.groups.delete_me
import help_group.groups.delete_user


import commands.delete

import events.activity


#@bot.listen()
#async def on_ready():
#    await bot.tree.sync()

bot.run("")