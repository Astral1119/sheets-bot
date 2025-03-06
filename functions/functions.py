import discord
from discord.ext import commands
import sqlite3

class Functions(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.db = sqlite3.connect('functions/sheets-bot.db')
        self.c = self.db.cursor()

    @commands.hybrid_command(name='gsheets')
    async def gsheets(self, ctx, command):
        # clean
        command = command.upper()
        self.c.execute('SELECT * FROM sheets WHERE name = ?', (command,))
        result = self.c.fetchone()
        if result is None:
            await ctx.send('Command not found')
            return
        
        # description should be
        # Category: {type}
        # Syntax: [`{syntax}`](<{link}>)
        # {description}
        description = f'''Category: {result[2]}
        Syntax: [`{result[3]}`]({result[5]})
        {result[4]}'''

        embed = discord.Embed(
            title=result[1],
            description=description,
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)
    
    @commands.hybrid_command(name='excel')
    async def excel(self, ctx, command):
        # clean
        command = command.upper()
        self.c.execute('SELECT * FROM excel WHERE name = ?', (command,))
        result = self.c.fetchone()
        if result is None:
            await ctx.send('Command not found')
            return
        
        # description should be
        # Category: {type}
        # Syntax: [`{syntax}`](<{link}>)
        # {description}
        description = f'''Category: {result[2]}
        Syntax: [`{result[3]}`]({result[5]})
        {result[4]}'''

        embed = discord.Embed(
            title=result[1],
            description=description,
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Functions(client))