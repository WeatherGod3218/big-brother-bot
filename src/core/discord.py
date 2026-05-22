import discord
import asyncio
import random

from modules import taskmanager
from logging import getLogger, Logger
from config import DISCORD_BOT_TOKEN
from discord.ext import commands
from pathlib import Path

logger: Logger = getLogger(__name__)
# Required for reading message content
intents = discord.Intents.default()
intents.message_content = True

bot: commands.Bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

image_amount: int = 0 # The amount of images of the man

@bot.event
async def on_ready() -> None:
    """
    Logging for when the bot has been initalized
    """
    logger.info(f"Bot has been signed in as {bot.user}")

@bot.command()
async def ping(ctx: commands.Context) -> None:
    """
    Replies with pong, simple health check

    Arguments:
        ctx (commands.Context): The discord bot context
    """
    await ctx.send("Pong!")

@bot.event
async def on_message(message: discord.Message) -> None:
    """
    Checks message to see if it mentions the bot, if so responds with a random image of the man

    Arguments:
        message (discord.Message): The messages context
    """
    global image_amount

    if message.author.bot:
        return

    if bot.user in message.mentions:
        await message.channel.send(
            file=discord.File(f"images/man_images/theman{random.randint(1,image_amount)}.png")
        )

    await bot.process_commands(message)

async def init_discord_bot() -> None:
    """
    Initalizes the discord bot, using the discord bot token found in the .env file
    """
    global image_amount

    logger.info("Initalizing Discord Bot!")

    image_amount = len([f for f in Path("./images/man_images").rglob('*') if f.is_file()])
    try:
        taskmanager.create_background_task(bot.start(DISCORD_BOT_TOKEN))
    except Exception as e:
        logger.error(f"Failed to initialize the discord bot with the error {e}")
