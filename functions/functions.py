import discord
from discord.ext import commands
from discord import app_commands
import sqlite3

class Functions(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.db = sqlite3.connect('functions/sheets-bot.db')
        self.c = self.db.cursor()

    def get_function_embed(self, type, command):
        # clean
        command = command.upper()
        self.c.execute(f'SELECT * FROM {type} WHERE name = ?', (command,))
        result = self.c.fetchone()
        if result is None:
            return None

        # description should be
        # Category: {type}
        # Syntax: [`{syntax}`](<{link}>)
        # {description}
        description = f'''
        **Category**: {result[2]}
        **Syntax**: [`{result[3]}`]({result[5]})
        {result[4]}
        '''

        embed = discord.Embed(
            title=result[1],
            description=description,
            color=discord.Color.green()
        )

        return embed

    @commands.hybrid_command(name='gsheets')
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def gsheets(self, ctx, command):
        embed = self.get_function_embed('sheets', command)

        await ctx.send(embed=embed)
    
    @commands.hybrid_command(name='excel')
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def excel(self, ctx, command):
        embed = self.get_function_embed('excel', command)

        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Functions(client))
