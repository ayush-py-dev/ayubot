
import discord
from dotenv import load_dotenv

load_dotenv()

# ---------------------- bot ---------------------- #

INTENTS = discord.Intents.all()

# BOT_COMMAND_PREFIX = os.getenv('prefix')
BOT_COMMAND_PREFIX = "!"

BOT_STATUS = discord.Status.idle

BOT_ACTIVITY = discord.Activity(
    type=discord.ActivityType.watching, name="my development"
)


# ---------------------- db ---------------------- #

AFK_CONFIG_SCHEMA = """
CREATE TABLE IF NOT EXISTS afk (
        user_id BIGINT,
        afk_reason TEXT,
        time BIGINT
    )
"""
