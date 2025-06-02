import dotenv
import discord
from discord.ext import commands
import os

dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN') or ''

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='=', intents=intents)

async def load_cogs():
    await bot.load_extension('parrot.parrot')
    await bot.load_extension('functions.functions')
    await bot.load_extension('wiki.search')

@bot.event
async def on_ready():
    assert(bot.user)
    print(f'Logged in as {bot.user.name}')
    await load_cogs()

    # sync commands
    try:
        await bot.tree.sync()
    except Exception as e:
        print(e)
    
    print('Bot is ready')

bot.run(TOKEN)
