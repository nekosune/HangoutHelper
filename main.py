import discord
from discord.ext import commands
import logging

from hangout import Hangout
from settings import get_prefix, load_configs, get_key

load_configs()
bot = commands.Bot(command_prefix=get_prefix(), description='Hangout Helper',
                   activity=discord.Game(name="stuff",
                                         emoji={'id': 712147816893644800, 'name': 'snoo_dealwithit2'}))
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot.add_cog(Hangout(bot))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bot.run(get_key())  # main