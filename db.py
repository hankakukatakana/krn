import sqlite3

dbname = 'lifeline.db'
conn = sqlite3.connect(dbname)

cur = conn.cursor()

conn = execute("CREATE TABLE lifeline(mm, category, prise)")
#cur.execute('INSENT INTO lifeline values()')

conn = close()