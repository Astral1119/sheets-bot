# define schema
from whoosh.fields import Schema, TEXT

schema = Schema(
    title=TEXT(stored=True),
    content=TEXT,
    url=TEXT(stored=True)
)

# create index directory if it doesn't exist
import os.path
from whoosh.index import create_in

if not os.path.exists("index"):
    os.mkdir("index")
ix = create_in("index", schema)

# add documents to the index
from whoosh.index import open_dir

ix = open_dir("index")

writer = ix.writer()

import os

# import all articles from ./articles
def index_articles():
    articles_path = "articles"
    for root, dirs, files in os.walk(articles_path):
        for filename in files:
            if filename.endswith(".md"):
                full_path = os.path.join(root, filename)
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    title = filename[:-3]  # remove .md extension

                    # build the slug path
                    relative_path = os.path.relpath(full_path, articles_path)
                    slug = relative_path.replace(".md", "").replace(" ", "-")
                    url = 'https://sheets.wiki/' + slug

                    writer.add_document(title=title, content=content, url=url)

    writer.commit()

if __name__ == "__main__":
    index_articles()
    print("Indexing complete. Articles have been indexed.")
    print("You can now use the search command in the wiki bot to search for articles.")
