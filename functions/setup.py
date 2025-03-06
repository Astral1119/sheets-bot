import sqlite3

db = sqlite3.connect('sheets-bot.db')
c = db.cursor()

# excel table
# id, name, type, syntax, description, link
c.execute('''
CREATE TABLE IF NOT EXISTS excel (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    type TEXT,
    syntax TEXT,
    description TEXT,
    link TEXT
)
''')

# google sheets table
# id, name, type, syntax, description, link
c.execute('''
CREATE TABLE IF NOT EXISTS sheets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    type TEXT,
    syntax TEXT,
    description TEXT,
    link TEXT
)
''')