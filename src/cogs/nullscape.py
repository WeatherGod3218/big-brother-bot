import discord
from discord import app_commands
from discord.ext import commands

from logging import getLogger, Logger

from config import BASE_DIR

logger: Logger = getLogger(__name__)

class Kolona(commands.Cog):
    """
    Cog used for all Nullscape related content. Currently has
        - Sends image of Kolonas 14 when asked (Inside joke)
    """
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="whatsmynumber", description="Ask Kolona to Remind you of your Number!")
    async def num(self, interaction: discord.Interaction):
        """
        Responds with an image of 14. Based off an inside joke during a nullscape run

        Arguments:
            ctx (commands.Context): The context of the message
        """
        await interaction.response.send_message(file=discord.File(f"{BASE_DIR}/images/kolona14.png"))

async def setup(bot):
    await bot.add_cog(Kolona(bot))