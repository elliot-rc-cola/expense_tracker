# expense tracker that lets you add expesne, list them, show the total expenses and filter by category

#setting up the functions to do each task:
# add an expense and its category
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

# print an expense and the category it belongs to  
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

# calculate the total for all expenses    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

# list all individual expenses from a specific category    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
    
# creates the main menu and fuctionality for user input
def main():
    expenses = []
    # user can specify which task to initiate by choosing the corresponding number
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')
        # populates the empty 'expenses' list that provides data for all other choices
        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
        # break clause to terminate the program
        elif choice == '5':
            print('Exiting the program.')
            break
# shows the menu in the terminal
main()