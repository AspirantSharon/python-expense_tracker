import sqlite3

def view_expenses():
    # Connect to the database
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    
    # Retrieve all expenses from the database
    c.execute("SELECT * FROM expenses")
    expenses = c.fetchall()
    
    # Print expenses
    for expense in expenses:
        print(f"ID: {expense[0]}, Description: {expense[1]}, Amount: {expense[2]}, Date: {expense[3]}")
    
    # Close the connection
    conn.close()

# Example usage
view_expenses()
