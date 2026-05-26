import discord
import random

from pathlib import Path
from logging import getLogger, Logger

from discord.ext import commands
from config import BASE_DIR

logger: Logger = getLogger(__name__)

the_man_images: list[Path] = []

def load_theman_images() -> None:
    """
    Loads all of "The Man" Images from the directory found in images/man_images
    """

    global the_man_images
    the_man_images = [f for f in Path(f"{BASE_DIR}/images/man_images").rglob('*') if f.is_file()]
    logger.info("Loaded Image Files Successfully!")
    
class TheMan(commands.Cog):
    """
    Cog used for all of "The Man" Commands. Currently has:
    - Sends Image when pinged
    """
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        """
        Checks each message that is sent, and sees if it needs to send an image of the man

        Arguments:
            message (discord.Message): The context of the message that was sent
        """
        global the_man_images

        if message.author.bot or len(the_man_images) == 0:
            return

        if self.bot.user in message.mentions:
            await message.channel.send(
                file=discord.File(str(random.choice(the_man_images)))
            )

async def setup(bot: commands.Bot):
    load_theman_images()
    await bot.add_cog(TheMan(bot))