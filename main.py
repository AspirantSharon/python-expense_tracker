import sys
from add_expense import add_expense
from view_expenses import view_expenses
from delete_expense import delete_expense

def main():
    print("Welcome to the Python Expense Tracker!")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        date = input("Enter expense date (YYYY-MM-DD): ")
        add_expense(description, amount, date)
        print("Expense added successfully!")
    
    elif choice == '2':
        print("All Expenses:")
        view_expenses()
    
    elif choice == '3':
        expense_id = int(input("Enter the expense ID to delete: "))
        delete_expense(expense_id)
        print("Expense deleted successfully!")
    
    elif choice == '4':
        print("Exiting the Expense Tracker. Goodbye!")
        sys.exit()
    
    else:
        print("Invalid choice. Please try again.")

if __name__ == '__main__':
    while True:
        main()

