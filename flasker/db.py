import sqlite3

dbname = 'lifeline.db'
def create_table():
    con = sqlite3.connect(dbname)
    con.execute("CREATE TABLE IF NOT EXISTS lifeline (mm, category, price)")
    con.close()