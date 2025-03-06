import discord
from discord.ext import commands
import json
import os

class Parrot(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.commands = []

        for filename in os.listdir('parrot'):
            if filename.endswith('.json'):
                command_name = filename[:-5]
                self.commands.append(command_name)
                self.add_parrot_command(command_name)

    def add_parrot_command(self, command_name):
        with open(f'parrot/{command_name}.json') as f:
            command_data = json.load(f)

        async def parrot(ctx):
            description = "\n".join(f'**{label}**: {desc}' for label, desc in command_data.items())
            embed = discord.Embed(
                title=command_name,
                description=description,
                color=discord.Color.green()
            )
            await ctx.send(embed=embed)

        parrot.__name__ = command_name  # Set correct function name
        self.client.add_command(commands.hybrid_command(name=command_name)(parrot))

async def setup(client):
    await client.add_cog(Parrot(client))