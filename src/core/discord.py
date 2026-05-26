import discord

from modules import taskmanager
from logging import getLogger, Logger
from config import DISCORD_BOT_TOKEN, GUILD_ID
from discord.ext import commands
from pathlib import Path

logger: Logger = getLogger(__name__)

intents = discord.Intents.default()
intents.message_content = True

class BigBrother(commands.Bot):
    async def setup_hook(self):
        await self.load_extension("cogs.nullscape")
        await self.load_extension("cogs.theman")


        await self.tree.sync()

    async def on_ready(self):
        logger.info(f"Logged in as {self.user}")


bot = BigBrother(command_prefix="!", intents=intents)

@bot.command(aliases=["health"])
async def ping(ctx: commands.Context) -> None:
    """
    Replies with pong, simple health check

    Arguments:
        ctx (commands.Context): The discord bot context
    """
    await ctx.send("Pong!")

async def init_discord_bot() -> None:
    """
    Initalizes the discord bot, using the discord bot token found in the .env file
    """
    try:
        await taskmanager.create_background_task(bot.start(DISCORD_BOT_TOKEN))
    except Exception as e:
        logger.error(f"Failed to initialize the discord bot with the error {e}")
