"""
parrot is a Discord bot cog that dynamically loads commands from a dictionary.
"""

command_list = {
    "apis":
        """
        map: Returns an example of map function usage within Google Sheets
        scan: Returns an example of scan function usage within Google Sheets
        reduce: Returns an example of reduce function usage within Google Sheets
        lambda: Returns an example of using lambda within Google Sheets
        documentation: Returns how to use let to incorporate documentation in your formulas for Google Sheets
        """,
    "learngas":
        """
        [ExcelGoogleSheets](https://www.youtube.com/@ExcelGoogleSheets/search?query=apps%20script)
        [Ben Collins](https://courses.benlcollins.com/p/apps-script-blastoff)
        [Spencer Farris](https://www.youtube.com/playlist?list=PLmE9Sui7JoQGqOJvhxYRjOFUtr5kMWUtJ)
        """,
    "notable":
        """
        [Advanced Dropdown Setups](https://docs.google.com/spreadsheets/d/1OlRIXjoaUG5Owjd3t9hGfmV7G8EmAKffP7YVPdNGNH0/edit?usp=sharing)
        [A History of Crash Bugs](https://docs.google.com/spreadsheets/d/107B_jSpObwxxYfL_HTBWZtB9cnMQDTraoirpaRUsNLc/edit?gid=582260365#gid=582260365)
        [Community Practice Problems](https://docs.google.com/spreadsheets/d/1RZVTUJj_qzugq_WCd7rMjmjzKtUM72Jb5x0RGFAVNnk/edit?gid=890374412#gid=890374412)
        """,
}

import discord
from discord.ext import commands
from discord import app_commands

class Parrot(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.commands = []


        for command_name, description in command_list.items():
            self.commands.append(command_name)
            self.add_parrot_command(command_name)

    def add_parrot_command(self, command_name):
        command_data = command_list[command_name]

        @app_commands.allowed_installs(guilds=True, users=True)
        @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
        async def parrot(ctx):
            description = command_data
            embed = discord.Embed(
                title=command_name,
                description=description,
                color=discord.Color.green()
            )
            await ctx.send(embed=embed)

        parrot.__name__ = command_name  # set correct function name
        self.client.add_command(commands.hybrid_command(name=command_name)(parrot))

async def setup(client):
    await client.add_cog(Parrot(client))
