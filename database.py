import sqlite3

# Connect to SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect('expenses.db')

# Create a cursor object
c = conn.cursor()

# Create a table for expenses
c.execute('''CREATE TABLE IF NOT EXISTS expenses
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
              description TEXT, 
              amount REAL, 
              date TEXT)''')

# Commit changes and close the connection
conn.commit()
conn.close()
