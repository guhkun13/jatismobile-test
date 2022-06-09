import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
  connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO user (username) VALUES (?)", ('guhkun13',))

connection.commit()
connection.close