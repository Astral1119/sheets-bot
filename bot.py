import dotenv
import discord
from discord.ext import commands
import os

dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='=', intents=intents)

async def load_cogs():
    await bot.load_extension('parrot.parrot')
    await bot.load_extension('functions.functions')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await load_cogs()

    # sync commands
    try:
        await bot.tree.sync()
    except Exception as e:
        print(e)
    
    print('Bot is ready')

bot.run(TOKEN)