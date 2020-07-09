import re
from pprint import pprint

import discord
from discord import Message
from discord.abc import GuildChannel
from discord.ext import commands

from settings import get_channel
import emoji


class Hangout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def extract_emojis(self, s: str):
        main_list = []
        list = [c for c in s if c in emoji.UNICODE_EMOJI]
        custom_emojis = re.findall(r'<:\w*:\d*>', s)
        list_place = {emoji: s.find(emoji) for emoji in list}
        custom_place = {emoji: s.find(emoji) for emoji in custom_emojis}
        all_dict = dict(list_place, **custom_place)
        all_list = sorted(all_dict.items(), key=lambda k: k[1])
        all_list = [s[0] for s in all_list]
        for i in range(0, len(all_list)):
            if len(all_list[i]) > 1:
                all_list[i] = int(all_list[i].split(':')[2].replace('>', ''))
                all_list[i] = self.bot.get_emoji(all_list[i])
        return all_list

    @commands.command()
    async def poll(self, ctx, *, text):
        channel: GuildChannel = await self.bot.fetch_channel(get_channel())
        message: Message = await channel.send(text)
        content = self.extract_emojis(message.content)
        emoji = []
        emoji += content
        for emoj in emoji:
            await message.add_reaction(emoj)
