import sqlite3


def add_expense(description, amount, date):
    # Connect to the database
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    
    # Insert the expense into the database
    c.execute("INSERT INTO expenses (description, amount, date) VALUES (?, ?, ?)", 
              (description, amount, date))
    
    # Commit and close
    conn.commit()
    conn.close()

# Example usage
add_expense("Lunch", 10.50, "2024-11-07")
