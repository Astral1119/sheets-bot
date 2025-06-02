import discord
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from discord.ext import commands
from discord import app_commands

class WikiSearch(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.ix = open_dir("wiki/index")

    def format_result(self, result):
        """
        Takes a list of title and URL pairs and formats them into an embed.
        """
        # description should be
        # [title](url)
        description = "\n".join(
            f"[{result[0]}]({result[1]})" for result in result
        )

        embed = discord.Embed(
            title="Search Results",
            description=description,
            color=discord.Color.green()
        )

        return embed

    @commands.hybrid_command(name='wiki')
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def search(self, ctx, *, query: str):
        """
        Searches for articles in wiki/articles.
        Then, slugifies the result and returns the sheets.wiki link.
        Note: we use the same articles submodule as the wiki because
        the wiki does not have a search API.
        """
        if not query:
            await ctx.send("Please provide a search query.")
            return
        
        with self.ix.searcher() as searcher:
            query_parser = QueryParser("content", self.ix.schema)
            parsed_query = query_parser.parse(query)
            results = searcher.search(parsed_query, limit=5)

            if not results:
                await ctx.send("No results found.")
                return

            response = []
            for result in results:
                response.append((result['title'], result['url']))
            
            embed = self.format_result(response)
            await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(WikiSearch(client))
