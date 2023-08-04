import sqlite3

# conect to anew db file called mydatabse.db
conn = sqlite3.connect('mydatabase.db')

# close the database connection
conn.close()