import sqlite3

dbname = 'lifeline.db'
con = sqlite3.connect(dbname)

cur = con.cursor()

con.execute("CREATE TABLE lifeline(mm, category, prise)")
#cur.execute('INSENT INTO lifeline values()')

con.close()