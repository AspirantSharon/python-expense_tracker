import sqlite3

def delete_expense(expense_id):
    # Connect to the database
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    
    # Delete the expense based on its ID
    c.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Example usage
delete_expense(1)  # Deletes the expense with ID 1
