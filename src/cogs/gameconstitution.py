import discord
from discord import app_commands
from discord.ext import commands

from logging import getLogger, Logger

from config import BASE_DIR

logger: Logger = getLogger(__name__)

CONSTITUTION = """
The Constitution of The "Video Games OST OAT" Playlist
- Every Collaborator is permitted to add songs at free will
- Songs in the playlist must have been featured prominetly in Video Games
   	"Example: Jumper from GD/Castle Crasher"
- "Now or Never" Is grandfathered in the Constitution
- If Majority vote to banish a song from the playlist there shall be no backlash
- No duplicates of songs. 
   	"Example: Monochrome, and Monochrome (INSTRUMENTAL) are considered to be dupe"
- Remixes are Permitted 
"""
class VideoGameOSTs(commands.Cog):
    """
    Cog used for the video games OAT
        - Sends image of Kolonas 14 when asked (Inside joke)
    """
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="constitution", description="The Video Game OST OAT Rules")
    async def constitution(self, interaction: discord.Interaction):
        """
        Responds with an image of 14. Based off an inside joke during a nullscape run

        Arguments:
            ctx (commands.Context): The context of the message
        """
        await interaction.response.send_message(f"{CONSTITUTION}")

async def setup(bot):
    await bot.add_cog(VideoGameOSTs(bot))