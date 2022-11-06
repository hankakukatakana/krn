import sqlite3

dbname = 'lifeline.db'

conn = sqlite3.connect(dbname)
conn = execute("CREATE TABLE lifeline(mm, category, prise)")

conn = close()